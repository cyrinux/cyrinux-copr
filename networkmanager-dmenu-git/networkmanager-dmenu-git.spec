%global commit0 33deba5ac3ab729075ea9a689382d94569b21e6b
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global _name   networkmanager-dmenu
Name:           %{_name}-git
Version:        2.5.0%{?bumpver:^%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        Control NetworkManager via dmenu
License:        MIT
BuildArch:      noarch
URL:            https://github.com/firecat53/networkmanager-dmenu
Source0:        %{url}/archive/%{commit0}/%{_name}-%{shortcommit0}.tar.gz
Provides:       %{_name}
Recommends:     dmenu network-manager-applet libnotify
Requires:       NetworkManager

%description

%prep
%autosetup -n %{_name}-%{commit0} -p1

%build

%install
%{__install} -m 0755 -vd %{buildroot}%{_bindir}
%{__install} -m 0755 -vp networkmanager_dmenu %{buildroot}%{_bindir}/
%{__install} -m 0755 -vd %{buildroot}%{_datarootdir}/applications
%{__install} -m 0644 -vp networkmanager_dmenu.desktop %{buildroot}%{_datarootdir}/applications/



%files
%defattr(-,root,root,-)
%{_bindir}/networkmanager_dmenu
%{_datarootdir}/applications/networkmanager_dmenu.desktop
%license LICENSE.txt
%doc README.md
%doc config.ini.example

%post
echo "To customize networkmanager-dmenu, copy /usr/share/doc/networkmanager-dmenu-git/config.ini.example into ~/.config/networkmanager-dmenu/config.ini and edit it"

%changelog
%autochangelog
