# Linux Commands



### Man-Pages

If you already know which command you want to use, but are not sure how exactly to use it, you can read its man-page (_man_ for _manual_). For instance, to know read more about the `cd` command, type 

```bash
man passwd
```

reveals this:

```bash
PASSWD(1)                 BSD General Commands Manual                PASSWD(1)

NAME
     passwd -- modify a user's password

SYNOPSIS
     passwd [-i infosystem [-l location]] [-u authname] [user]

DESCRIPTION
     The passwd utility changes the user's password.  If the user is not
     the super-user, passwd first prompts for the current password and will
     not continue unless the correct password is entered.
...
```
You can return to the command line by pressing `q` (for _quit_).
You can also [browse man-pages online](http://man7.org/linux/man-pages/dir_all_alphabetic.html).


### apropos Command

Let's say you want to copy a file but are unsure what the proper command is called. You can search in your local man-pages using the apropos command, for instance:

```bash
apropos copy
```

reveals

```bash
FcCacheCopySet(3)        - Returns a copy of the fontset from cache
FcCharSetCopy(3)         - Copy a charset
FcLangSetCopy(3)         - copy a langset object
FcMatrixCopy(3)          - Copy a matrix
FcPatternDuplicate(3)    - Copy a pattern
FcRangeCopy(3)           - Copy a range object
FcStrCopy(3)             - duplicate a string
FcStrCopyFilename(3)     - create a complete path from a filename
FcValueSave(3)           - Copy a value
tiffcp(1)                - copy (and possibly convert) a TIFF file
tiffcrop(1)              - select, copy, crop, convert, extract, and/or process one or more TIFF files
asr(8)                   - Apple Software Restore; copy volumes (e.g. from disk images)
copy(9), copyin(9), copyinstr(9), copyout(9), copystr(9) - kernel copy functions
copyops(n), transfer::copy(n) - Data transfer foundation
cp(1)                    - copy files
cpio(1)                  - copy files to and from archives
...
```

From there you can read that `cp` is probably the right command.



### Command Help

The man pages are quite extensive, and sometimes you want to have a shorter description. Then you can use the help text for the command, which is often available when you use the `--help` flag for the command:

```bash
cd --help
```




# cd

# rm

# echo

# info

# ls

# passwd

Changes the password



# touch

