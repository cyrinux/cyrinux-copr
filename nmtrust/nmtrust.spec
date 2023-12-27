Name:           nmtrust
%global         branch  master
Version:        %{branch}
Release:        %autorelease
Summary:        A simple framework for determining network trust with NetworkManager

License:        NOLICENSE
URL:            https://github.com/pigmonkey/nmtrust
Source0:        https://github.com/pigmonkey/nmtrust/archive/refs/heads/master.zip

Requires: NetworkManager

%description

%prep
%autosetup -n %{name}-%{branch}


%install
%{__install} -m 0755 -vd                     %{buildroot}%{_sysconfdir}/%{name}
%{__install} -m 0755 -vd                     %{buildroot}%{_bindir}
%{__install} -m 0755 -vp %{name} %{buildroot}%{_bindir}/
%{__install} -m 0755 -vp ttoggle %{buildroot}%{_bindir}/
%{__install} -m 0755 -vd                     %{buildroot}%{_sysconfdir}/NetworkManager/dispatcher.d/
%{__install} -m 0755 -vp dispatcher/10trust %{buildroot}/%{_sysconfdir}/NetworkManager/dispatcher.d/


%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_bindir}/ttoggle
%{_sysconfdir}/NetworkManager/dispatcher.d/10trust
%dir %{_sysconfdir}/%{name}
%doc README.md


%post
echo "To finish the setup, check usage: https://github.com/pigmonkey/nmtrust/tree/master#usage-1"


%changelog
%autochangelog
