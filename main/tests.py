from django.test import TestCase

class MainTest(TestCase):
    def test_view(self):
        res = self.client.get('')
        self.assertEqual(res.status_code,200)