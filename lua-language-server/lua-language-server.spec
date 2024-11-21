%global debug_package %{nil}

Name:    lua-language-server
Version: 3.13.2
Release: 1%{?dist}
Summary: A language server that offers Lua language support
License: MIT
URL:     https://github.com/LuaLS/lua-language-server
Source0: https://github.com/LuaLS/lua-language-server/releases/download/%{version}/lua-language-server-%{version}-submodules.zip
Source1: wrapper

BuildRequires: git
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: libstdc++-devel
BuildRequires: libstdc++-static

%description
A language server that offers Lua language support

%prep
%setup -q -c

%build
cd 3rd/luamake
./compile/install.sh
cd ../..
./3rd/luamake/luamake

%global optdir /opt/%{name}

%install
%{__install} -D -m 755 bin/lua-language-server %{buildroot}%{optdir}/bin/lua-language-server
%{__install} -D -m 644 bin/main.lua %{buildroot}%{optdir}/bin/main.lua
%{__install} -D -m 644 main.lua %{buildroot}%{optdir}/main.lua
%{__install} -D -m 664 debugger.lua %{buildroot}%{optdir}/debugger.lua
%{__install} -D -m 664 changelog.md %{buildroot}%{optdir}/changelog.md
cp -r locale meta script %{buildroot}%{optdir}
%{__install} -D -m 755 %{SOURCE1} %{buildroot}%{_bindir}/lua-language-server

%files
%license LICENSE
%doc README.md

%{optdir}
%{_bindir}/lua-language-server

%changelog
%autochangelog
