To get facts from files in `test/data/input` run `extract $files` (on UNIX run `./extract $files`) in **this** directory.

To extract facts from all files in `test/data/input` run `extract -a` (on UNIX -- `./extract -a`).

To normalize **and extract** facts from files run `extract -n $files` (`$files` could be `-a` or empty: `-a` will be used as default).

You can combine the options (`-an`, `-na`).

`tomitaparser` (or `tomita-$platfrom_name`) **have to be** in PATH (`/usr/bin`)
