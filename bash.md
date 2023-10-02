## View history

`$ history > history.txt`
`$ history`

## Grep
`grep --help`

* -r, --recursive
* -w, --word-regexp	force PATTERN to match only whole words
* -n, --line-number	print line number with output lines
* -i, --ignore-case	ignore case distinctions
* -L, --files-without-match	print only names of FILEs containing no match

### Find * that contains ${pattern}
`grep -riwn . -e 'pattern'

### Find * that does NOT contain ${pattern}
`grep -riL . -e 'pattern'

### Filters and modifiers
* `--color=always`
* `--include=*.jmx`
* `|sed 's/^/|- '`

## Gzip
* Decompress gzip file: `gzip -d <file>`

## Cat
* Include non printing character: `cat -v`

## View Rhel version
+ `cat /etc/redhat-release`