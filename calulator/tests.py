# from django.test import TestCase

# # Create your tests here.
# from django.test import TestCase
# from django.urls import reverse

# class CalculatorViewTests(TestCase):

#     def setUp(self):
#         self.url = reverse('calculator')  # Make sure your url name='calculator'

#     def test_get_request(self):
#         """Test GET request loads the calculator page"""
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'calculator.html')

#     def test_addition(self):
#         response = self.client.post(self.url, {'num1': 5, 'num2': 3, 'operation': 'add'})
#         self.assertContains(response, '8.0')

#     def test_subtraction(self):
#         response = self.client.post(self.url, {'num1': 10, 'num2': 4, 'operation': 'subtract'})
#         self.assertContains(response, '6.0')

#     def test_multiplication(self):
#         response = self.client.post(self.url, {'num1': 6, 'num2': 7, 'operation': 'multiply'})
#         self.assertContains(response, '42.0')

#     def test_division(self):
#         response = self.client.post(self.url, {'num1': 20, 'num2': 4, 'operation': 'divide'})
#         self.assertContains(response, '5.0')

#     def test_division_by_zero(self):
#         response = self.client.post(self.url, {'num1': 10, 'num2': 0, 'operation': 'divide'})
#         self.assertContains(response, 'Division by zero error')


from django.test import TestCase
from django.urls import reverse
import math

class CalculatorViewTests(TestCase):

    def setUp(self):
        self.url = reverse('calculator')  # Ensure your url pattern has name='calculator'

    # Basic operations
    def test_addition_operation(self):
        response = self.client.post(self.url, {'expression': '5+3'})
        self.assertContains(response, '8')

    def test_subtraction_operation(self):
        response = self.client.post(self.url, {'expression': '10-4'})
        self.assertContains(response, '6')

    def test_multiplication_operation(self):
        response = self.client.post(self.url, {'expression': '6*7'})
        self.assertContains(response, '42')

    def test_division_operation(self):
        response = self.client.post(self.url, {'expression': '20/4'})
        self.assertContains(response, '5')

    def test_division_by_zero_returns_error(self):
        response = self.client.post(self.url, {'expression': '10/0'})
        self.assertContains(response, 'Error')  # 'Division by zero error' is now handled as general Error

    # Invalid input
    def test_invalid_expression_returns_error(self):
        response = self.client.post(self.url, {'expression': 'abc'})
        self.assertContains(response, 'Error')

    # Advanced math functions
    def test_sqrt_operation(self):
        response = self.client.post(self.url, {'expression': 'sqrt(16)'})
        self.assertContains(response, '4.0')

    def test_pow_operation(self):
        response = self.client.post(self.url, {'expression': 'pow(2,3)'})
        self.assertContains(response, '8')

    def test_pi_constant(self):
        response = self.client.post(self.url, {'expression': 'pi'})
        self.assertContains(response, str(math.pi))

    def test_e_constant(self):
        response = self.client.post(self.url, {'expression': 'e'})
        self.assertContains(response, str(math.e))

    def test_trig_functions(self):
        response = self.client.post(self.url, {'expression': 'sin(pi/2)'})
        self.assertContains(response, '1.0')
        response = self.client.post(self.url, {'expression': 'cos(0)'})
        self.assertContains(response, '1.0')
        response = self.client.post(self.url, {'expression': 'tan(0)'})
        self.assertContains(response, '0.0')

    def test_log_function(self):
        response = self.client.post(self.url, {'expression': 'log(1)'})
        self.assertContains(response, '0.0')
