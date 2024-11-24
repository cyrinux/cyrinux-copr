%global forgeurl https://github.com/magic-wormhole/magic-wormhole.rs
%global _reponame magic-wormhole.rs
%global debug_package %{nil}

Version:    1.7.4
%global tag 1.7.4
%forgemeta

Name:   wormhole-rs
Release:        %autorelease
Summary:        Get things from one computer to another, safely
License:        EUPL-1.2
URL:            %{forgeurl}
Source:         %{forgesource}
BuildRequires: cargo-rpm-macros >= 24
Requires: libxcb

%global _description %{expand:
Get things from one computer to another, safely.}

%description %{_description}

%prep
%autosetup -n %{_reponame}-%{version} -p1
%{__cargo} fetch --locked

%build
export RUSTUP_TOOLCHAIN=stable
export CARGO_TARGET_DIR=target
%{__cargo} build --frozen --release --all-features

%install
%{__install} -m 0755 -vd %{buildroot}%{_bindir}
%{__install} -Dm 0755 -t %{buildroot}%{_bindir}/ "target/release/%{name}"
%{__install} -m 0755 -vd %{buildroot}{%{fish_completions_dir},%{zsh_completions_dir},%{bash_completions_dir}}
target/release/%{name} completion bash > "%{buildroot}%{bash_completions_dir}/%{name}"
target/release/%{name} completion zsh >"%{buildroot}%{zsh_completions_dir}/_%{name}"
target/release/%{name} completion fish > "%{buildroot}%{fish_completions_dir}/%{name}.fish"

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{bash_completions_dir}/*
%{zsh_completions_dir}/*
%{fish_completions_dir}/*

%changelog
%autochangelog
