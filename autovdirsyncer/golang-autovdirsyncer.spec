%bcond_without check

%global forgeurl        https://git.sr.ht/~whynothugo/autovdirsyncer
%global goname autovdirsyncer
%global goipath         git.sr.ht/~whynothugo/autovdirsyncer
%global tag v0.2.1
Version:     0.2.1

%gometa -f -L
%forgemeta

%global common_description %{expand:
Autovdirsyncer is a wrapper to daemonise vdirsyncer.
}

%global golicenses      LICENCE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Execute scripts on IMAP mailbox changes (new/deleted/updated messages) using IDLE, golang version

License: GPL-3.0-only
URL:     %{forgeurl}
Source0: %{forgesource}
Source1: vendor-%{tag}.tar.gz
Source2: bundle_go_deps_for_rpm.sh


BuildRequires: golang git-core go-rpm-macros systemd-rpm-macros systemd-devel
Requires: systemd
%{?systemd_requires}

%description %{common_description}

%prep
%goprep -k
%setup -n %{name}-%{tag} -q -T -D -a 1
%autopatch -p1

%build
%gobuild -o %{gobuilddir}/bin/%{goname} %{goipath}
%{_fixperms}  %{gobuilddir}

%install
%{__install} -dm 0755 -v %{buildroot}/%{_userunitdir}/
%{__install} -Dm 0644 -v -t %{buildroot}/%{_userunitdir}/ %{goname}.service
%{__install} -m 0755 -vd %{buildroot}%{_bindir}
%{__install} -m 0755 -vp %{gobuilddir}/bin/%{goname} %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENCE
%doc README.md
%{_bindir}/%{goname}
%{_userunitdir}/%{goname}.service

%changelog
%autochangelog
