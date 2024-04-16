%bcond_without check

%global __cargo_is_lib() 0

%global crate swayr

Name:           rust-swayr
%global tag     0.27.3
Version:        0.27.3%{?bumpver:^%{bumpver}.git%{shortcommit}}
Release:        %autorelease -b2
Summary:        A LRU window-switcher (and more) for the sway window manager

License:        GPLv3
URL:            https://sr.ht/~tsdh/swayr/
Source:         %{crates_source}
Source:         %{crate}-%{tag}-vendor.tar.xz
Recommends:     sway

BuildRequires:  cargo-rpm-macros >= 25

%global _description %{expand:
A LRU window-switcher (and more) for the sway window manager.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        GPLv3

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/swayr
%{_bindir}/swayrd
%{_userunitdir}/%{_name}.service


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
%{__install} -dm 0755 %{buildroot}%{_userunitdir}
cat > %{buildroot}%{_userunitdir}/%{_name}.service << EOF
[Unit]
Description=swayr daemon
PartOf=graphical-session.target
After=graphical-session.target

[Service]
ExecStart=%{_bindir}/%{_name}d
Restart=always
RestartSec=10s
StandardOutput=null

[Install]
WantedBy=graphical-session.target
EOF

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
