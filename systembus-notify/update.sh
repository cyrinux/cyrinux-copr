#!/usr/bin/bash
set -euxo pipefail

PROJECT=cyrinux/misc
NAME=systembus-notify
SPEC=${NAME}.spec
REPO=rfjakob/systembus-notify

ec=0

oldTag="$(rpmspec -q --qf "%{version}\n" ${SPEC} | head -1 | sed 's/\^.*//')"
newTag="$(curl -s "https://api.github.com/repos/${REPO}/tags" | jq -r '.[0].name' | sed 's/^v//')"

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
        git commit -am "up rev ${NAME}-${newTag}" &&
        git push &&
        copr-cli build-package ${PROJECT} --name ${NAME} --nowait --enable-net on; }
