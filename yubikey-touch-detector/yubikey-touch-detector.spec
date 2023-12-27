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
Release:        %autorelease
Summary:        A tool to detect when your YubiKey is waiting for a touch (to send notification or display a visual indicator on the screen)

License:        ISC
URL:            %{gourl}
Source0:        %{gosource}
Source1:        https://raw.githubusercontent.com/maximbaz/%{goname}/%{version}/%{goname}.service
Source2:        https://raw.githubusercontent.com/maximbaz/%{goname}/%{version}/%{goname}.socket
Source3:        https://raw.githubusercontent.com/maximbaz/%{goname}/main/service.conf.example

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
%{__install} -dm 0755 -v %{buildroot}%{_userunitdir}/
%{__install} -Dm 0644 -v -t %{buildroot}%{_userunitdir}/ %{_sourcedir}/%{goname}.service
%{__install} -Dm 0644 -v -t %{buildroot}%{_userunitdir}/ %{_sourcedir}/%{goname}.socket
%{__install} -Dm 0644 -v -t %{buildroot}%{_pkgdocdir}/ %{_sourcedir}/service.conf.example

%gopkginstall
%{__install} -dm 0755 -v %{buildroot}%{_bindir}
%{__install} -Dm 0755 -v %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

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
%autochangelog
