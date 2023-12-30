#!/bin/sh
crate="$(basename $(pwd))"
echo "Creating crate $crate"
copr add-package-scm misc --clone-url https://github.com/cyrinux/cyrinux-copr --subdir $crate --method make_srpm --webhook-rebuild on --name $crate
copr build-package --nowait misc --name $crate
