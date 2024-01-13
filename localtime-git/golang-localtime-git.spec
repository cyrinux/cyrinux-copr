%global forgeurl        https://github.com/Stebalien/localtime
%global commit0         2dcc765c550cea3b6e3791404928857f02e2505e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 3
%global commit  %{commit0}
%forgemeta

%global gomodulesmode GO111MODULE=on

%global common_description %{expand:
A daemon for keeping the system timezone up-to-date based on the current location.}

%global golicenses      LICENSE
%global godocs          README.md

%global _name localtime

Name:    %{_name}-git
Version: 0.1.0%{?bumpver:^%{bumpver}.git%{shortcommit0}}
Release: %autorelease
Summary: A daemon for keeping the system timezone up-to-date based on the current location

License: GPL-3.0
URL:     %{forgeurl}
Source0: %{forgesource}
BuildRequires: systemd-rpm-macros go-rpm-macros git-core m4 make
Provides: %{_name}
Requires: geoclue2 polkit dbus
%{?systemd_requires}

%description %{common_description}

%prep
%autosetup -n %{_name}-%{commit0}

%build
%gobuild -o %{gobuilddir}/bin/localtimed ./
export PREFIX=%{_usr}
%{__make} localtime-geoclue-agent.service localtime.service localtime.sysusers polkit.rules
%{__sed} -i '/ExecStart/s/lib/libexec/' localtime-geoclue-agent.service

%install
%{__install} -m 0755 -vd %{buildroot}%{_bindir}
%{__install} -m 0755 -vt %{buildroot}%{_bindir}/ %{gobuilddir}/bin/localtimed
%{__install} -Dm644 polkit.rules %{buildroot}%{_usr}/share/polkit-1/rules.d/40-localtime.rules
%{__install} -Dm644 localtime.service %{buildroot}%{_unitdir}/localtime.service
%{__install} -Dm644 localtime.sysusers %{buildroot}%{_usr}/lib/sysusers.d/localtime.conf
%{__install} -Dm644 localtime-geoclue-agent.service %{buildroot}%{_unitdir}/localtime-geoclue-agent.service

%pre
if [ $1 == 1 ]; then
    useradd -r -U localtimed 2> /dev/null; true
fi

%post
if [ $1 == 1 ]; then
    %systemd_post localtime.service
fi

%preun
if [ $1 == 0 ]; then
    %systemd_preun localtime.service
fi

%postun
if [ $1 == 0 ]; then
    userdel --force localtimed 2> /dev/null; true
fi

%files
%defattr(-,root,root,-)
%license LICENSE
%doc README.md
%{_bindir}/localtimed
%{_unitdir}/localtime.service
%{_unitdir}/localtime-geoclue-agent.service
%{_usr}/lib/sysusers.d/localtime.conf
%{_usr}/share/polkit-1/rules.d/40-localtime.rules

%changelog
%autochangelog
