import logging

from pelican import signals
from pelican.generators import CachingGenerator

logger = logging.getLogger(__name__)


TEMPLATE = """\
<!DOCTYPE html>
<html>

<head>
    <link rel="canonical" href="/{{ page.save_as }}" />
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <meta http-equiv="refresh" content="0;url=/{{ page.save_as }}" />
</head>

<body>
<p>This content has moved. If you are not redirected, please click here:</p>
<p><a href="/{{ page.save_as }}">{{ page.save_as }}</a></p>
</body>

</html>
"""


class RedirectGenerator(CachingGenerator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.redirects = []
        signals.article_generator_finalized.connect(self.redirect_articles)
        signals.page_generator_finalized.connect(self.redirect_pages)
        self._templates["redirect"] = self.env.from_string(TEMPLATE)

    def redirect_articles(self, article_generator):
        for article in article_generator.articles:
            if article.metadata.get("original_url"):
                self.redirects.append(article)

    def redirect_pages(self, page_generator):
        for page in page_generator.pages:
            if page.metadata.get("original_url"):
                self.redirects.append(page)

    def generate_output(self, writer):
        for page in self.redirects:
            logger.debug(
                "\nSource Path: %s\nRedirect File: %s",
                page.source_path,
                page.metadata["original_url"],
            )
            writer.write_file(
                page.metadata["original_url"],
                self.get_template("redirect"),
                self.context,
                self.settings["RELATIVE_URLS"],
                paginated=False,
                page=page,
            )


def get_generators(pelican_object):
    return RedirectGenerator


def register():
    signals.get_generators.connect(get_generators)
