%bcond_without check

%global forgeurl https://github.com/mr-karan/doggo
%global goipath         github.com/mr-karan/doggo
Version:                0.6.1-dev
%global tag v0.6.1-dev

%gometa -f -L
%forgemeta

%global goname doggo

%global common_description %{expand:
:dog: Command-line DNS Client for Humans. Written in Golang.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease -b3
Summary:        :dog: Command-line DNS Client for Humans. Written in Golang

License: GPL-3.0-only
URL:     %{forgeurl}
Source0: %{forgesource}
Source1: vendor-%{tag}.tar.gz
Source2: bundle_go_deps_for_rpm.sh

BuildRequires: go-rpm-macros git-core golang
BuildRequires: pkgconfig(openssl)

%description %{common_description}

%prep
%goprep -k
%setup -q -T -D -a 1
%autopatch -p1

%build
%gobuild -o %{gobuilddir}/bin/%{name} %{goipath}/cmd/%{name}
%{_fixperms}  %{gobuilddir}

%install
%{__install} -m 0755 -vd %{buildroot}%{_bindir}
%{__install} -m 0755 -vt %{buildroot}%{_bindir}/ %{gobuilddir}/bin/%{name}

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
