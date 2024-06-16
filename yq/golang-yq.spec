%bcond_without check

%global forgeurl        https://github.com/mikefarah/yq
%global goipath         github.com/mikefarah/yq
Version:     4.44.2
%global tag v4.44.2

%gometa -L -f
%forgemeta

%global goname yq

%global common_description %{expand:
Yq is a portable command-line YAML, JSON, XML, CSV, TOML  and properties
processor.}

%global golicenses      LICENSE
%global godocs          README.md

Name:    %{goname}
Release: %autorelease -b5
Summary: Yq is a portable command-line YAML, JSON, XML, CSV, TOML  and properties processor

License: MIT
URL:     %{forgeurl}
Source0: %{forgesource}
Source1: vendor-%{tag}.tar.gz
Source2: bundle_go_deps_for_rpm.sh

BuildRequires: systemd-rpm-macros go-rpm-macros git-core
BuildRequires: pkgconfig(openssl)
%description %{common_description}

%prep
%goprep -k
%setup -q -T -D -a 1
%autopatch -p1

%build
%gobuild -o %{gobuilddir}/bin/%{goname} %{goipath}
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
%{_bindir}/%{name}

%changelog
%autochangelog
