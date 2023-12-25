# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/emersion/go-imap-idle
%global goipath         github.com/emersion/go-imap-idle
%global commit          db256843144576c70e551f0732f1d1d3b5bec67e

# REMOVE BEFORE SUBMITTING THIS FOR REVIEW
# ---
# New Fedora packages should use %%gometa -f, which makes the package
# ExclusiveArch to %%golang_arches_future and thus excludes the package from
# %%ix86. If the new package is needed as a dependency for another package,
# please consider removing that package from %%ix86 in the same way, instead of
# building more go packages for i686. If your package is not a leaf package,
# you'll need to coordinate the removal of the package's dependents first.
# ---
# REMOVE BEFORE SUBMITTING THIS FOR REVIEW
%gometa -f


%global common_description %{expand:
IDLE extension for go-imap.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        IDLE extension for go-imap

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

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Mon Dec 25 2023 Cyril Levis <git@levis.name> 0-0.1
- new package built with tito

%autochangelog
