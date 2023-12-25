# vim: syntax=spec
%bcond_without check

# https://github.com/maximbaz/yubikey-touch-detector
%global goipath         github.com/maximbaz/yubikey-touch-detector
Version:                1.10.1
%global tag             1.10.1

%gometa -f

%global goname yubikey-touch-detector

%global common_description %{expand:
A tool to detect when your YubiKey is waiting for a touch (to send notification
or display a visual indicator on the screen).}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
# Release:      %autorelease
Release:        3%{?dist}
Summary:        A tool to detect when your YubiKey is waiting for a touch (to send notification or display a visual indicator on the screen)

License:        ISC
URL:            %{gourl}
Source0:         %{gosource}
Source1:        https://raw.githubusercontent.com/maximbaz/%{goname}/%{version}/%{goname}.service
Source2:        https://raw.githubusercontent.com/maximbaz/%{goname}/%{version}/%{goname}.socket
Source3:        https://raw.githubusercontent.com/maximbaz/%{goname}/%{version}/service.conf.example

BuildRequires: systemd-rpm-macros
BuildRequires: systemd-devel
BuildRequires: systemd
%{?systemd_requires}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/%{goname} %{goipath}

%install
install -dm 0755 -v %{buildroot}%{_userunitdir}/
install -Dm 0644 -v -t %{buildroot}%{_userunitdir}/ %{_sourcedir}/%{goname}.service
install -Dm 0644 -v -t %{buildroot}%{_userunitdir}/ %{_sourcedir}/%{goname}.socket
install -Dm 0644 -v -t %{buildroot}%{_pkgdocdir}/ %{_sourcedir}/service.conf.example

%gopkginstall
install -dm 0755 -v %{buildroot}%{_bindir}
install -Dm 0755 -v %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%post
%systemd_user_post %{goname}.socket

%preun
%systemd_user_preun %{goname}.socket

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_userunitdir}/%{goname}.service
%{_userunitdir}/%{goname}.socket
%{_pkgdocdir}/service.conf.example

%gopkgfiles

%changelog
* Mon Dec 25 2023 Cyril Levis <git@levis.name> 1.10.1-2
- fix systemd unit

* Mon Dec 25 2023 Cyril Levis <git@levis.name> 1.10.1-1
- new package built with tito

%autochangelog
