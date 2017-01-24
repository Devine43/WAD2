from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   # Construct a dictionary to pass the template engine as its context
   # Note they key boldmessage is the same as {{ boldmessage }} in the template!
   context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

   #Return a rendered response to send to the client
   #We make use of the shortcut function to make our lives easier
   #Note that the first parameter is the template we wish to use
   return render(request, 'rango/index.html',context=context_dict)

def about(request):
    #Construct a dictionary to pass the template engine as its context
    context_dict = {'boldmessage':"Veiled Chameleon, Water Monitor, Komodo Dragon "}

    #Return a rendered response to send to the client
    return render(request, 'rango/about.html', context=context_dict)

