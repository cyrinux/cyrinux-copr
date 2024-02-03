%bcond_without check

%global forgeurl        https://github.com/guumaster/hostctl
%global goipath         github.com/guumaster/hostctl
Version:      1.1.4
%global tag  v1.1.4

%gometa -f -L
%forgemeta

%global goname hostctl

%global common_description %{expand:
Your dev tool to manage /etc/hosts like a pro!}

%global golicenses      LICENSE
%global godocs          README.md

Name:    %{goname}
Release: %autorelease
Summary: Your dev tool to manage /etc/hosts like a pro!
License: MIT
URL:     %{forgeurl}
Source0: %{forgesource}
Source1: vendor-%{tag}.tar.gz
Source2: bundle_go_deps_for_rpm.sh

BuildRequires: systemd-rpm-macros go-rpm-macros  git-core golang
BuildRequires: pkgconfig(openssl)

%description %{common_description}

%prep
%goprep -k
%setup -q -T -D -a 1
%autopatch -p1

%build
%gobuild    -o %{gobuilddir}/bin/%{goname} %{goipath}/cmd/hostctl
%{_fixperms}  %{gobuilddir}

%install
%{__install} -m 0755 -vd %{buildroot}%{_bindir}
%{__install} -m 0755 -vp %{gobuilddir}/bin/%{goname} %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{goname}

%changelog
%autochangelog
