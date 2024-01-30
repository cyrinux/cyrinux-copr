%bcond_without check

%global __cargo_is_lib() 0

%global crate skyspell

Name:           rust-skyspell
Version:        1.0.2
%global tag     v1.0.2
Release:        %autorelease
Summary:        Fast and handy spell checker for the command line

License:        BSD-3-Clause
URL:            https://github.com/your-tools/skyspell
Source:         %{crates_source}
Source:         %{crate}-%{version}-vendor.tar.xz

BuildRequires:  cargo-rpm-macros >= 25
BuildRequires:  enchant2-devel sqlite-devel
Recommends: aspell aspell-en

%global _description %{expand:
Fast and handy spell checker for the command line.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        BSD-3-Clause

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/skyspell

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
