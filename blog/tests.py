from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post

class BlogTest(TestCase):
    def setup(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@gmail.com',
            password = 'secret'
        )

        post =Post.object.create(
            title = 'Hey you',
            author = self.user,
            body = 'Do you love programming??',
        )

    def test_string_representation(self):
        post = Post(title = 'Hey you')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        post = Post.objects.get(id=1)
        self.assertEqual(f'{post.title}', 'Hey you')
        self.assertEqual(f'{post.author}', 'testuser')
        self.assertEqual(f'{post.body}', 'Do you love programming??')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Do you love programming??')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/1/')
        no_response = self.client.get('/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Hey you')
        self.assertTemplateUsed(response, 'detail.html')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_new'),{
            'title' : 'New title',
            'body' : 'New text',
            'author' : self.user,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')

    def test_post_create_view(self):
        response = self.client.post(reverse('detail', args='1'),{
            'title': 'Updated title',
            'body' : 'Updated text',
        })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.get(
            reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 200)

    
