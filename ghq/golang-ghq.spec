%bcond_without check

%global forgeurl https://github.com/x-motemen/ghq
%global goipath         github.com/x-motemen/ghq
Version:                1.5.0
%global tag            v1.5.0


BuildRequires: git-core golang go-rpm-macros
Requires: git-core

%gometa -f -L
%forgemeta

%global goname ghq

%global common_description %{expand:
Remote repository management made easy.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.adoc

Name:    %{goname}
Release: %autorelease -b5
Summary: Remote repository management made easy

License: MIT
URL:     %{forgeurl}
Source0: %{forgesource}
Source1: vendor-%{tag}.tar.gz
Source2: bundle_go_deps_for_rpm.sh

%description %{common_description}

%prep
%goprep -k
%setup -q -T -D -a 1
%autopatch -p1

%build
%gobuild -o %{gobuilddir}/bin/ghq %{goipath}
%{_fixperms}  %{gobuilddir}

%install
%{__install} -m 0755 -vd                     %{buildroot}%{_bindir}
%{__install} -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc CHANGELOG.md README.adoc
%{_bindir}/%{goname}

%changelog
%autochangelog
