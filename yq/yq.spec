# https://github.com/mikefarah/yq
%global goipath         github.com/mikefarah/yq/v4
Version:                4.40.5

%global debug_package %{nil}

%gometa -f

%global goname yq

%global common_description %{expand:
Yq is a portable command-line YAML, JSON, XML, CSV, TOML  and properties
processor.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Yq is a portable command-line YAML, JSON, XML, CSV, TOML  and properties processor

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

BuildRequires: golang git


%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%global ldflags "-linkmode=external -s"

%build
env GOBIN="%{gobuilddir}/bin" go install -ldflags %{ldflags} %{goipath}@v%{version}

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog
