# Setting up PATH
Installing from pip with `--user` puts d2lmf in a subdirectory of your home
directory. It's probably not in your `PATH`, so invoking d2lmf may be a little
annoying by default. Fortunately, that can be fixed by changing your `PATH`.

Unfortunately, how you go about changing your `PATH` depends on what operating
system you're running and how you have configured it.

# Ubuntu
The most recent Ubuntu releases come with this set up already, so you might
not have to do anything. Try running `d2lmf extract --help` to check. If it
worked, you can close these instructions right now. If the command was not
found, don't worry—we'll fix that.

If you have a `~/.bash_profile` or `~/.bash_login`, add the command below to
the end of it. If you do not have either, then add the command to `~/.profile`.

```bash
export PATH="$HOME/.local/bin:$PATH"
```

This will take effect on your next login. Until then, you'll have to run that
command in each new shell you open.

# OSX
If you have a `~/.bash_profile` or `~/.bash_login`, add the command below to
the end of it. If you do not have either, then add the command to `~/.profile`.

```bash
export PATH="$PATH:$HOME/Library/Python/2.7/bin"
```

This will take effect on your next login. Until then, you'll have to run that
command in each new shell you open.

# Windows
My experience with the PATH on Windows has been inconsistent. If you chose the
option to add Python to your `PATH` in the Python installer, you might already
be able to invoke d2lmf directly. If not, I would recommend just invoking d2lmf
as a python module, like `python -m d2lmf extract --help`.
