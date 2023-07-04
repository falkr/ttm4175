# Writing Documents




# Chunks

# Markdown Chunks

The Markdown chunks of the document should follow [Pandoc's Markdown syntax](https://pandoc.org/MANUAL.html#pandocs-markdown).

## Sections

Sections on different levels are written with preceeding `#`, `##`, `###`

```markdown
# Section Level 1
```

```markdown
## Section Level 2
```

```markdown
### Section Level 3
```

## Text Markup

**bold** text __bold__ text.
*emphasized* text, _emphasized text_




## Lists




# YAML Elements

YAML elements start and stop with a delimiter `---`.


## Referenced Chunks

Use a chunk as a reference to other chunks defined in other files.

```yaml
---
ref: file.md
---
```

## Videos


---
type: youtube
video: wupToqz1e2g
caption: "The Pale Blue Dot."
start: 80
---

```yaml
---
type: youtube
video: wupToqz1e2g
position: aside
caption: "The Pale Blue Dot."
start: 80
---
```

## Tables

Tables can be included directly as HTML, or via the following YAML section that refers to a table stored in a file.
The table in the file must use the [mediawiki syntax for tables](https://www.mediawiki.org/wiki/Help:Tables), with an example shown below.
The optional class attribute places a `<div>` element around the table for styling with the given class.

The optional format attribute allows to select the markup within the cells. Examples are html, markdown, wikimedia, latex.

```yaml
---
type: table
file: tables/table.mw
class: rubric
caption: "Table with a caption."
---
```

```mediawiki
{|
|Orange
|Apple
|-
|Bread
|Pie
|-
|Butter
|Ice cream 
|}
```



## Figures

## Buttons

## Hints

Hints are boxes with information that is only visible when the reader clicks on the header.
The top of the hint is specified with a YAML section. 
The content of the hint is provided as post-YAML section, directly following the YAML header.
It ends after two consecutive empty lines.

---
type: hint
title: Hint about Something
---
Within the content you can have lists:

* 10.0.0.0/8
* 172.16.0.0/12
* 192.168.0.0/16

And you can continue.

**Remember:** Hints should be helpful. 


```yaml
---
type: hint
title: Hint about Something
---
Within the content you can have lists:

* 10.0.0.0/8
* 172.16.0.0/12
* 192.168.0.0/16

An you can coninue.

**Remember:** Hints should be helpful. 
```


# HTML Blocks


# Code Blocks

Supermark  uses Pandoc's functions to highlight code. Place the code between the following delimiters:


<div>
<pre>
```bash
pandoc --list-highlight-languages
```
</pre>
</div>


`abc`, `asn1`, `asp`, `ats`, `awk`, `actionscript`, `ada`, `agda`, `alertindent`, `apache`, `bash`, `bibtex`, `boo`, `c`, `cs`, `cpp`, `cmake`, `css`, `changelog`, `clojure`, `coffee`, `coldfusion`, `commonlisp`, `curry`, `d`, `dtd`, `diff`, `djangotemplate`, `dockerfile`, `doxygen`, `doxygenlua`, `eiffel`, `elixir`, `email`, `erlang`, `fsharp`, `fortran`, `gcc`, `glsl`, `gnuassembler`, `m4`, `go`, `html`, `hamlet`, `haskell`, `haxe`, `ini`, `isocpp`, `idris`, `fasm`, `nasm`, `json`, `jsp`, `java`, `javascript`, `javadoc`, `julia`, `kotlin`, `llvm`, `latex`, `lex`, `lilypond`, `literatecurry`, `literatehaskell`, `lua`, `mips`, `makefile`, `markdown`, `mathematica`, `matlab`, `maxima`, `mediawiki`, `metafont`, `modelines`, `modula2`, `modula3`, `monobasic`, `ocaml`, `objectivec`, `objectivecpp`, `octave`, `opencl`, `php`, `povray`, `pascal`, `perl`, `pike`, `postscript`, `powershell`, `prolog`, `pure`, `purebasic`, `python`, `r`, `relaxng`, `relaxngcompact`, `roff`, `ruby`, `rhtml`, `rust`, `sgml`, `sql`, `sqlmysql`, `sqlpostgresql`, `scala`, `scheme`, `tcl`, `tcsh`, `texinfo`, `mandoc`, `vhdl`, `verilog`, `xml`, `xul`, `yaml`, `yacc`, `zsh`, `dot`, `noweb`, `rest`, `sci`, `sed`, `xorg`, `xslt`,

For an updated list, type:

```bash
pandoc --list-highlight-languages
```

# File Encoding

  - UTF-8


# Special

### Learning Goals

```markdown
:goals:
- Learning Goal 1
- Learning Goal 2


```

End the goal environment with two empty lines.


:goals:
- Learning Goal 1
- Learning Goal 2


## Tips

:tip: A tip is shown in a highlighted box.


```
:tip: A tip is shown in a highlighted box.
```


## Warnings

:warning: Use warnings to prevent harm or damage. Draw attention.


```
:warning: Use warnings to prevent harm or damage. Draw attention.
```



# Image Placeholders


# Constants


You can use constants in your documents that get replaced with values. 

```markdown
Year: {{:year:}}
```

