Pelican Redirect: A Plugin for Pelican
====================================================

[![build](https://github.com/bryanwweber/pelican-redirect/actions/workflows/main.yml/badge.svg)](https://github.com/bryanwweber/pelican-redirect/actions/workflows/main.yml)
[![PyPI Version](https://img.shields.io/pypi/v/pelican-redirect)](https://pypi.org/project/pelican-redirect/)
![Python Versions](https://img.shields.io/pypi/pyversions/pelican-redirect)
![License](https://img.shields.io/pypi/l/pelican-redirect?color=blue)

Redirect pages using meta http-equiv tags

Installation
------------

This plugin can be installed via:

```shell
python -m pip install pelican-redirect
```

Usage
-----

Once this plugin is installed, you can add a key to the frontmatter of the file called `original_url`. The plugin will generate an HTML page at that location that redirects to the new location of the post/page. Example:

```markdown
Title: A sample title
original_url: blog-posts/2021/07/21/a-sample-title.html

Content here
```

Assuming this file is now going to be served from `blog-posts/a-simple-title.html`, a file will be written to `blog-posts/2021/07/21/a-sample-title.html` that redirects to the new URL.s

Contributing
------------

Contributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues][].

To start contributing to this plugin, review the [Contributing to Pelican][] documentation, beginning with the **Contributing Code** section.

[existing issues]: https://github.com/bryanwweber/pelican-redirect/issues
[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html

License
-------

This project is licensed under the BSD-3-Clause license.
