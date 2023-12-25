[![Copr build status](https://copr.fedorainfracloud.org/coprs/cyrinux/misc/package/wldash/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/cyrinux/misc/package/wldash/)

This copr repo contains various packages.

Copr repository maintain by @cyrinux and @maximbaz https://copr.fedorainfracloud.org/coprs/cyrinux/.


# Help for me

```
$ sudo dnf install tito mock copr-cli go2rpm rust2rpm -y
$ alias mockbuild='\
        rpmlint *.spec &&
        spectool -g *.spec &&
        __mockf() {
                local SRPM=$( mock "$@" -v --resultdir . --buildsrpm --spec *.spec --sources . 2>&1 | awk "/ Wrote: /{ print gensub(\".*/([^/]+)$\",\"\\\1\",\"g\",\$3) }" )
                mock "$@" --resultdir . "${SRPM:?ERROR: Missing SRPM}"; }; __mockf'
```
