%bcond_without check

%global forgeurl        https://github.com/rs/curlie
%global goipath         github.com/rs/curlie
Version:      1.7.2
%global tag  v1.7.2

%gometa -f -L
%forgemeta

%global goname curlie

%global common_description %{expand:
The power of curl, the ease of use of httpie.}

%global golicenses      LICENSE
%global godocs          README.md

Name:    %{goname}
Release: %autorelease -b2
Summary: The power of curl, the ease of use of httpie.
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
%gobuild    -o %{gobuilddir}/bin/%{goname} %{goipath}
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
