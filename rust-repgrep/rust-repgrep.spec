%bcond_without check

%global __cargo_is_lib() 0

%global crate repgrep
%global _binname rgr

Name:           rust-repgrep
Version:        0.15.0
%global tag     0.15.0
Release:        %autorelease -b3
Summary:        An interactive replacer for ripgrep that makes it easy to find and replace across files on the command line

License:        Unlicense OR MIT OR Apache-2.0
URL:            https://github.com/acheronfail/repgrep
Source0:        %{crates_source}
Source1:        %{crate}-%{tag}-vendor.tar.xz

Requires:       ripgrep >= 14
BuildRequires:  cargo-rpm-macros >= 25
BuildRequires:  asciidoctor
BuildRequires:  ripgrep >= 14

%global _description %{expand:
An interactive replacer for ripgrep that makes it easy to find and replace across files on the command line.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        Unlicense OR MIT OR Apache-2.0

%description -n %{crate} %{_description}

%files       -n %{crate}
%{_bindir}/rgr
%{zsh_completions_dir}
%{bash_completions_dir}
%{fish_completions_dir}
%{_usr}/share/man/man1
%license LICENSE-APACHE
%license LICENSE-MIT
%license LICENSE-UNLICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md

%prep
%autosetup -n %{crate}-%{version} -p1 -a1
%cargo_prep -v vendor
%{__mkdir} completions

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}
%{_bindir}/asciidoctor --doctype manpage --backend manpage --destination-dir completions doc/rgr.1.template
%{_bindir}/rg --generate=complete-bash | sed 's/ rg/ rgr/g; s/_rg/_rgr/g' > completions/%{_binname}.bash
%{_bindir}/rg --generate=complete-zsh | sed 's/ rg/ rgr/g; s/_rg/_rgr/g' > completions/_%{_binname}
%{_bindir}/rg --generate=complete-fish | sed 's/ rg/ rgr/g; s/_rg/_rgr/g' > completions/%{_binname}.fish

%install
%cargo_install
%{__install} -m 0755 -vd %{buildroot}%{_usr}/share/man/man1
%{__cp} completions/%{_binname}.1 %{buildroot}%{_usr}/share/man/man1/%{_binname}.1
%{__install} -m 0755 -vd %{buildroot}{%{fish_completions_dir},%{zsh_completions_dir},%{bash_completions_dir}}
%{__install} -Dm 0644 -v -t %{buildroot}%{fish_completions_dir}/ completions/%{_binname}.fish
%{__install} -Dm 0644 -v -t %{buildroot}%{zsh_completions_dir}/ completions/_%{_binname}
%{__install} -Dm 0644 -v -t %{buildroot}%{bash_completions_dir}/ completions/%{_binname}.bash


%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
