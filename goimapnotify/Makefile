cur_dir := $(shell pwd)
pkg := "$(shell basename $(cur_dir))"

all: create build

create:
	@echo "Creating $(pkg)"
	copr add-package-scm misc --clone-url https://github.com/cyrinux/cyrinux-copr --subdir goimapnotify --method tito --webhook-rebuild on  --name $(pkg)

build:
	copr build-package --nowait misc --name $(pkg)

delete:
	copr delete-package misc --name $(pkg)

.PHONY: create build delete
