%bcond_without check
%global __cargo_is_lib() 0

%global crate teehee
%global tag     v0.2.8

Name:           rust-teehee
Version:        0.2.8
Release:        %autorelease -b1
Summary:        Hex editor with inspiration from Vim, Kakoune and Hiew
License:        Apache-2.0
URL:            https://github.com/Gskartwii/teehee
Source:         %{crates_source}
Source:         %{crate}-%{version}-vendor.tar.xz

BuildRequires:  cargo-rpm-macros >= 25

%global _description %{expand:
Hex editor with inspiration from Vim, Kakoune and Hiew.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        Apache-2.0

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc README.md
%{_bindir}/teehee

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

