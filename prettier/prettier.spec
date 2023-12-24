%global forgeurl https://github.com/prettier/prettier
%global tag 3.1.1
%forgemeta

%global debug_package %{nil}

%global name prettier

%global common_description %{expand:
Prettier is an opinionated code formatter.}

%global licenses      LICENSE
%global docs          README.md

Name:    %{name}
Version: 3.1.1
Release: %autorelease -b1
Summary: Prettier is an opinionated code formatter.
BuildRequires: nodejs-packaging yarnpkg nodejs-npm
Requires: nodejs
License:    MIT
URL:        %{forgeurl}
Source:     %{forgesource}
%description %{common_description}

%prep
%autosetup -n %{name}-%{version} -p1
yarn --frozen-lockfile

%build
yarn build

%install
%{__install} -dm 0755 -v %{buildroot}%{_bindir}
%{__install} -dm 0755 -v %{buildroot}%{nodejs_sitelib}
%{__ln_s} -v ../..%{nodejs_sitelib}/bin/%{name}.cjs %{buildroot}%{_bindir}/%{name}
%{__cp} -av dist/* %{buildroot}%{nodejs_sitelib}/

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/*
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%changelog
%autochangelog
