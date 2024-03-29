%bcond_without check

%global __cargo_is_lib() 0

%global crate skyspell_kak

Name:           rust-skyspell-kak
Version:        1.0.3
%global tag     v1.0.3
Release:        %autorelease -b2
Summary:        Kakoune integration for skyspell

License:        BSD-3-Clause
URL:            https://github.com/your-tools/skyspell
Source:         %{crates_source}
Source:         %{crate}-%{version}-vendor.tar.xz

BuildRequires:  cargo-rpm-macros >= 25
BuildRequires:  enchant2-devel sqlite-devel


%global _description %{expand:
Kakoune integration for skyspell.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        BSD-3-Clause
Requires:       skyspell
Provides:       skyspell-kak

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/skyspell-kak

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
