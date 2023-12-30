cur_dir := $(shell pwd)
crate := "$(shell basename $(cur_dir))"

all: create push build

push:
	git push

create:
	@echo "Creating crate $(crate)"
	copr add-package-custom misc --script ./bootstrap --name $(crate) --script-builddeps "curl systemd-rpm-macros rust2rpm git openssl-devel" --webhook-rebuild on || true

build:
	copr build-package --nowait misc --name $(crate)

delete:
	copr delete-package misc --name $(crate)

.PHONY: create push build delete
