 ```bash
 $ git log --pretty=oneline
 $ git tag -a v0.1 <commitid>
 ```

### Reset
 ```bash
git reset --hard
git clean -d -x -f
```

### Diff

```bash
$ git difftool
$ git difftool 2c1373:src/test/java/..java 04a2a4:src/test/java/test/...java
```

### Merge dry run

```bash
$ git merge origin/INTEGRATION --no-commit --no-ff
$ git merge --abort
```

### Reset a particular file to HEAD

```bash
git reset -- FILENAME
```

### Remove from staging
- If na add then wala sa .gitignore
````bash
$ git rm -r --cached .idea
````

### E-view ang remote

````bash
$ git remote -v
````
### To know what will be deleted

`git clean -n`
`git clean --dry-run`

### To delete unwanted files
`git clean -fd`

## Diff

`git diff` - Uncommited changes. Local vs Index
`git diff --cached` - Index vs HEAD
`git diff HEAD`
`git diff --name-only`

## Config
- `git config --global --list`
- `git config --list`
