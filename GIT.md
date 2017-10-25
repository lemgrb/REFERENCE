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
