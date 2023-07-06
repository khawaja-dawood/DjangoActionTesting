from django.test import TestCase
from blog.models import Post


class ModelTesting(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title='django',
            author='John',
            slug='django'
        )

    def test_post_model(self):
        d = self.post
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d), 'django')
