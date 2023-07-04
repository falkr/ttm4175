



---
type: nav
prev: ["All extensions", "index.html"]
---





# Documentation

# Tables

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



