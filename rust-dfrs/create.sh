#!/bin/sh
crate="$(basename $(pwd))"
echo "Creating crate $crate"
copr add-package-custom misc --script ./bootstrap --name $crate --script-builddeps "curl rust2rpm git" --webhook-rebuild on
copr build-package --nowait misc --name $crate
