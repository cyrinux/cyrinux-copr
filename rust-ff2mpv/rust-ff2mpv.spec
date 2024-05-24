%global forgeurl https://github.com/ryze312/ff2mpv-rust
%global tag    1.1.5
%forgemeta

%global crate ff2mpv-rust

Name:           ff2mpv
Version:        1.1.5
Release:        %autorelease -b2
Summary:        Native messaging host for ff2mpv written in Rust
SourceLicense:  GPLv3
License:        GPLv3
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  cargo-rpm-macros >= 25

%global _description %{expand:
%{summary}.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        GPLv3

%description -n %{crate} %{_description}

%prep
%forgeautosetup -p1
%{__cargo} fetch --locked

%build
export RUSTUP_TOOLCHAIN=stable
export CARGO_TARGET_DIR=target
%{__cargo} build --frozen --release --all-features
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%{__install} -m 0755 -vd %{buildroot}%{_bindir}
%{__install} -Dm 0755 -t %{buildroot}%{_bindir}/ "target/release/%{crate}"
%{__mkdir} -p %{buildroot}%{_libdir}/mozilla/native-messaging-hosts/
cat > %{buildroot}%{_libdir}/mozilla/native-messaging-hosts/%{name}.json << EOF
{
  "name": "ff2mpv",
  "description": "ff2mpv's external manifest",
  "path": "%{_bindir}/ff2mpv-rust",
  "type": "stdio",
  "allowed_extensions": [
    "ff2mpv@yossarian.net"
  ]
}
EOF
# add support for chrome extension https://chrome.google.com/webstore/detail/ff2mpv/ephjcajbkgplkjmelpglennepbpmdpjg
# https://github.com/DanSM-5/ff2mpv/blob/master/ff2mpv.json
# ff2mpv-rust manifest | jq 'del(.allowed_extensions) | .allowed_origins |= ["chrome-extension://ephjcajbkgplkjmelpglennepbpmdpjg/"]' >manifest-chrome.json
%{__mkdir} -p %{buildroot}%{_sysconfdir}/chromium/native-messaging-hosts/
cat > %{buildroot}%{_sysconfdir}/chromium/native-messaging-hosts/%{name}.json << EOF
{
  "name": "ff2mpv",
  "description": "ff2mpv's external manifest",
  "path": "%{_bindir}/ff2mpv-rust",
  "type": "stdio",
  "allowed_origins": [
    "chrome-extension://ephjcajbkgplkjmelpglennepbpmdpjg/"
  ]
}
EOF

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/ff2mpv-rust
%{_libdir}/mozilla/native-messaging-hosts/%{name}.json
%{_sysconfdir}/chromium/native-messaging-hosts/%{name}.json

%changelog
%autochangelog
