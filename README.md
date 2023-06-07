# xaod_usage

 Book describing how to use the xAOD ATLAS ServiceX Backend.

 Under development - not at all polished!

This web-book website can be found here: [https://gordonwatts.github.io/xaod_usage/chapters/met.html](https://gordonwatts.github.io/xaod_usage).

## Updating The Book

```bash
jupyter-book build --all ./book
ghp-import -n -p -f ./book/_build/html
```

If you want to use this as a test of servicex and the `xAOD` backend, then first clean the build directory to remove all the cache:

```bash
jupyter-book clean --all ./book
```

And then follow the build instructions above.

## Development

### Testing New Type Packages

This package can be used to test/develop new typing packages. When you are doing that:

1. Create a new python environment that contains `poetry`
1. `pip install -e .` in the `xaod_usage` directory.
1. `pip uninstall func_adl_x...` - uninstall any type packages that were installed
1. `cd` into each directory that contains a type package you want to install and do a `pip install -e .`

Now you can regenerate the type packages at will and test them in the scripts.
