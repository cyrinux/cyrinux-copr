%global _vpath_srcdir .

#global forgeurl https://github.com/ErikReider/SwayAudioIdleInhibit
%global forgeurl https://github.com/rkrishn7/SwayAudioIdleInhibit
%global commit 7a0611fc16e09b0efcf84cae8d4254fa41fcf297
#global tag    v0.1.1
%forgemeta

Name:           SwayAudioIdleInhibit
Version:        0.1.2
Release:        %autorelease -b7
Summary:        Prevents swayidle from sleeping while any application is outputting or receiving audio

License:        GPLv3
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  meson gcc-c++
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wlroots)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pipewire-devel
BuildRequires:  systemd-devel
Requires:       pipewire-pulseaudio
Requires:       libwayland-client

%description

%prep
%autosetup -n %{name}-%{commit} -p1

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
