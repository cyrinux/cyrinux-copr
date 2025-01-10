%bcond_without check

%global goipath         github.com/maximbaz/yubikey-touch-detector
Version:                1.12.5
%global tag             1.12.5

%gometa -L -f

%global goname yubikey-touch-detector

%global common_description %{expand:
A tool to detect when your YubiKey is waiting for a touch (to send notification
or display a visual indicator on the screen).}

%global golicenses      LICENSE
%global godocs          README.md

Name:    %{goname}
Release: %autorelease -b6
Summary: A tool to detect when your YubiKey is waiting for a touch (to send notification or display a visual indicator on the screen)

License: ISC
URL:     https://github.com/maximbaz/yubikey-touch-detector
Source0: https://github.com/maximbaz/%{goname}/releases/download/%{version}/%{goname}-%{version}-src.tar.gz
Source1: vendor-%{version}.tar.gz
Source2: bundle_go_deps_for_rpm.sh
Source3: https://raw.githubusercontent.com/maximbaz/%{goname}/%{version}/%{goname}.service
Source4: https://raw.githubusercontent.com/maximbaz/%{goname}/%{version}/%{goname}.socket
Source5: https://raw.githubusercontent.com/maximbaz/%{goname}/main/service.conf.example
Source6: https://github.com/maximbaz/%{goname}/releases/download/%{version}/%{goname}-%{version}-src.tar.gz.asc
Source7: https://github.com/maximbaz.gpg


BuildRequires: systemd-rpm-macros go-rpm-macros golang git-core gnupg2 gpgme-devel
Requires: gpgme
%{?systemd_requires}

%description %{common_description}

%prep
%{gpgverify} --keyring='%{SOURCE7}' --signature='%{SOURCE6}' --data='%{SOURCE0}'
%goprep -k
%setup -q -T -D -a 1
%autopatch -p1


%build
%gobuild -o %{gobuilddir}/bin/%{goname} %{goipath}
%{_fixperms} %{gobuilddir}

%install
%{__install} -dm 0755 -v %{buildroot}%{_userunitdir}/
%{__install} -Dm 0644 -v -t %{buildroot}%{_userunitdir}/ %{SOURCE3}
%{__install} -Dm 0644 -v -t %{buildroot}%{_userunitdir}/ %{SOURCE4}
%{__install} -Dm 0644 -v -t %{buildroot}%{_pkgdocdir}/  %{SOURCE5}
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

%changelog
%autochangelog
