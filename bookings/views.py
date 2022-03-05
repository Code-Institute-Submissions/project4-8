from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.views import generic, View
from .models import bookTable
from .models import TableInverntory
from .forms import BookTableForm

def index(request):
    return render(request, 'index.html', context=None)

def login(request):
    return render(request, 'login.html', context=None)

def signUp(request):
    return render(request, 'Sign-up.html', context=None)
    
def loggedin(request):
    return render(request, 'logged-in.html', context=None)

# def bookTables(request):
#     form = BookTableForm()
#     mydict = {'form': form}
#     return render(request, 'book-table.html', context=mydict)

class BookingTables(TemplateView):
    template_name = 'book-tables.html'

    def get(self, request):
        form = BookTableForm()
        return render(request, 'book-table.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = BookTableForm(data=request.POST)
        Table_booked = False
        if form.is_valid():
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            people = request.POST['people']
            pick_date = request.POST['pick_date']
            pick_time = request.POST['pick_time']
            
            if len(people) <= 5 and len(people) > 0:
                Tablecount == -1
                if len(people) > 5 and len(people) <= 10:
                    Tablecount == -2
                    if len(people) >= 10 and len(people) <=15:
                        Tablecount == -3
                        if len(people) >=15 and len(people) <=20:
                            Tablecount == -4
                            
            if Tablecount > 0:
                print('tables available')
            else:
                print('Not enough tables, please try book a different date.')

            if first_name and last_name in request.POST['pick_date'].exists():
                raise Error('cannot book you here again, please pick a different date.')



            
            Table_booked = True
            BookTable = bookTable(first_name=first_name, last_name=last_name, people=people, pick_date=pick_date, pick_time=pick_time)
            BookTable.save()
        else:
            form = BookTableForm()


        return render(request, 'book-table.html', context={'form': form, 'Table_booked': Table_booked})


       
        
           
              
                
                  
                    
                        

