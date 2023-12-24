%global forgeurl https://github.com/rofl0r/microsocks
%global tag    v1.0.3
%forgemeta

Name:           microsocks
Version:        1.0.3
Release:        %autorelease -b2
Summary:        Tiny, portable SOCKS5 server with very moderate resource usage

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires: gcc
Requires:      glibc

%description

%prep
%forgeautosetup -p1

%build
%make_build

%install
%{__install} -dm 0755 -v %{buildroot}%{_bindir}
%{__install} -Dm 0755 -v -t %{buildroot}%{_bindir}/ %{name}


%files
%{_bindir}/%{name}
%license COPYING
%doc README.md

%changelog
%autochangelog
