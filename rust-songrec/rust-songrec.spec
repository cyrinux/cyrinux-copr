%bcond_without check
%global __cargo_is_lib() 0

%global tag 0.4.0
%global forgeurl https://github.com/marin-m/SongRec
%forgemeta

%global crate songrec

Name:           rust-songrec
Version:        0.4.0
Release:        %autorelease -b1
Summary:        Open-source Shazam client for Linux, written in Rust

License:        GPL-3.0+
URL:            https://crates.io/crates/songrec
Source:         %{crates_source}
Source:         songrec-%{tag}-vendor.tar.xz

BuildRequires:  cargo-rpm-macros >= 25
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pipewire-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(pango)
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  gtk3-devel

%global _description %{expand:
An open-source Shazam client for Linux, written in Rust.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        GPL-3.0+

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/songrec

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
