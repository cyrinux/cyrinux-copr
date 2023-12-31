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
Source:     %{url}/archive/refs/tags/v%{version}.tar.gz

%description %{common_description}

%prep
%autosetup -n %{name}-%{version} -p1

%build
make

%install
install -dm 0755 -v %{buildroot}%{_bindir}
install -Dm 0755 -v -t %{buildroot}%{_bindir}/ %{name}
install -dm 0755 -v %{buildroot}%{_sysconfdir}/xdg/autostart
install -Dm 0644 -v -t %{buildroot}%{_sysconfdir}/xdg/autostart/ %{name}.desktop

%files
%{_bindir}/%{name}
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%license LICENSE
%doc README.md

%changelog
%autochangelog
