%global _vpath_srcdir .

Name:           SwayAudioIdleInhibit
Version:        0.1.1
Release:        %autorelease
Summary:        Prevents swayidle from sleeping while any application is outputting or receiving audio

License:        GPLv3
URL:            https://github.com/ErikReider/%{name}
Source:         https://github.com/ErikReider/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  wayland-protocols-devel wlroots-devel
BuildRequires:  pipewire-devel pulseaudio-libs-devel
BuildRequires:  systemd-devel
Requires:       pipewire-pulseaudio
Requires:       libwayland-client

%description

%prep
%autosetup -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%{_bindir}/sway-audio-idle-inhibit
%license LICENSE
%doc README.md

%changelog
%autochangelog
