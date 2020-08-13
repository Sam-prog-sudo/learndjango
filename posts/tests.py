from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostTests(TestCase):

    def setUp(self):
        Post.objects.create(title='just a test', cover='salut.png')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.title}'
        self.assertEquals(expected_object_name, 'just a test')

    def test_post_list_view(self):
        response = self.client.get(reverse('posts'))
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'just a test')
        self.assertTemplateUsed(response, 'posts.html')
