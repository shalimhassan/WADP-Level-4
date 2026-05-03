from django.shortcuts import render

# Create your views here.

def add_product(request):
  if request.mothod =='POST':
    form_data = ProductForm(request.POST)
    if form_data.is_valid():
      form_data = form_data.save(commit=False)
      form_data.created_by = request.user
      form_data.total_amount = form_data.price * Decimal()