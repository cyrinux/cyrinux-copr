.PHONY: prepare goprep rustprep srpm
specfile = $(notdir $(spec))

prepare:
	dnf install --nodocs -y rpm-build rpmdevtools

goprep:
	dnf install --nodocs -y golang git-core
	go env -w GOPROXY=https://proxy.golang.org,direct
	go env -w GOSUMDB=sum.golang.org

golang-%.spec: goprep
	@if [ -x bundle_go_deps_for_rpm.sh ]; then \
		bash bundle_go_deps_for_rpm.sh $(specfile)
	fi

rustprep:
	dnf install --nodocs -y rust2rpm git-core

rust-%.spec: rustprep
	@if [ -x bundle_rust_deps_for_rpm.sh ]; then \
		bash bundle_rust_deps_for_rpm.sh $(specfile)
	fi

%.spec:
	echo "Nothing to do"

srpm: prepare $(specfile)
	spectool -g ./$(specfile)
	rpmbuild -bs --define "_sourcedir ${PWD}" --define "_specdir ${PWD}" \
		--define "_builddir ${PWD}" --define "_srcrpmdir $(outdir)" --define \
		"_rpmdir ${PWD}" --define "_buildrootdir ${PWD}/.build" $(specfile)
