# Usage


## Default Directory Structure

:tree:
- course/
    - pages/
        - index.md
        - hello.md
    - templates/
        - page.html
    - assets/
        - ...
    - figures/
        - ...
    - index.html
    - hello.html

## Default Command

Move into the main folder of your project, and invoke the following command:

```
supermark
````

Supermark will look for *.md files in the `pages` folder and transform each of them into a html file placed at the toplevel.


## Options

- `--all`, `-a` --- re-generate *all* files, not only the ones changed. Use this option for example when the template changed.
- `--verbose`, `-v` --- tell more about what the program does.
- `--draft`, `-d` --- also print draft parts of the documents.
- `--input`, `-i` --- input directory containing the *.md files.
- `--output`, `-o` --- output directory.
- `--template`, `-t` --- template file for the transformation.