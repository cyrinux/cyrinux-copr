%bcond_without check

%global __cargo_is_lib() 0

%global crate repgrep

Name:           rust-repgrep
Version:        0.15.0
%global tag     0.15.0
Release:        %autorelease
Summary:        An interactive replacer for ripgrep that makes it easy to find and replace across files on the command line

License:        Unlicense OR MIT OR Apache-2.0
URL:            https://github.com/acheronfail/repgrep
Source0:        %{crates_source}
Source1:        %{crate}-%{tag}-vendor.tar.xz

BuildRequires:  cargo-rpm-macros >= 25
BuildRequires:  asciidoctor

%global _description %{expand:
An interactive replacer for ripgrep that makes it easy to find and replace across files on the command line.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        Unlicense OR MIT OR Apache-2.0

%description -n %{crate} %{_description}

%files       -n %{crate}
%{_bindir}/rgr
%license LICENSE-APACHE
%license LICENSE-MIT
%license LICENSE-UNLICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md

%prep
%autosetup -n %{crate}-%{version} -p1 -a1
%cargo_prep -v vendor

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
