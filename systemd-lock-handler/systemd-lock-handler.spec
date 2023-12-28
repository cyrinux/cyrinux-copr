%global debug_package %{nil}

Name:           systemd-lock-handler
Version:        2.4.2
Release:        %autorelease
Summary:        Logind lock event to systemd target translation.

License:       ISC
URL:           https://git.sr.ht/~whynothugo/%{name}
Source0:       https://git.sr.ht/~whynothugo/%{name}/archive/v%{version}.tar.gz

BuildRequires: golang git systemd-devel
Requires: systemd

%description


%prep
%autosetup -n %{name}-v%{version}

%build
go build -ldflags="-linkmode=external -s"

%install
%make_install


%files
%{_userunitdir}/*
/usr/lib/%{name}
%license LICENCE
%doc README.md


%changelog
%autochangelog
