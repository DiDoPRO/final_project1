from django.shortcuts import render

# Create your views here.
from .models import Food, Table, TableInstance, Type, Drink

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_tables = Table.objects.all().count()
    num_instances = TableInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = TableInstance.objects.filter(status__exact='a').count()
  # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=None)

from django.views import generic

class TableListView(generic.ListView):
    model = Table 
   
class TableDetailView(generic.DetailView):
    model = Table    

class FoodListView(generic.ListView):
    model = Food

class FoodDetailView(generic.DetailView):
    model = Food      

class DrinkListView(generic.ListView):
    model = Drink

class DrinkDetailView(generic.DetailView):
    model = Drink  
    
import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from catalog.forms import RenewTableForm

@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def renew_table_restoran(request, pk):
    """View function for renewing a specific BookInstance by librarian."""
    table_instance = get_object_or_404(TableInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewTableForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            table_instance.due_back = form.cleaned_data['renewal_date']
            table_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed') )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewTableForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'table_instance': table_instance,
    }

    return render(request, 'catalog/table_renew_restoran.html', context)    