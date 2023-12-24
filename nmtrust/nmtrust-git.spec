%global debug_package %{nil}

%global commit0 464a5f05cb2da85e008884ca7fe08a8e51b55043
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 2

#FIXME: should be name nmtrust-git?
Name:           nmtrust
Version:        1.1.2%{?bumpver:^%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        A simple framework for determining network trust with NetworkManager
License:        NOLICENSE
BuildArch:      noarch
URL:            https://github.com/pigmonkey/nmtrust
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

Requires: NetworkManager

%description

%prep
%autosetup -n %{name}-%{commit0} -p1

%build

%install
%{__install} -m 0755 -vd %{buildroot}%{_sysconfdir}/%{name}
touch  %{buildroot}%{_sysconfdir}/%{name}/excluded_networks
touch  %{buildroot}%{_sysconfdir}/%{name}/trusted_units
touch  %{buildroot}%{_sysconfdir}/%{name}/trusted_networks
%{__install} -m 0755 -vd %{buildroot}%{_bindir}
%{__install} -m 0755 -vp %{name} %{buildroot}%{_bindir}/
%{__install} -m 0755 -vp ttoggle %{buildroot}%{_bindir}/
%{__install} -m 0755 -vd                     %{buildroot}%{_sysconfdir}/NetworkManager/dispatcher.d/
%{__install} -m 0755 -vp dispatcher/10trust %{buildroot}/%{_sysconfdir}/NetworkManager/dispatcher.d/

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_bindir}/ttoggle
%{_sysconfdir}/NetworkManager/dispatcher.d/10trust
%config %{_sysconfdir}/%{name}/*
%doc README.md

%post
echo "To finish the setup, check usage: https://github.com/pigmonkey/nmtrust/tree/master#usage-1"

%changelog
%autochangelog
