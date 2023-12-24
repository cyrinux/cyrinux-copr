SHELL := /bin/bash

package ?= .
SPEC_FILE = $(wildcard $(package)/*.spec)
cur_dir := $(realpath $(package))
pkg := $(notdir $(cur_dir))

all: check_requirements create build

# Check if SPEC_FILE is empty
ifeq ($(strip $(SPEC_FILE)),)
$(error No .spec file found in the current directory)
endif

# Check for required commands
check_requirements:
	@command -v awk >/dev/null 2>&1 || { echo >&2 "AWK is not installed. Aborting."; exit 1; }
	@command -v git >/dev/null 2>&1 || { echo >&2 "Git is not installed. Aborting."; exit 1; }
	@command -v copr-cli >/dev/null 2>&1 || { echo >&2 "Copr CLI 'copr-cli' is not installed. Aborting."; exit 1; }


# Create the package
create:
	@echo "Creating $(pkg)"
	copr-cli add-package-scm misc --clone-url https://github.com/cyrinux/cyrinux-copr --subdir $(pkg) --method make_srpm --webhook-rebuild on --name $(pkg) || true

# Build from local spec file
build:
	copr-cli build --nowait misc $(SPEC_FILE)

# Rebuild the package for repo
rebuild:
	copr-cli build-package --nowait misc --name $(pkg)

# Delete the package
delete:
	copr-cli delete-package misc --name $(pkg)

.PHONY: create build rebuild delete update_version check_requirements

