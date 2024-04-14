%bcond_without check

%global __cargo_is_lib() 0

%global crate swayr

Name:           rust-swayr
Version:        0.27.3
%global tag     0.27.3
Release:        %autorelease
Summary:        A LRU window-switcher (and more) for the sway window manager

License:        GPLv3
URL:            https://github.com/anthraxx/dfrs
Source:         %{crates_source}
Source:         dfrs-%{tag}-vendor.tar.xz

BuildRequires:  cargo-rpm-macros >= 25

%global _description %{expand:
A LRU window-switcher (and more) for the sway window manager.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        GPLv3

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/swayr
%{_bindir}/swayrd

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
