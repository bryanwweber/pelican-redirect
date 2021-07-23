# from .pelican_redirect import *  # NOQA
from pelican import signals
from pelican.generators import CachingGenerator


class RedirectGenerator(CachingGenerator):
    def generate_context(self):
        pass

    def generate_output(self):
        pass


def get_generators(pelican_object):
    # define a new generator here if you need to
    return RedirectGenerator


def register():
    signals.get_generators.connect(get_generators)
