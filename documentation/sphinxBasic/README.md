# Sphinex
Document project

## Brief structure of folders and files
```text

Sphinx
├── _build/
│   └── html/
│      └── index.html
├── _ext/
├── _static/
├── _templates/
├── pages/
├── conf.py
├── index.rst
├── make.bat
├── Makefile
└── README.md

```

## Installation
- `pip install -U Sphinx`;

## Create basic configuration file
```sh
	sphinx-quickstart
	> Separate source and build directories (y/n) [n]: n
	> Project name: app
	> Author name(s): user_dev
	> Project release []: 1.0
	> Project language [en]: pt_BR
```

## Additional settings
- html[title,logo,favicon,theme]
- extensions
- css custom

Add on `conf.py`.
```py
	# html custom
	html_title = 'Documentation'
	html_logo = '_static/book.png'
	html_favicon = '_static/book.png'
	html_theme = 'sphinx_rtd_theme'
	# extensions
	extensions = [
		'sphinx.ext.autodoc',
	    'sphinx.ext.graphviz',
		'sphinx.ext.todo',
		'sphinx.ext.viewcode',
		"myst_parser",
	]
	# css custom
	def setup(app):
		app.add_css_file('css/custom.css')

```

## Generate documentation in HTML format
```sh
	sphinx-apidoc -o . ..
	make clean & make html
```

## Result
![result](./_static/img/preview_sphinx.png)

## References
- https://www.sphinx-doc.org/