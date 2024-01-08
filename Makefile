# Usage: make package=pkg_directory create
SHELL := /bin/bash
package ?= .
cur_dir := $(realpath $(package))
SPEC_FILE = $(wildcard $(package)/*.spec)
SPEC_NAME := $(shell basename $(SPEC_FILE))
PKG := $(notdir $(cur_dir))
PROJECT := "misc"
GIT_COPR_URL := "https://github.com/cyrinux/cyrinux-copr"

all: check_requirements create rebuild

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
	@echo "Creating $(PKG) on $(PROJECT) with $(SPEC_FILE)"
	copr-cli add-package-scm $(PROJECT) \
		--clone-url $(GIT_COPR_URL) \
		--subdir $(PKG) \
		--method make_srpm \
		--spec $(SPEC_NAME) \
		--commit main \
		--webhook-rebuild on \
		--name $(PKG)

# Build from local spec file
build:
	copr-cli build --nowait misc $(SPEC_FILE)

# Rebuild the package for repo
rebuild:
	copr-cli build-package --nowait misc --name $(PKG)

# Delete the package
delete:
	copr-cli delete-package misc --name $(PKG)

.PHONY: create build rebuild delete update_version check_requirements

