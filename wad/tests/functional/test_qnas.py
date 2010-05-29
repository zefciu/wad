from wad.tests import *

class TestQnasController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='qnas', action='index'))
        # Test response...
