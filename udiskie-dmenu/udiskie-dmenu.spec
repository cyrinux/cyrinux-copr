%global debug_package %{nil}

%global forgeurl https://github.com/fogine/udiskie-dmenu
%global tag 0.6.0


%forgemeta

%global common_description %{expand:
manage removable devices via dmenu (or rofi).}

%global licenses      LICENSE
%global docs          README.md

Name:           udiskie-dmenu
Version:        0.6.0
Release:        %autorelease -b1
Summary:        Manage removable devices via dmenu (or rofi)

Requires: nodejs udiskie libnotify dmenu

License:    MIT
URL:        %{forgeurl}
Source:     %{forgesource}

%description %{common_description}

%prep
%autosetup -n %{name}-%{version} -p1

%build

%install
%{__install} -dm 0755 -v %{buildroot}%{_bindir}
%{__install} -Dm 0755 -v -t %{buildroot}%{_bindir}/ %{name}

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%changelog
%autochangelog
