%bcond_without check
%global __cargo_is_lib() 0

%global crate bore-cli
%global tag     v0.5.1

Name:           rust-bore-cli
Version:        0.5.1
Release:        %autorelease -b1
Summary:        A modern, simple TCP tunnel in Rust that exposes local ports to a remote server, bypassing standard NAT connection firewalls
License:        MIT
URL:            https://github.com/ekzhang/bore
Source:         %{crates_source}
Source:         %{crate}-%{version}-vendor.tar.xz

BuildRequires:  cargo-rpm-macros >= 25

%global _description %{expand:
A modern, simple TCP tunnel in Rust that exposes local ports to a remote server, bypassing standard NAT connection firewalls.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        MIT

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/bore

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

