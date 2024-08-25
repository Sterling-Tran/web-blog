from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Tech", slug="tech")

    def test_category_str(self):
        self.assertEqual(str(self.category), "Tech")

    def test_category_slug_unique(self):
        category2 = Category(name="Science", slug="tech")  # Trying to use existing slug
        with self.assertRaises(Exception):
            category2.save()


class TagModelTest(TestCase):

    def setUp(self):
        self.tag = Tag.objects.create(name="Python", slug="python")

    def test_tag_str(self):
        self.assertEqual(str(self.tag), "Python")

    def test_tag_slug_unique(self):
        tag2 = Tag(name="Django", slug="python")  # Trying to use existing slug
        with self.assertRaises(Exception):
            tag2.save()


class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.category = Category.objects.create(name="Tech", slug="tech")
        self.tag = Tag.objects.create(name="Python", slug="python")
        self.post = Post.objects.create(
            title="Django Testing",
            slug="django-testing",
            content="This is a test post content.",
            author=self.user,
            category=self.category
        )
        self.post.tags.add(self.tag)

    def test_post_str(self):
        self.assertEqual(str(self.post), "Django Testing")

    def test_absolute_url(self):
        self.assertEqual(self.post.absolute_url(), '/blog/django-testing')

    def test_post_likes(self):
        self.post.likes.add(self.user)
        self.assertIn(self.user, self.post.likes.all())

    def test_post_tags(self):
        self.assertIn(self.tag, self.post.tags.all())


class CommentModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.category = Category.objects.create(name="Tech", slug="tech")
        self.post = Post.objects.create(
            title="Django Testing",
            slug="django-testing",
            content="This is a test post content.",
            author=self.user,
            category=self.category
        )
        self.comment = Comment.objects.create(
            post=self.post,
            user=self.user,
            content="This is a test comment."
        )

    def test_comment_str(self):
        self.assertEqual(str(self.comment), f'Comment by {self.user} on {self.post}')

    def test_comment_default_active(self):
        self.assertTrue(self.comment.active)


class SubscriptionModelTest(TestCase):

    def setUp(self):
        self.subscription = Subscription.objects.create(email="test@example.com")

    def test_subscription_str(self):
        self.assertEqual(str(self.subscription), "test@example.com")

    def test_subscription_unique_email(self):
        subscription2 = Subscription(email="test@example.com")
        with self.assertRaises(Exception):
            subscription2.save()


class SavePostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.category = Category.objects.create(name="Tech", slug="tech")
        self.post = Post.objects.create(
            title="Django Testing",
            slug="django-testing",
            content="This is a test post content.",
            author=self.user,
            category=self.category
        )
        self.save_post = SavePost.objects.create(post=self.post, user=self.user)

    def test_save_post_str(self):
        self.assertEqual(str(self.save_post), f'{self.user} saved {self.post}')
