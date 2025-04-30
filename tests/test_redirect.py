def test_generators():
    """Literally the least possible test

    test that get_generators returns something"""
    from pelican.plugins.pelican_redirect import get_generators

    assert get_generators(None) is not None
