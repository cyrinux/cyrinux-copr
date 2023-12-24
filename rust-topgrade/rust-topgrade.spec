%global debug_package %{nil}

%global forgeurl https://github.com/topgrade-rs/topgrade
%global tag    v13.0.0
%forgemeta

Name:           topgrade
Version:        13.0.0
Release:        %autorelease -b7
Summary:        Topgrade - Invoke the upgrade procedure of multiple package managers
Group:          System Environment/Shells
License:        GPLv3
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires: cargo-rpm-macros >= 24

%description
Keeping your system up to date mostly involves invoking more than a single package manager. This usually results in big shell one-liners saved in your shell history. Topgrade tries to solve this problem by detecting which tools you use and run their appropriate package managers.

%prep
%forgeautosetup -p1
%{__cargo} fetch --locked

%build
export RUSTUP_TOOLCHAIN=stable
export CARGO_TARGET_DIR=target
%{__cargo} build --frozen --release --all-features

%install
%{__install} -Dm0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog


