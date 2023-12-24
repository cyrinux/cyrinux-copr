%bcond_without check

%global __cargo_is_lib() 0

%global crate dfrs

Name:           rust-dfrs
Version:        0.0.7
%global tag     0.0.7
Release:        %autorelease -b1
Summary:        Display file system space usage using graphs and colors

License:        MIT
URL:            https://github.com/anthraxx/dfrs
Source:         %{crates_source}
Source:         dfrs-%{tag}-vendor.tar.xz

BuildRequires:  cargo-rpm-macros >= 25

%global _description %{expand:
Display file system space usage using graphs and colors.}

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
%{_bindir}/dfrs

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
