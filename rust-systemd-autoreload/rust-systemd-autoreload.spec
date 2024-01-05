%global commit0 ab03f073add417f9a5e63fe7d6545e4c85a0daed
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1
%global forgeurl https://git.sr.ht/~whynothugo/systemd-autoreload
%global commit  %{commit0}
%forgemeta

%global _name systemd-autoreload

Name:           %{_name}-git
URL:            %{forgeurl}
Version:        0.1.0%{?bumpver:^%{bumpver}.git%{shortcommit0}}
Release:        %autorelease -b1
Summary:        Systemd autoreload
SourceLicense:  ISC
License:        ISC
Source:         %{forgesource}
BuildRequires:  systemd-rpm-macros
BuildRequires:  git-core
BuildRequires:  gcc
Requires:       systemd-libs
Provides:       %{_name}
Provides:       rust-%{_name}

%global _description %{expand:
A tiny rust app that automatically reloads systemd --user unit files when you edit them.}

%description %{_description}

%prep
%autosetup -n %{_name}-%{commit0}
export RUSTUP_TOOLCHAIN=stable
curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y

%build
export RUSTFLAGS='-Copt-level=3 -Cdebuginfo=1 -Ccodegen-units=1 -Clink-arg=-Wl,-z,relro -Clink-arg=-Wl,-z,now -Clink-arg=-specs=/usr/lib/rpm/redhat/redhat-package-notes'
$HOME/.cargo/bin/cargo build --release --package %{_name}

%install
%{__install} -dm 0755 %{buildroot}%{_systemd_util_dir}
%{__install} -Dm755 target/release/%{_name} -t %{buildroot}%{_systemd_util_dir}/%{_name}
%{__install} -dm 0755 %{buildroot}%{_userunitdir}
cat > %{buildroot}%{_userunitdir}/%{_name}.service << EOF
[Unit]
Description=Automatically reload systemd --user unit files

[Service]
ExecStart=%{_systemd_util_dir}/%{_name}
Type=notify
Slice=background.slice

[Install]
WantedBy=default.target
EOF

%files
%license LICENCE
%doc README.md
%{_systemd_util_dir}/%{_name}
%{_userunitdir}/%{_name}.service

%changelog
%autochangelog

