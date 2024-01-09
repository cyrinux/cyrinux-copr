%global forgeurl https://github.com/rfjakob/systembus-notify
%global tag v1.1
%forgemeta

Version:   1.1

%global name systembus-notify

%global common_description %{expand:
Systembus-notify - system bus notification daemon.}

%global licenses      LICENSE
%global docs          README.md

Name:      %{name}
Release:   %autorelease -b1
Summary:   Systembus-notify - system bus notification daemon
License:   MIT
URL:       %{forgeurl}
Source:    %{forgesource}

BuildRequires: clang
BuildRequires: systemd-devel
Requires: systemd

%description %{common_description}

%prep
%autosetup -n %{name}-%{version} -p1

%build
%{__make}

%install
%{__install} -dm 0755 -v %{buildroot}%{_bindir}
%{__install} -Dm 0755 -v -t %{buildroot}%{_bindir}/ %{name}
%{__install} -dm 0755 -v %{buildroot}%{_sysconfdir}/xdg/autostart
%{__install} -Dm 0644 -v -t %{buildroot}%{_sysconfdir}/xdg/autostart/ %{name}.desktop

%files
%{_bindir}/%{name}
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%license LICENSE
%doc README.md

%changelog
%autochangelog
