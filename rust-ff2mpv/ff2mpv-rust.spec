# Generated by rust2rpm 25
%bcond_without check

# prevent library files from being installed
%global __cargo_is_lib() 0

%global crate ff2mpv-rust

Name:           ff2mpv
Version:        1.1.0
Release:        %autorelease
Summary:        Native messaging host for ff2mpv written in Rust

SourceLicense:  GPLv3
License:        GPLv3

URL:            https://github.com/ryze312/ff2mpv-rust
Source0:        https://github.com/ryze312/ff2mpv-rust/archive/refs/tags/%{version}.tar.gz
Source1:        ff2mpv-rust-%{version}-vendor.tar.xz

BuildRequires:  cargo-rpm-macros >= 25

%global _description %{expand:
%{summary}.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        GPLv3

%description -n %{crate} %{_description}

%prep
%autosetup -n %{crate}-%{version} -p1 -a1
%cargo_prep -v vendor

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%cargo_install
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

%if %{with check}
%check
%cargo_test
%endif

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
