%global debug_package %{nil}

# https://github.com/hoyon/mpv-mpris
Version:                1.1

%global name mpv-mpris

%global common_description %{expand:
MPRIS plugin for mpv.}

%global licenses      LICENSE
%global docs          README.md

Name:           %{name}
Release:        %autorelease
Summary:        MPRIS plugin for mpv

BuildRequires: clang
BuildRequires: mpv-devel

License:        MIT
URL:        https://github.com/hoyon/mpv-mpris
Source:     %{url}/archive/refs/tags/%{version}.tar.gz

%description %{common_description}

%prep
%autosetup -n %{name}-%{version} -p1

%build
make

%install
make install-system DESTDIR=%{buildroot} PLUGINDIR=%{_libdir}/%{name}

%files
%{_libdir}/%{name}/mpris.so
/etc/mpv/scripts/mpris.so
%license LICENSE
%doc README.md

%changelog
%autochangelog
