#!/bin/bash
# Description:
# This script creates an archive with vendored dependencies from a rust SPEC file.

# Check if the RPM SPEC file is given as an argument
if [[ $# -ne 1 ]]; then
    echo "Usage: $0 <path_to_rpm_spec_file>"
    exit 1
fi

RPM_SPEC_FILE=$1

# Extract the directory from the RPM SPEC file path
SPEC_DIR=$(dirname $(realpath "$RPM_SPEC_FILE"))

# Extract the URL, commit, tag, and version from the RPM SPEC file
CRATE=$(awk '/^%global crate/ {print $NF}' "$RPM_SPEC_FILE")
VERSION=$(rpmspec -q --qf "%{version}\n" "$RPM_SPEC_FILE" | head -1 | sed 's/\^.*//')

rust2rpm -V -s $CRATE $VERSION > /dev/null
