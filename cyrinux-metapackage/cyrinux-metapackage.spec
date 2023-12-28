Name:           cyrinux-meta
Version:        1.0
Release:        1%{?dist}
Summary:        Cyrinux metapackage
BuildArch:      noarch
License:        GPLv3
URL:            copr://cyrinux/misc
Source0:        fonts.tar.gz

Requires: NetworkManager-openvpn
Requires: NetworkManager-openvpn-gnome
Requires: NetworkManager-wifi
Requires: ShellCheck
Requires: SwayNotificationCenter
Requires: abattis-cantarell-fonts
Requires: acpi
Requires: adwaita-qt5
Requires: adwaita-qt6
Requires: alsa-ucm-asahi
Requires: asahi-fwupdate
Requires: asahi-platform-metapackage
Requires: asahi-repos
Requires: asdf-vm
Requires: basesystem
Requires: bat
Requires: binwalk
Requires: browserpass
Requires: browserpass-chromium
Requires: browserpass-firefox
Requires: calibre
Requires: cargo
Requires: chromium
Requires: containerd.io
Requires: copr-cli
Requires: cyrinux-meta
Requires: darkman
Requires: dash
Requires: dejavu-fonts-all
Requires: direnv
Requires: dnf
Requires: docker-buildx-plugin
Requires: docker-ce
Requires: docker-ce-cli
Requires: docker-compose-plugin
Requires: dracut-asahi
Requires: dracut-kbd-backlight
Requires: dua-cli
Requires: earlyoom
Requires: eza
Requires: fd-find
Requires: fedora-asahi-remix-scripts
Requires: filesystem
Requires: firefox
Requires: flatpak
Requires: fontawesome-fonts-all
Requires: fping
Requires: freerdp
Requires: fzf
Requires: gdisk
Requires: geoclue2-demos
Requires: gh
Requires: ghq
Requires: gimp
Requires: git-delta
Requires: gitui
Requires: glibc-all-langpacks
Requires: gnome-keyring
Requires: go2rpm
Requires: gocryptfs
Requires: goimapnotify
Requires: golang
Requires: google-noto-sans-fonts
Requires: google-noto-serif-fonts
Requires: graphviz
Requires: grub2-efi-aa64
Requires: grub2-efi-aa64-modules
Requires: grubby
Requires: helvum
Requires: htop
Requires: hyprland
Requires: hyprland-autoname-workspaces
Requires: initial-setup
Requires: inotify-tools
Requires: isync
Requires: iwd
Requires: kak-lsp
Requires: kakoune
Requires: kernel-16k
Requires: kernel-16k-modules-extra
Requires: khal
Requires: lato-fonts
Requires: lftp
Requires: liberation-fonts
Requires: libgnome-keyring
Requires: light
Requires: meld
Requires: mock
Requires: moreutils
Requires: mpv
Requires: neomutt
Requires: network-manager-applet
Requires: nextcloud-client
Requires: nmap
Requires: nmtrust
Requires: notmuch
Requires: obs-studio
Requires: open-sans-fonts
Requires: pam-u2f
Requires: pamu2fcfg
Requires: paperwork
Requires: pass
Requires: passmenu
Requires: pavucontrol
Requires: perl
Requires: pinentry-gnome3
Requires: pipewire-utils
Requires: polkit-gnome
Requires: privoxy
Requires: progress
Requires: proxychains-ng
Requires: pulseaudio-utils
Requires: pwgen
Requires: pyp2rpm
Requires: python-unversioned-command
Requires: qalculate-gtk
Requires: qemu
Requires: restic
Requires: rust-analyzer
Requires: rust2rpm
Requires: rustfmt
Requires: setroubleshoot
Requires: shim-aa64
Requires: signal-desktop
Requires: songrec
Requires: sqlite
Requires: supertuxkart
Requires: swappy
Requires: swaybg
Requires: swayidle
Requires: swaylock
Requires: systembus-notify
Requires: systemd-oomd-defaults
Requires: tarsnap
Requires: terminus-fonts-console
Requires: tig
Requires: tiny-dfr
Requires: tito
Requires: tlp
Requires: tmux
Requires: tor
Requires: torsocks
Requires: trash-cli
Requires: typetogether-literata-fonts
Requires: uboot-images-armv8
Requires: udiskie
Requires: update-m1n1
Requires: usbguard-dbus
Requires: vdirsyncer
Requires: vimiv-qt
Requires: waybar
Requires: wev
Requires: wireguard-tools
Requires: wldash
Requires: yubikey-manager
Requires: yubikey-touch-detector
Requires: zathura-pdf-mupdf
Requires: zsh
Requires: SwayAudioIdleInhibit


%description
This is the meta package that installs the core components.

%prep
%setup -q -n fonts

%install
%{__install} -m 0755 -vd %{buildroot}%{_fontbasedir}/cyrinux/
%{__install} -m 0755 -vp *.ttf %{buildroot}%{_fontbasedir}/cyrinux/

%post
fc-cache -rv >/dev/null 2>&1

%postun
fc-cache -rv >/dev/null 2>&1

%files
%defattr(644,root,root,-)
%{_fontbasedir}/cyrinux/*.ttf


%changelog
%autochangelog
