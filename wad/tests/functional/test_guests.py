from wad.tests import *

class TestGuestsController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='guests', action='index'))
        # Test response...
