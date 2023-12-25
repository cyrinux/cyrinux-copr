%bcond_without check

# prevent library files from being installed
%global __cargo_is_lib() 0

%global crate wldash
%global commitId 70e53c1246e0d35b78c5db5146d0da6af716c293

Name:           wldash
Version:        0.3.0
Release:        %autorelease
Summary:        A very good tiny wayland launcher.

SourceLicense:  None
License:        GPLv3

Url: https://github.com/kennylevinsen/%{crate}
Source0: https://git.sr.ht/~kennylevinsen/%{crate}/archive/%{commitId}.tar.gz
Source1: https://levis.name/%{crate}-%{version}-vendor.tar.xz 
Patch: 0000-cargo.toml.patch

BuildRequires: git
BuildRequires: cargo-rpm-macros >= 25
BuildRequires: alsa-lib-devel
BuildRequires: fontconfig-devel
BuildRequires: dbus-devel
BuildRequires: pulseaudio-libs-devel

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%autosetup -S git -v -n %{crate}-%{commitId} -p1 -a1
%cargo_prep -v vendor

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/wldash

%changelog
* Mon Dec 25 2023 Cyril Levis <git@levis.name> 0.3.0-1
- new package built with tito

* Mon Dec 25 2023 Cyril Levis <git@levis.name>
-  Init wldash

%autochangelog