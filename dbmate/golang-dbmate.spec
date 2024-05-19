%global forgeurl https://github.com/amacneil/dbmate
%global goipath         github.com/amacneil/dbmate/v2
Version:                2.16.0
%global tag            v2.16.0

%gometa -f -L
%forgemeta

%global gomodulesmode GO111MODULE=on

%global goname dbmate

%global common_description %{expand:
:rocket: A lightweight, framework-agnostic database migration tool.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease -b1
Summary:        :rocket: A lightweight, framework-agnostic database migration tool

License: MIT
URL:     %{forgeurl}
Source0: %{forgesource}
Source1: vendor-%{tag}.tar.gz
Source2: bundle_go_deps_for_rpm.sh

BuildRequires: golang gcc git-core go-rpm-macros
BuildRequires: pkgconfig(sqlite)

%description %{common_description}

%prep
%goprep -k
%setup -q -T -D -a 1
%autopatch -p1

%build
%gobuild -o %{gobuilddir}/bin/%{goname} %{goipath}
%{_fixperms}  %{gobuilddir}

%install
%{__install} -m 0755 -vd %{buildroot}%{_bindir}
%{__install} -m 0755 -vt %{buildroot}%{_bindir}/ %{gobuilddir}/bin/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
