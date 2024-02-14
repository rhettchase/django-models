from django.test import TestCase
from django.urls import reverse
from .models import Snack
from django.contrib.auth.models import User


class SnacksTests(TestCase):
    def setUp(self):
        # Create a User instance to use as the purchaser
        self.user = User.objects.create_user(username='testuser', password='12345')
        # Now use the created User instance for the purchaser field
        self.snack = Snack.objects.create(name="Test Snack", purchaser=self.user, description="Test Description")
        
    def test_list_page_status_code(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_list_page_template(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "base.html")
        
    def test_detail_page_status_code(self):
        url = reverse("snack_detail", kwargs={'pk': self.snack.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_detail_page_template(self):
        url = reverse("snack_detail", kwargs={'pk': self.snack.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_detail.html")
        self.assertTemplateUsed(response, "base.html")
