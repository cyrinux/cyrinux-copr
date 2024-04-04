%bcond_without check

%global forgeurl        https://github.com/xbglowx/vault-kv-search
%global goipath         github.com/xbglowx/vault-kv-search
Version:     0.2.1
%global tag v0.2.1

%gometa -L -f
%forgemeta

%global goname vault-kv-search

%global common_description %{expand:
Recursively search Hashicorp Vault for a substring.}

%global golicenses      LICENSE
%global godocs          README.md

Name:    %{goname}
Release: %autorelease
Summary: Recursively search Hashicorp Vault for a substring

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
%{__mkdir} completions

%build
%gobuild -o %{gobuilddir}/bin/%{goname} %{goipath}
%{gobuilddir}/bin/%{goname} completion fish > completions/%{goname}.fish
%{gobuilddir}/bin/%{goname} completion bash > completions/%{goname}.bash
%{gobuilddir}/bin/%{goname} completion zsh > completions/_%{goname}
%{_fixperms}  %{gobuilddir}

%install
%{__install} -m 0755 -vd                     %{buildroot}%{_bindir}
%{__install} -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%{__install} -m 0755 -vd $RPM_BUILD_ROOT%{fish_completions_dir}
%{__cp} completions/%{name}.fish $RPM_BUILD_ROOT%{fish_completions_dir}/%{name}.fish
%{__install} -m 0755 -vd $RPM_BUILD_ROOT%{bash_completions_dir}
%{__cp} completions/%{name}.bash $RPM_BUILD_ROOT%{bash_completions_dir}/%{name}
%{__install} -m 0755 -vd $RPM_BUILD_ROOT%{zsh_completions_dir}
%{__cp} completions/_%{name} $RPM_BUILD_ROOT%{zsh_completions_dir}/_%{name}

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%{_bindir}/%{name}
%{zsh_completions_dir}
%{bash_completions_dir}
%{fish_completions_dir}

%changelog
%autochangelog
