<<<<<<< HEAD
from django.shortcuts import render
from django.views import View

class Homepage(View):
	def get(self,request):
		return render(request,'Home/index.html')


=======

# Create your views here.
#listing of items found

from django.shortcuts import render, reverse
from django.contrib import messages
from django.http.response import HttpResponseRedirect

from .models import Found_item

def search_page(request):
    context = dict()
    context['section'] = 'Search Page'
    template = "test/search_page.html"
    return render(request, template, context)


def result_page(request):
    context = dict()
    context['section'] = 'Results'
    template = "test/result_page.html"

    if request.method == 'POST':
        id_number = request.POST.get('ID_number')

        if id_number is None:
            messages.error(request, 'You need to key in an ID number')
            return HttpResponseRedirect(reverse('search_page'))

        
        items = Found_item.objects.all().filter(idNo__contains=id_number)
        
        context['items'] = items
        context['id_number'] = id_number

        return render(request, template, context)

    return render(request, template, context)
>>>>>>> d8a67fb0ae64310a4c827db3683439734ee72375
