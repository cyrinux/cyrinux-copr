# Generated by go2rpm 1.9.0
%bcond_without check

# https://github.com/x-motemen/ghq
%global goipath         github.com/x-motemen/ghq
Version:                1.4.4

BuildRequires: git
Requires: git

%gometa -f

%global goname ghq

%global common_description %{expand:
Remote repository management made easy.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.adoc

Name:           %{goname}
Release:        %autorelease
Summary:        Remote repository management made easy

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/ghq %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc CHANGELOG.md README.adoc
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Dec 26 2023 Cyril Levis <git@levis.name> 1.4.4-1
- new package built with tito

* Tue Dec 26 2023 Cyril Levis <git@levis.name> 1.4.3-1
- new package built with tito

%autochangelog
