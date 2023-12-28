# https://github.com/amacneil/dbmate
%global goipath         github.com/amacneil/dbmate
Version:                2.10.0

%global debug_package %{nil}

%gometa -f

%global goname dbmate


%global common_description %{expand:
:rocket: A lightweight, framework-agnostic database migration tool.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        :rocket: A lightweight, framework-agnostic database migration tool

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

BuildRequires: golang git sqlite-devel

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%global ldflags "-linkmode=external -s"

%build
env GOBIN="%{gobuilddir}/bin" go install -tags sqlite_omit_load_extension,sqlite_json -ldflags %{ldflags} %{goipath}/v2@v%{version}

%install
%{__install} -m 0755 -vd %{buildroot}%{_bindir}
%{__install} -m 0755 -vt %{buildroot}%{_bindir}/ %{gobuilddir}/bin/%{name}


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}


%changelog
%autochangelog
