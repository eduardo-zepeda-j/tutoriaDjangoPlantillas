from django.shortcuts import render,redirect
from django.views.generic import *
from .forms import *


# Create your views here.
class Index(TemplateView):
    template_name = "index.html"

   
        
    def render_to_response(self, context, **response_kwargs):
        
        diccionario = {"form":self.form}
        #context.update(diccionario)
        
        return super().render_to_response(context, **response_kwargs)
    
    def indexView(request):
        form = Persona()
        
        if request.method == 'POST':
            form = Persona(data = request.POST)
            itemsPost = request.POST.items()
            print('este es el itempost')
            diccionarioSesion ={}
            nombre =''
            apellido = ''
            for key, value in request.POST.items():
                
                if key == 'nombre':
                    nombre = value
                if key == 'apellido':
                    apellido = value
                
            diccionarioSesion.update(nombre = nombre, apellido = apellido)
            
            print(diccionarioSesion)
            variableSesion = request.session['datos'] = diccionarioSesion

            return redirect('home')
        
        return render(request,'index.html',{'form':form})

class Home(TemplateView):
    template_name = "home.html"
    
    def decirHola(request):
        diccionarioSesion = request.session['datos']
        
        nombre = diccionarioSesion.get('nombre')
        apellido = diccionarioSesion.get('apellido')
        
        print(nombre)
        print(apellido)
        
        return render(request,'home.html',{'nombre':nombre,'apellido':apellido})