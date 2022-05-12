from django.shortcuts import render


# Create your views here.
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>CHUCK NORRIS</h1>')

def about(request):
  return render(request, 'about.html')

def chucknorris_index(request):
  return render(request, 'chucknorris/index.html', { 'chucknorris': chucknorris })

def home(request):
  # Request the list of categories
  ...
  # Get the category from the submitted form
  category = request.GET.get('category')
  if category:
    # The form was submitted with a selected category
    # Request a joke from the category
    ...
  else:
    # No form was submitted...
    # Just random joke!
    ...
  render(request, 'home.html', {'joke': joke, 'categories': categories})