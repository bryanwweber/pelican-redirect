# Pelican Redirect: A Plugin for Pelican

[![build](https://github.com/bryanwweber/pelican-redirect/actions/workflows/main.yml/badge.svg)](https://github.com/bryanwweber/pelican-redirect/actions/workflows/main.yml)
[![PyPI Version](https://img.shields.io/pypi/v/pelican-redirect)](https://pypi.org/project/pelican-redirect/)
![Python Versions](https://img.shields.io/pypi/pyversions/pelican-redirect)
![License](https://img.shields.io/pypi/l/pelican-redirect?color=blue)

Redirect pages using meta http-equiv tags

## Installation

This plugin can be installed via:

```shell
python -m pip install pelican-redirect
```

## Usage

Once this plugin is installed, you can add a key to the frontmatter of the file called `original_url`. The plugin will generate an HTML page at that location that redirects to the new location of the post/page. Example:

```markdown
Title: A sample title
original_url: blog-posts/2021/07/21/a-sample-title.html

Content here
```

Assuming this file is now going to be served from `blog-posts/a-simple-title.html`, a file will be written to `blog-posts/2021/07/21/a-sample-title.html` that redirects to the new URL.

If `original_url` does not have a file extension, or the file extension is something other than `.htm` or `.html`, then `original_url` is assumed to be a directory and `index.html` is appended to the URL.

## Bulk Usage

To perform a page-wide redirect, you can use the `CONTENT_REDIRECT_CONFIGURATION` setting, which allows you to configure an original URL using page metadata. The structure of this configuration key looks like so:

```python
CONTENT_REDIRECT_CONFIGURATION = [
    {
        "ARTICLE_URL": "old/layout/{slug}.html",
        "PAGE_URL": "old/pages/{slug}.html",
    }
]
```

For any entry in that list, if there is no key for the content type (for example, one configuration may only have `ARTICLE_URL`, another might only have `PAGE_URL`), the redirect will only be generated for the keys that are specified and the others will be skipped.

## Contributing

Contributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues][].

To start contributing to this plugin, review the [Contributing to Pelican][] documentation, beginning with the **Contributing Code** section.

[existing issues]: https://github.com/bryanwweber/pelican-redirect/issues
[contributing to pelican]: https://docs.getpelican.com/en/latest/contribute.html

## License

This project is licensed under the BSD-3-Clause license.
