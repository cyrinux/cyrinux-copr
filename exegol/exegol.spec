# Created by pyp2rpm-3.3.10
%global pypi_name exegol
%global pypi_version 4.3.1

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Python wrapper to use Exegol, a container based fully featured and community- driven hacking environment

License:        GNU (GPLv3)
URL:            https://github.com/ThePorgs/Exegol
Source0:        https://files.pythonhosted.org/packages/source/e/%{pypi_name}/Exegol-%{pypi_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-requests
BuildRequires:  (python3dist(argcomplete) >= 3.2.1 with python3dist(argcomplete) < 3.3)
BuildRequires:  (python3dist(docker) >= 7 with python3dist(docker) < 7.1)
BuildRequires:  (python3dist(gitpython) >= 3.1.40 with python3dist(gitpython) < 3.2)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  (python3dist(rich) >= 13.7 with python3dist(rich) < 13.8)
BuildRequires:  python3dist(setuptools)

%description
<div align"center"> <img alt"latest commit on master" width"600" src" <br><br>
<a target"_blank" rel"noopener noreferrer" href" title""><img src" alt"pip
package version"></a> <img alt"Python3.7" src" <img alt"latest commit on
master" src" <br><br> <img alt"latest commit on master" src"

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       (python3dist(argcomplete) >= 3.2.1 with python3dist(argcomplete) < 3.3)
Requires:       (python3dist(docker) >= 7 with python3dist(docker) < 7.1)
Requires:       (python3dist(gitpython) >= 3.1.40 with python3dist(gitpython) < 3.2)
Requires:       python3dist(pyyaml)
Requires:       python3dist(requests) >= 2.31
Requires:       (python3dist(rich) >= 13.7 with python3dist(rich) < 13.8)
Requires:       python3dist(setuptools)
Requires:       docker
%description -n python3-%{pypi_name}
<div align"center"> <img alt"latest commit on master" width"600" src" <br><br>
<a target"_blank" rel"noopener noreferrer" href" title""><img src" alt"pip
package version"></a> <img alt"Python3.7" src" <img alt"latest commit on
master" src" <br><br> <img alt"latest commit on master" src"


%prep
%autosetup -n Exegol-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md exegol-docker-build/sources/assets/exegol/skel/README.md exegol-docker-build/sources/assets/exegol/skel/bloodhound/README.md exegol-docker-build/sources/assets/exegol/skel/bloodhound/customqueries_merge/README.md exegol-docker-build/sources/assets/exegol/skel/bloodhound/customqueries_replacement/README.md exegol-docker-build/sources/dockerfiles/README.md
%{_bindir}/exegol
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Dec 25 2023 Cyril Levis <git@levis.name> - 4.3.1-1
- Initial package.
