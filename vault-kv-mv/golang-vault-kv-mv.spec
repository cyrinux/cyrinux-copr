%bcond_without check

%global forgeurl        https://github.com/xbglowx/vault-kv-mv
%global goipath         github.com/xbglowx/vault-kv-mv
Version:     0.05
%global tag v0.05

%gometa -L -f
%forgemeta

%global goname vault-kv-mv

%global common_description %{expand:
Easily move Hashicorp Vault keys to different paths.}

%global golicenses      LICENSE
%global godocs          README.md

Name:    %{goname}
Release: %autorelease
Summary: Easily move Hashicorp Vault keys to different paths

License: Mozilla Public License Version 2.0
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
