%undefine _missing_build_ids_terminate_build
%global debug_package %{nil}

Name:           browserpass-native
Version:        3.1.0
Release:        2%{?dist}
Summary:        Native application for the browserpass browser extension
License:        ISC
URL:            https://github.com/browserpass/browserpass-native
Source:         https://github.com/browserpass/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  golang
BuildRequires:  git
ExcludeArch:    ppc64

Recommends:     pass

%description
This is a host application for browserpass browser extension providing it
access to your password store. The communication is handled through Native
Messaging API.

%prep
%setup -qa0

%build
%make_build browserpass

%check
make test

%install
make configure
%make_install

rm -rf %{buildroot}/usr/share/{doc,licenses}

%files
%license LICENSE
%doc README.md
%{_bindir}/browserpass
%{_prefix}/lib/browserpass

%changelog
* Tue Dec 26 2023 Cyril Levis <git@levis.name> 3.1.0-2
- Automatic commit of package [browserpass-native] release [3.1.0-1].
  (git@levis.name)

%autochangelog
