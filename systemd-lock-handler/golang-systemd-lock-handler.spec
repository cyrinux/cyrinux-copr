%bcond_without check

%global forgeurl https://git.sr.ht/~whynothugo/systemd-lock-handler
%global goipath git.sr.ht/~whynothugo/systemd-lock-handler
%global goname systemd-lock-handler
%global tag v2.4.2
Version:     2.4.2
%global golicenses      LICENSE
%global godocs          README.md
%gometa -f -L
%forgemeta

Name:       %{goname}
Release:    %autorelease -b1
Summary:    Logind lock event to systemd target translation.
License:    ISC
URL:        %{forgeurl}
Source0:    %{forgesource}
Source1:    vendor-%{tag}.tar.gz
Source2:    bundle_go_deps_for_rpm.sh
BuildRequires: systemd-rpm-macros go-rpm-macros golang git-core
Requires:   systemd
%{?systemd_requires}

%description

%prep
%goprep -k
%setup -n %{goname}-%{tag} -q -T -D -a 1
%autopatch -p1

%build
%gobuild   -o %{gobuilddir}/bin/%{goname} %{goipath}
%{_fixperms}  %{gobuilddir}

%install
%{__install} -Dm755 %{gobuilddir}/bin/%{goname} %{buildroot}/usr/lib/%{goname}
%{__install} -Dm644 %{goname}.service %{buildroot}%{_userunitdir}/%{goname}.service
%{__install} -Dm644 lock.target %{buildroot}%{_userunitdir}/lock.target
%{__install} -Dm644 unlock.target %{buildroot}%{_userunitdir}/unlock.target
%{__install} -Dm644 sleep.target %{buildroot}%{_userunitdir}/sleep.target

%if %{with check}
%check
%gocheck
%endif

%post
%systemd_user_post %{goname}.socket

%preun
%systemd_user_preun %{goname}.socket

%files
%{_userunitdir}/*
/usr/lib/%{name}
%license LICENCE
%doc README.md

%changelog
%autochangelog
