%global forgeurl https://github.com/biomejs/biome
%global tag    v1.6.1
%forgemeta

%global crate biome

Name:           rust-biome
Version:        1.6.1
Release:        %autorelease
Summary:        Display file system space usage using graphs and colors

License:        MIT
URL:            %{forgeurl}
Source:         %{forgeurl}/archive/refs/tags/cli/%{tag}.tar.gz
BuildRequires:  cargo-rpm-macros >= 25

%global _description %{expand:
A toolchain for web projects, aimed to provide functionalities to maintain them. Biome offers formatter and linter, usable via CLI and LSP.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        MIT

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE-MIT
%license LICENSE-APACHE
%license ROME_LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/biome

%prep
%autosetup -n %{crate}-cli-%{tag} -p1
%{__cargo} fetch --locked

%build
export RUSTUP_TOOLCHAIN=stable
export CARGO_TARGET_DIR=target
if [[ "$(uname -m)" == "aarch64" ]]; then
  export JEMALLOC_SYS_WITH_LG_PAGE=16
fi

%{__cargo} build --frozen --release
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%{__install} -m 0755 -vd %{buildroot}%{_bindir}
%{__install} -Dm 0755 -t %{buildroot}%{_bindir}/ "target/release/%{crate}"

%changelog
%autochangelog
