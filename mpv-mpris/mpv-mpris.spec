%global debug_package %{nil}
%global forgeurl https://github.com/hoyon/mpv-mpris

%global tag 1.1

%forgemeta

%global name mpv-mpris

%global common_description %{expand:
MPRIS plugin for mpv.}

%global licenses      LICENSE
%global docs          README.md

Name:           %{name}
Version:        1.1
Release:        %autorelease -b1
Summary:        MPRIS plugin for mpv

BuildRequires: clang
BuildRequires: pkgconfig(mpv)

License:    MIT
URL:        %{forgeurl}
Source:     %{forgesource}

%description %{common_description}

%prep
%autosetup -n %{name}-%{version} -p1

%build
%make_build

%install
%{__make} install-system DESTDIR=%{buildroot} PLUGINDIR=%{_libdir}/%{name}

%files
%{_libdir}/%{name}/mpris.so
%{_sysconfdir}/mpv/scripts/mpris.so
%license LICENSE
%doc README.md

%changelog
%autochangelog
