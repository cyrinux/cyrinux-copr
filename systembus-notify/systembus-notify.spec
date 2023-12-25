%global debug_package %{nil}

# https://github.com/rfjakob/systembus-notify
Version:                1.1

%global name systembus-notify

%global common_description %{expand:
Systembus-notify - system bus notification daemon.}

%global licenses      LICENSE
%global docs          README.md

Name:           %{name}
Release:        %autorelease
Summary:        Systembus-notify - system bus notification daemon

BuildRequires: clang
BuildRequires: systemd-devel


License:        MIT
URL:        https://github.com/rfjakob/systembus-notify
Source:     https://github.com/rfjakob/%{name}/archive/refs/tags/v%{version}.tar.gz

%description %{common_description}

%prep
%autosetup -n %{name}-%{version} -p1

%build
make

%install
install -dm 0755 -v %{buildroot}%{_bindir}
install -Dm 0755 -v %{name} %{buildroot}%{_bindir}/
install -dm 0755 -v %{buildroot}%{_sysconfdir}/xdg/autostart
install -Dm 0644 -v %{name}.desktop %{buildroot}%{_sysconfdir}/xdg/autostart/

%files
%{_bindir}/%{name}
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%license LICENSE
%doc README.md

%changelog
* Mon Dec 25 2023 Cyril Levis <git@levis.name> 1.1-1
- new package built with tito

%autochangelog
