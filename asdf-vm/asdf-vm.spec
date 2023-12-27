Name:           asdf-vm
Version:        0.13.1
Release:        %autorelease
Summary: "Extendable version manager with support for Ruby, Node.js, Elixir, Erlang & more"

License:        MIT
URL:            https://asdf-vm.com
Source0:        https://github.com/%{name}/asdf/archive/refs/tags/v%{version}.tar.gz

Requires: curl git

%description

%prep
%autosetup -n asdf-%{version}


%install
%global dst $RPM_BUILD_ROOT/opt/%{name}
%{__rm} -r -f $RPM_BUILD_ROOT
%{__install} -m 0755 -vd "%{dst}"
%{__cp} -rv "bin" "%{dst}"
%{__cp} -rv "lib" "%{dst}"
%{__cp} -v   asdf.elv    "%{dst}"
%{__cp} -v   asdf.fish   "%{dst}"
%{__cp} -v   asdf.nu     "%{dst}"
%{__cp} -v   asdf.sh     "%{dst}"
%{__cp} -v   defaults    "%{dst}"
%{__cp} -v   help.txt    "%{dst}"
%{__cp} -v   version.txt "%{dst}"
%{__install} -m 0755 -vd $RPM_BUILD_ROOT%{fish_completions_dir}
%{__cp} completions/asdf.fish $RPM_BUILD_ROOT%{fish_completions_dir}/asdf.fish
%{__install} -m 0755 -vd $RPM_BUILD_ROOT%{bash_completions_dir}
%{__cp} completions/asdf.bash $RPM_BUILD_ROOT%{bash_completions_dir}/asdf
%{__install} -m 0755 -vd $RPM_BUILD_ROOT%{zsh_completions_dir}
%{__cp} completions/_asdf $RPM_BUILD_ROOT%{zsh_completions_dir}/_asdf

%files
%defattr(-,root,root,-)
/opt/%{name}
%{zsh_completions_dir}
%{bash_completions_dir}
%{fish_completions_dir}

%license LICENSE

%changelog
%autochangelog
