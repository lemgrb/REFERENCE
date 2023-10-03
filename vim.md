Add in ~.vimrc

```vim
:set tabstop=4
:set shiftwidth=4
:set expandtab
:set clipboard+=unnamed
:set number
```

Find and replace

- `:%s/foo/bar/gc` Find foo (all lines) and replace after confirmation

Go to line

- `22G` Go to line 22

Find starting at current line

- `:,$s/foo/bar/fc`

Block select then indent:

1. V
2. jj
3. <

Add `\C` for Case insensitive text seach:

```bash
/someText\C
```

Show non-printing characters: `:set list` unshow `:set nolist`
