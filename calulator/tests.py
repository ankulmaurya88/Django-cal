from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse

class CalculatorViewTests(TestCase):

    def setUp(self):
        self.url = reverse('calculator')  # Make sure your url name='calculator'

    def test_get_request(self):
        """Test GET request loads the calculator page"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'calculator.html')

    def test_addition(self):
        response = self.client.post(self.url, {'num1': 5, 'num2': 3, 'operation': 'add'})
        self.assertContains(response, '8.0')

    def test_subtraction(self):
        response = self.client.post(self.url, {'num1': 10, 'num2': 4, 'operation': 'subtract'})
        self.assertContains(response, '6.0')

    def test_multiplication(self):
        response = self.client.post(self.url, {'num1': 6, 'num2': 7, 'operation': 'multiply'})
        self.assertContains(response, '42.0')

    def test_division(self):
        response = self.client.post(self.url, {'num1': 20, 'num2': 4, 'operation': 'divide'})
        self.assertContains(response, '5.0')

    def test_division_by_zero(self):
        response = self.client.post(self.url, {'num1': 10, 'num2': 0, 'operation': 'divide'})
        self.assertContains(response, 'Division by zero error')
