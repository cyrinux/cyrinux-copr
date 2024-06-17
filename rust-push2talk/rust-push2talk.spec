%global crate push2talk
%global forgeurl https://github.com/cyrinux/push2talk
%global tag    1.3.1
%forgemeta

Name:           rust-push2talk
Version:        1.3.1
Release:        %autorelease -b1
Summary:        Push to talk application is working with both wayland/x11 and pulseaudio

License:        ISC
URL:            %{forgeurl}
Source0:        %{crates_source}
Source1:        %{crate}-%{version}-vendor.tar.xz
Source2:        https://raw.githubusercontent.com/cyrinux/%{crate}/%{version}/push2talk.service

BuildRequires:  cargo-rpm-macros >= 25
BuildRequires:  rust-libudev-devel
BuildRequires:  rust-libpulse-binding-devel
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  systemd-rpm-macros
Requires:       pipewire-pulseaudio systemd
%{?systemd_requires}


%global _description %{expand:
This Push to talk application is working with both wayland/x11 and
pulseaudio (pipewire).}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        ISC

%description -n %{crate} %{_description}

%prep
%autosetup -n %{crate}-%{version} -p1 -a1
%cargo_prep -v vendor

%files       -n %{crate}
%license LICENSE.md
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_userunitdir}/%{crate}.service
%{_bindir}/%{crate}

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%cargo_install
%{__install} -Dm 0644 -t %{buildroot}%{_userunitdir}/ %{crate}.service

%systemd_user_post %{crate}.service
%systemd_user_preun %{crate}.service

%changelog
%autochangelog

