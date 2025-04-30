from pathlib import Path

import pytest


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


@pytest.fixture(name="output_file")
def get_output_file(tmp_path: Path):
    """Fixture to get the output file"""
    return tmp_path / "output_file.html"


@pytest.fixture(name="writer")
def get_writer(settings, output_file: Path):
    """Fixture to get a writer instance"""
    from pelican.writers import Writer

    settings["TEMPLATE_PAGES"] = {}
    return Writer(output_file, settings)


def test_plugin_version(generator):
    """Test that the plugin version is not None"""
    assert isinstance(generator.version, str)


def test_plugin_version_meta(generator, writer, output_file: Path):
    generator.generate_output(writer)
    assert output_file.read_text() == "foo: bar"
