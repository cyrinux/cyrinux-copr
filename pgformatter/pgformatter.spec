
%global debug_package %{nil}
%global forgeurl        https://github.com/darold/pgFormatter
%global name pgFormatter
%global tag   v5.5
%forgemeta

%global common_description %{expand:
A PostgreSQL SQL syntax beautifier that can work as a console program or as a CGI.}

%global licenses      LICENSE
%global docs          README

Name:           %{name}
Release:        %autorelease -b5
Summary:        A PostgreSQL SQL syntax beautifier that can work as a console program or as a CGI.
Version:        5.5
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
Requires: perl

License:    MIT
URL:        %{forgeurl}
Source:     %{forgesource}

%description %{common_description}

%prep
%forgeautosetup -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{__make} pure_install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p"
%{_fixperms} $RPM_BUILD_ROOT/*
find $RPM_BUILD_ROOT -type f -name .packlist -delete

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man*/*
%license LICENSE
%doc README

%changelog
%autochangelog
