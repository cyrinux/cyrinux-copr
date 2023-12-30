srpm:
	dnf install -y openssl openssl-devel git curl
	dnf install -y rust2rpm
	rm -rf /build/package
	rm -rf /tmp/\_topdir
	rm -rf /tmp/scratch
	mkdir -p /tmp/\_topdir/SOURCES
	mkdir -p /tmp/scratch
	cp -r ./\* /tmp/scratch
	cd /tmp/scratch;
	rust2rpm -V -s dfrs
	rpmbuild -bs --define "\_topdir /tmp/\_topdir" /tmp/scratch/rust-dfrs.spec
	cp -r /tmp/\_topdir/SRPMS/\* \$(outdir)

.PHONY: srpm
