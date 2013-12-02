from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from models import Book
from forms import ContactForm

# Create your views here.
def search_form(request):
    query = request.GET.get('q', '')
    if query == '':
        return render(request, 'search_form.html', {'error': True})
    qbooks = Book.objects.filter(title__icontains=query)
    return render(request, "search_res.html", {'query': query, 'books':qbooks})
    

def search_res(request):
    query = request.GET.get('q', '')
    if query == '':
        return render(request, 'search_form.html', {'error': True})
    qbooks = Book.objects.filter(title__icontains=query)
    return render(request, "search_res.html", {'query': query, 'books':qbooks})

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('thanks/')
    return render(request, 'contact.html', {'form': form})

def thank(request):
    return render(request, 'thank.html')

def haha(request,num):
    return HttpResponse("hello world. " + num)

def hahaha(request,num):
    return HttpResponse("hello world. " + num)
