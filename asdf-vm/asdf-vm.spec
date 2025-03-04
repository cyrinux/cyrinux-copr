%global forgeurl https://github.com/asdf-vm/asdf
%global tag    v0.16.5
%forgemeta

Name:           asdf-vm
Version:        0.16.5
Release:        %autorelease -b4
Summary: Extendable version manager with support for Ruby, Node.js, Elixir, Erlang & more
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

Requires:       curl git-core

%description

%prep
%forgeautosetup -p1


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
