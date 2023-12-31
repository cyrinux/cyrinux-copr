# Generated by go2rpm 1.9.0
%bcond_without check

# https://gitlab.com/shackra/goimapnotify
%global goipath         gitlab.com/shackra/goimapnotify
%global forgeurl        https://gitlab.com/shackra/goimapnotify
Version:                2.3.9
%global tag             2.3.9

%gometa -f

%global goname goimapnotify

%global common_description %{expand:
Execute scripts on IMAP mailbox changes (new/deleted/updated messages) using
IDLE, golang version.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.rst README.md

Name:           %{goname}
Release:        3
Summary:        Execute scripts on IMAP mailbox changes (new/deleted/updated messages) using IDLE, golang version

License:        GPL-3.0-only
URL:            %{gourl}
Source0:        %{gosource}
Source1:        https://gitlab.com/shackra/%{goname}/-/raw/%{version}/%{goname}@.service

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
%gobuild -o %{gobuilddir}/bin/goimapnotify %{goipath}

%install
install -dm 0755 -v %{buildroot}/%{_userunitdir}/
install -Dm 0644 -v -t %{buildroot}/%{_userunitdir}/ %{goname}@.service

%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc CHANGELOG.rst README.md
%{_bindir}/*
%{_userunitdir}/%{goname}@.service

%gopkgfiles

%changelog
%autochangelog
