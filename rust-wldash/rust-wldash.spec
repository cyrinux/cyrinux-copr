%bcond_without check

%global forgeurl https://git.sr.ht/~kennylevinsen/wldash
%global commit 70e53c1246e0d35b78c5db5146d0da6af716c293
%forgemeta

Name:           wldash
Version:        0.3.0
Release:        %autorelease
Summary:        A very good tiny wayland launcher.

SourceLicense:  None
License:        GPLv3

Url:     %{forgeurl}
Source0: %{forgesource}

BuildRequires: cargo-rpm-macros >= 25
BuildRequires: git-core
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(libpulse)
BuildRequires: dbus-devel

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%forgeautosetup -p1
%{__cargo} fetch --locked

%build
export RUSTUP_TOOLCHAIN=stable
export CARGO_TARGET_DIR=target
%{__cargo} build --frozen --release

%install
%{__install} -m 0755 -vd %{buildroot}%{_bindir}
%{__install} -Dm 0755 -t %{buildroot}%{_bindir}/ "target/release/%{name}"

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%changelog
%autochangelog
