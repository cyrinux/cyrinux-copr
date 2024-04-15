%global commit0 99baca7747e6d48801f91b58bc392b7df46dc56b
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 2
%global forgeurl https://git.sr.ht/~whynothugo/shotman
%global commit  %{commit0}
%forgemeta

%global _name shotman

Name:           %{_name}-git
URL:            %{forgeurl}
Version:        0.4.5%{?bumpver:^%{bumpver}.git%{shortcommit0}}
Release:        %autorelease -b1
Summary:        The uncompromising screenshot GUI for Wayland compositors
SourceLicense:  ISC
License:        ISC
Source:         %{forgesource}
BuildRequires:  systemd-rpm-macros
BuildRequires:  git-core
BuildRequires:  gcc
BuildRequires:  rust-xkbcommon0.4+wayland-devel
Provides:       %{_name}
Provides:       rust-%{_name}

%global _description %{expand:
The uncompromising screenshot GUI for Wayland compositors.}

%description %{_description}

%prep
%autosetup -n %{_name}-%{commit0}
export RUSTUP_TOOLCHAIN=stable
curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y

%build
export RUSTFLAGS='-Copt-level=3 -Cdebuginfo=1 -Ccodegen-units=1 -Clink-arg=-Wl,-z,relro -Clink-arg=-Wl,-z,now -Clink-arg=-specs=/usr/lib/rpm/redhat/redhat-package-notes'
$HOME/.cargo/bin/cargo build --release --package %{_name}

%install
%{__install} -dm 0755 %{buildroot}%{_bindir}
%{__install} -Dm755 target/release/%{_name} -t %{buildroot}%{_bindir}/%{_name}

%files
%license LICENCE
%doc README.md

%changelog
%autochangelog

