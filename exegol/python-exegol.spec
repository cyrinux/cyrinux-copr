%global pypi_name Exegol
%global pypi_version 4.3.1

%global forgeurl  https://github.com/ShutdownRepo/Exegol
%global tag 4.3.1
%global forgeurl1  https://github.com/ShutdownRepo/Exegol-images
%global branch1 main
%global forgeurl2  https://github.com/ShutdownRepo/Exegol-resources
%global branch2 main
%forgemeta -a

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Python wrapper to use Exegol, a container based fully featured and community- driven hacking environment

License:        GNU (GPLv3)
URL:            %{forgeurl0}
Source0:        %{forgesource0}
Source1:        %{forgesource1}
Source2:        %{forgesource2}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(argcomplete)
BuildRequires:  python3dist(docker)
BuildRequires:  python3dist(gitpython)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(rich)
BuildRequires:  python3dist(setuptools)

%description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-argcomplete
Requires:       python3-docker
Requires:       python3-gitpython
Requires:       python3-pyyaml
Requires:       python3-requests
Requires:       python3-rich
Requires:       python3-setuptools

Provides:       exegol
Recommends:     docker-ce

%description -n python3-%{pypi_name}

%prep
%autosetup -n Exegol-%{pypi_version} -a1 -a2
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
%{__rm} -rf %{buildroot}/usr/exegol-docker-build
%{__rm} -rf %{buildroot}/usr/exegol-imgsync


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/exegol
%{python3_sitelib}/exegol
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
%autochangelog
