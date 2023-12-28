# https://github.com/mr-karan/doggo
%global goipath         github.com/mr-karan/doggo
Version:                0.5.7

%global debug_package %{nil}

%gometa -f

%global goname doggo

%global common_description %{expand:
:dog: Command-line DNS Client for Humans. Written in Golang.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        :dog: Command-line DNS Client for Humans. Written in Golang

License:        GPL-3.0-only
URL:            %{gourl}
Source:         %{gosource}

BuildRequires: git

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%build
env GOBIN="%{gobuilddir}/bin" go install -ldflags="-linkmode=external -s"  %{goipath}/cmd/%{name}@v%{version}

%install
%{__install} -m 0755 -vd %{buildroot}%{_bindir}
%{__install} -m 0755 -vt %{buildroot}%{_bindir}/ %{gobuilddir}/bin/%{name}


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}


%changelog
%autochangelog
