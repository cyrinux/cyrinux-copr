#!/usr/bin/bash
set -euxo pipefail

PROJECT=cyrinux/misc
NAME=rust-shotman
SPEC=${NAME}.spec
REPO=~whynothugo/shotman

ec=0

oldTag="$(rpmspec -q --qf "%{version}\n" ${SPEC} | head -1 | sed 's/\^.*//')"
newTag="$(curl -s "https://git.sr.ht/${REPO}/refs/rss.xml" | xmllint --xpath '//item[1]/title/text()' - | sed 's/^v//')"

oldCommit="$(sed -n 's/.*\bcommit0\b \(.*\)/\1/p' $SPEC)"
newCommit="$(git ls-remote https://git.sr.ht/${REPO} main | cut -f 1)"

sed -i "s/$oldCommit/$newCommit/" $SPEC

rpmdev-vercmp "$oldTag" "$newTag" || ec=$?
case $ec in
    0) ;;
    12)
        perl -pe 's/(?<=bumpver\s)(\d+)/0/' -i $SPEC
        sed -i "/^Version:/s/$oldTag/$newTag/" $SPEC
        sed -i "/^%global tag/s/$oldTag/$newTag/" $SPEC
        ;;
    *) exit 1 ;;
esac

git diff --quiet ||
    { perl -pe 's/(?<=bumpver\s)(\d+)/$1 + 1/ge' -i $SPEC &&
        git commit -am "up rev ${NAME}-git-${newTag}+${newCommit:0:7}" &&
        git push &&
        copr-cli build-package ${PROJECT} --name ${NAME} --nowait --enable-net on &&
        curl -s "${GOTIFY_URL}/message?token=${GOTIFY_APP_TOKEN}" -F "title=Fedora COPR" -F "message=up rev ${NAME}-${newTag}" -F "priority=5"; }
