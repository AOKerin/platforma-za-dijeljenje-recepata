from django.test import TestCase
from .models import Category, Recipe, Tip
from django.contrib.auth.models import User
from django.urls import reverse


class ModelTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Deserti")
        self.user = User.objects.create_user(username="testuser", password="test123")

    def test_category_str(self):
        self.assertEqual(str(self.category), "Deserti")

    def test_recipe_creation(self):
        recipe = Recipe.objects.create(
            title="Palačinke",
            description="Opis recepta",
            category=self.category,
            author=self.user
        )
        self.assertEqual(str(recipe), "Palačinke")

    def test_tip_creation(self):
        recipe = Recipe.objects.create(
            title="Palačinke",
            description="Opis recepta",
            ingredients="Brašno, mlijeko, jaja",
            category=self.category,
            author=self.user
        )
        tip = Tip.objects.create(
            recipe=recipe,
            content="Tijesto ostavite 15 minuta da odstoji."
        )
        self.assertIn("Tip for", str(tip))


class ViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='12345')

    def test_recipe_list_view(self):
        response = self.client.get(reverse('recipe-list'))
        self.assertEqual(response.status_code, 200)

    def test_tip_list_view(self):
        response = self.client.get(reverse('tip-list'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_create_requires_login(self):
        response = self.client.get(reverse('recipe-create'))
        self.assertEqual(response.status_code, 302)  # redirect to login