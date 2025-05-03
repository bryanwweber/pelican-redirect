from pathlib import Path

import pytest

from pelican.contents import Page


def test_generators():
    """Literally the least possible test

    test that get_generators returns something"""
    from pelican.plugins.pelican_redirect import get_generators

    assert get_generators(None) is not None


@pytest.fixture(name="settings")
def get_settings():
    """Fixture to get the settings"""
    from pelican.settings import DEFAULT_CONFIG

    return DEFAULT_CONFIG.copy()


@pytest.fixture(name="generator")
def get_generator(settings, tmp_path: Path):
    """Fixture to get a generator instance"""
    from pelican.plugins.pelican_redirect import RedirectGenerator

    context = {}
    path = tmp_path / "input"
    theme = "no-op"
    output_path = tmp_path / "output"
    return RedirectGenerator(context, settings, path, theme, output_path)


@pytest.fixture(name="output_dir")
def get_output_dir(tmp_path: Path):
    """Fixture to get the output file"""
    return tmp_path / "output"


@pytest.fixture(name="writer")
def get_writer(settings, output_dir: Path):
    """Fixture to get a writer instance"""
    from pelican.writers import Writer

    settings["TEMPLATE_PAGES"] = {}
    return Writer(output_dir, settings)


@pytest.fixture(name="page")
def get_page(settings):
    page = Page("content", {}, settings, "source-path.html.j2")
    page.override_save_as = "dest-path.html"
    return page


def test_plugin_version(generator):
    """Test that the plugin version is not None"""
    assert isinstance(generator.version, str)


def test_plugin_version_meta(generator, writer, output_dir: Path):
    from pelican.plugins.pelican_redirect import Redirect

    generator.redirects = [Redirect(to="new-url", from_url="old-path.html")]
    generator.generate_output(writer)
    redirect_content = (output_dir / "old-path.html").read_text()
    assert "pelican-redirect-plugin-version" in redirect_content


def test_plugin_redirect_to_new(generator, writer, output_dir: Path):
    from pelican.plugins.pelican_redirect import Redirect

    generator.redirects = [
        Redirect(to="doesn't matter, ignored in this", from_url="old-path.html")
    ]
    generator.generate_output(writer)
    redirect_content = (output_dir / "old-path.html").read_text()
    assert 'content="0;url=/"' in redirect_content


def test_plugin_redirect_to_existing(generator, writer, output_dir: Path, page: Page):
    from pelican.plugins.pelican_redirect import Redirect

    generator.redirects = [Redirect(to=page, from_url="old-path.html")]
    generator.generate_output(writer)

    redirect_content = (output_dir / "old-path.html").read_text()
    assert f'content="0;url=/{page.save_as}"' in redirect_content
