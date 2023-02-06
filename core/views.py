from django.views.generic import View #utilizamos vistas de clases la View lo importamos
from django.shortcuts import render #importamos el render

class HomeView(View):#cuando utilizamos una clase debemos utilizar self
    def get(self, request, *args, **kwars):#esto hace referencia a cualquier parametro que nuestro request pueda tener lo vamos a utilizar para obetr el id del ussuario
        context={
            
        }
        return render(request, 'index.html',context)#aqui retornamos el template lo que tiene el osea index.html osea la informacion en html q vamos a mostrar el template gusrda todos los html