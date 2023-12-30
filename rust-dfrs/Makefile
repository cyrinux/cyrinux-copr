cur_dir := $(shell pwd)
crate := "$(shell basename $(cur_dir))"

all: create build

create:
	echo "Creating crate $(crate)"
	copr add-package-custom misc --script ./bootstrap --name $(crate) --script-builddeps "curl rust2rpm git" --webhook-rebuild on

build:
	copr build-package --nowait misc --name $(crate)
