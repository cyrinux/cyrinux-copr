#!/usr/bin/bash
set -euxo pipefail

PROJECT=cyrinux/misc
NAME=wldash
SPEC=rust-wldash.spec
REPO=~kennylevinsen/wldash
FORGE=sourcehut # sourcehut

ec=0

oldTag="$(rpmspec -q --qf "%{version}\n" ${SPEC} | head -1 | sed 's/\^.*//')"
if [ "$FORGE" == "gitlab" ]; then
    PROJECT_ID=$(curl -s "https://gitlab.com/api/v4/projects?search=${NAME}" | jq ".[] | select(.path_with_namespace == \"${REPO}\") | .id")
    newTag="$(curl -s "https://gitlab.com/api/v4/projects/${PROJECT_ID}/repository/tags?order_by=updated&sort=desc" | jq -r '.[0].name')"
elif [ "$FORGE" == "sourcehut" ]; then
    newTag="$(curl -s "https://git.sr.ht/${REPO}/refs/rss.xml" | xmllint --xpath '//item[1]/title/text()' - | sed 's/^v//')"
else
    newTag="$(curl -s "https://api.github.com/repos/${REPO}/releases" | jq -r '.[0].name' | sed 's/^v//')"
fi

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
        copr-cli build-package ${PROJECT} --name ${NAME} --nowait --enable-net on &&
        curl -s "${GOTIFY_URL}/message?token=${GOTIFY_APP_TOKEN}" -F "title=Fedora COPR" -F "message=up rev ${NAME}-${newTag}" -F "priority=5"; }
