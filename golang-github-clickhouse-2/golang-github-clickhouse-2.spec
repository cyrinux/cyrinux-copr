# Generated by go2rpm 1.9.0
%bcond_without check

# https://github.com/ClickHouse/clickhouse-go
%global goipath         github.com/ClickHouse/clickhouse-go/v2
Version:                2.17.1

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
Golang driver for ClickHouse.}

%global golicenses      LICENSE
%global godocs          examples CONTRIBUTING.md CHANGELOG.md README.md\\\
                        TYPES.md v1_v2_CHANGES.md\\\
                        contributors/contributors.go

Name:           %{goname}
Release:        %autorelease
Summary:        Golang driver for ClickHouse

License:        Apache-2.0
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
for cmd in benchmark/v2/read benchmark/v2/write-async benchmark/v2/write-native-struct benchmark/v2/write-compress-buffer-limit lib/column/codegen benchmark/v2/write-async-std benchmark/v2/write benchmark/v2/read-native benchmark/v2/write-native-columnar benchmark/v1/read benchmark/v2/write-native benchmark/v1/write; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

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
%doc examples CONTRIBUTING.md CHANGELOG.md README.md TYPES.md v1_v2_CHANGES.md
%doc contributors/contributors.go
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog