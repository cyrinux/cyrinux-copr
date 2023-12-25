%global debug_package %{nil}

%global goipath         github.com/scylladb/go-set
Version:                1.0.2

%gometa -f


%global common_description %{expand:
Type-safe, zero-allocation sets for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Type-safe, zero-allocation sets for Go

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%gopkgfiles

%changelog
* Mon Dec 25 2023 Cyril Levis <git@levis.name> 1.0.2-1
- new package built with tito

%autochangelog
