%bcond_without check

%global goipath         gitlab.com/shackra/goimapnotify
%global forgeurl        https://gitlab.com/shackra/goimapnotify
Version:                2.3.16
%global tag             2.3.16

%gometa -L -f
%forgemeta

%global goname goimapnotify

%global common_description %{expand:
Execute scripts on IMAP mailbox changes (new/deleted/updated messages) using
IDLE, golang version.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.rst README.md

Name:    %{goname}
Release: %autorelease -b4
Summary: Execute scripts on IMAP mailbox changes (new/deleted/updated messages) using IDLE, golang version

License: GPL-3.0-only
URL:     %{forgeurl}
Source0: %{forgesource}
Source1: vendor-%{version}.tar.gz
Source2: bundle_go_deps_for_rpm.sh

BuildRequires: systemd-rpm-macros go-rpm-macros git-core
BuildRequires: pkgconfig(openssl)
%{?systemd_requires}

%description %{common_description}

%prep
%goprep -k
%setup -q -T -D -a 1
%autopatch -p1

%build
%gobuild    -o %{gobuilddir}/bin/%{goname} %{goipath}
%{_fixperms}  %{gobuilddir}

%install
%{__install} -m 0755 -vd %{buildroot}%{_bindir}
%{__install} -m 0755 -vp %{gobuilddir}/bin/%{goname} %{buildroot}%{_bindir}/
%{__install} -dm 0755 -v %{buildroot}/%{_userunitdir}/
%{__install} -Dm 0644 -v -t %{buildroot}/%{_userunitdir}/ %{goname}@.service

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc CHANGELOG.rst README.md
%{_bindir}/%{goname}
%{_userunitdir}/%{goname}@.service

%changelog
%autochangelog
