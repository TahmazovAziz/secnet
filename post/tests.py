from django.test import TestCase
from post.models import Post
from users.models import Users

class TestPost(TestCase):
        
    def test_view(self):
        res = self.client.get('/post/')
        self.assertEqual(res.status_code,200)

    def test_uploud_file(self):
        users_inst = Users.objects.create(username='root')
        post_inst = Post.objects.create(id=1,title='test_titl', image='*.mp4',userid=users_inst)
        self.assertIsNotNone(post_inst)