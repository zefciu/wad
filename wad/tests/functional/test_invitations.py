from wad.tests import *

class TestInvitationsController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='invitations', action='index'))
        # Test response...
