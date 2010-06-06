from wad.tests import *

class TestGiftsController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='gifts', action='index'))
        # Test response...
