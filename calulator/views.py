# from django.shortcuts import render, redirect   
# from django.views import View

# # Create your views here.


# class CalculatorView(View):
#     def get(self, request):
#         return render(request, 'calculator.html')       
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['operations'] = ['add', 'subtract', 'multiply', 'divide']
#         return context
    
#     def post(self, request):
#         # Handle the form submission
#         num1 = float(request.POST.get('num1', 0))
#         num2 = float(request.POST.get('num2', 0))
#         operation = request.POST.get('operation', 'add')

#         if operation == 'add':
#             result = num1 + num2
#         elif operation == 'subtract':
#             result = num1 - num2
#         elif operation == 'multiply':
#             result = num1 * num2
#         elif operation == 'divide':
#             result = num1 / num2 if num2 != 0 else 'Division by zero error'

#         return render(request, 'calculator.html', {'result': result})
    
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     context['operations'] = ['add', 'subtract', 'multiply', 'divide']
#     #     return context

#     def post(self, request):
#         # Handle the form submission
#         num1 = float(request.POST.get('num1', 0))
#         num2 = float(request.POST.get('num2', 0))
#         operation = request.POST.get('operation', 'add')

#         if operation == 'add':
#             result = num1 + num2
#         elif operation == 'subtract':
#             result = num1 - num2
#         elif operation == 'multiply':
#             result = num1 * num2
#         elif operation == 'divide':
#             result = num1 / num2 if num2 != 0 else 'Division by zero error'

#         context = self.get_context_data()
#         context['result'] = result
#         return render(request, 'calculator.html', context)
    

        
#         return render(request, 'calculator.html', {'result': None})



# from django.views.generic import TemplateView

# class CalculatorView(TemplateView):
#     template_name = 'calculator.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['operations'] = ['add', 'subtract', 'multiply', 'divide']
#         context['result'] = None
#         return context

#     def post(self, request, *args, **kwargs):
#         context = self.get_context_data()
#         num1 = float(request.POST.get('num1', 0))
#         num2 = float(request.POST.get('num2', 0))
#         operation = request.POST.get('operation', 'add')

#         if operation == 'add':
#             result = num1 + num2
#         elif operation == 'subtract':
#             result = num1 - num2
#         elif operation == 'multiply':
#             result = num1 * num2
#         elif operation == 'divide':
#             result = num1 / num2 if num2 != 0 else 'Division by zero error'



#         context['result'] = result
#         return self.render_to_response(context)
    

from django.views import View
from django.shortcuts import render
import math

class CalculatorView(View):
    template_name = "calculator.html"

    def get(self, request):
        """Handle GET requests - show empty calculator initially"""
        return render(request, self.template_name, {"result": None, "expression": ""})

    def post(self, request):
        """Handle POST requests - process calculator expression"""
        expression = request.POST.get("expression", "")
        result = None
        try:
            # Safe evaluation with restricted functions
            result = eval(expression, {"__builtins__": None}, {
                "sqrt": math.sqrt,
                "pow": pow,
                "abs": abs,
                "pi": math.pi,
                "e": math.e,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "log": math.log
            })
        except Exception:
            result = "Error"

        return render(request, self.template_name, {"result": result, "expression": expression})