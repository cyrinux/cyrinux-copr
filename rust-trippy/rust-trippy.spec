%bcond_without check

%global forgeurl https://github.com/fujiapple852/trippy
%global tag    0.11.0-rc.2
%forgemeta

%global _binname trip

Name:           trippy
Version:        0.11.0-rc.2
Release:        %autorelease -b1
Summary:        A network diagnostic tool
License:        Apache License 2.0
URL:            https://trippy.cli.rs
Source:         %{forgesource}
Requires:       clang libcap

BuildRequires: cargo-rpm-macros >= 24

%description
A network diagnostic tool.

%prep
%forgeautosetup -p1
%{__cargo} fetch --locked
%{__mkdir} completions

%build
export RUSTUP_TOOLCHAIN=stable
export CARGO_TARGET_DIR=target
%{__cargo} build --frozen --release
target/release/%{_binname} --generate fish > completions/%{name}.fish
target/release/%{_binname} --generate bash > completions/%{name}.bash
target/release/%{_binname} --generate zsh > completions/_%{name}

%install
%{__install} -Dm0755 target/release/%{_binname} %{buildroot}%{_bindir}/%{_binname}
%{__chmod} +s %{buildroot}%{_bindir}/%{_binname}
%{__install} -m 0755 -vd %{buildroot}{%{fish_completions_dir},%{zsh_completions_dir},%{bash_completions_dir}}
%{__install} -Dm 0644 -v -t %{buildroot}%{fish_completions_dir}/%{name}.fish completions/%{name}.fish
%{__install} -Dm 0644 -v -t %{buildroot}%{bash_completions_dir}/%{name} completions/%{name}.bash
%{__install} -Dm 0644 -v -t %{buildroot}%{zsh_completions_dir}/_%{name} completions/_%{name}

%if %{with check}
%check
%{__cargo} check --frozen
%endif

%post
setcap CAP_NET_RAW+p %{_bindir}/%{_binname}

%files
%defattr(-,root,root,-)
%{_bindir}/%{_binname}
%{zsh_completions_dir}
%{bash_completions_dir}
%{fish_completions_dir}
%doc README.md
%license LICENSE

%changelog
%autochangelog
