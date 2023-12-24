%global forgeurl        https://github.com/tomasklaen/uosc
%global goipath         github.com/tomasklaen/uosc
Version:                5.1.1
%global tag             5.1.1

%global gomodulesmode GO111MODULE=on

%gometa -f -L
%forgemeta

%global goname ziggy

%global _mpv %{_sysconfdir}/mpv

%global common_description %{expand:
Feature-rich minimalist proximity-based UI for MPV player.}

%global golicenses      LICENSE.LGPL
%global godocs          README.md

Name:           uosc
License:        LGPL
Release:        %autorelease -b6
Summary:        Feature-rich minimalist proximity-based UI for MPV player.
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        %{url}/releases/download/%{version}/%{name}.zip

BuildRequires: golang git-core go-rpm-macros unzip
BuildRequires: pkgconfig(sqlite)

%description %{common_description}

%prep
%goprep -k
%setup -q -T -D -a 1
%autopatch -p1

%build
%gobuild -o %{gobuilddir}/bin/%{goname}-linux ./src/%{goname}
%{_fixperms}  %{gobuilddir}

%install
%{__install} -m 0755 -vd %{buildroot}%{_mpv}
%{__install} -m 0755 -vd %{buildroot}%{_mpv}/script-opts
%{__install} -m 0644 -vt %{buildroot}%{_mpv}/script-opts/ ./src/uosc.conf
%{__unzip} %{SOURCE1} -d %{buildroot}%{_mpv}
%{__rm} -v %{buildroot}%{_mpv}/scripts/uosc/bin/ziggy-*
%{__install} -m 0755 -vt %{buildroot}%{_mpv}/scripts/uosc/bin/ %{gobuilddir}/bin/%{goname}-linux


%files
%defattr(-,root,root,-)
%license LICENSE.LGPL
%doc README.md
%config %{_mpv}/script-opts/uosc.conf
%{_mpv}/scripts
%{_mpv}/fonts


%changelog
%autochangelog
