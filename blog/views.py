from django.shortcuts import render
from django.views.generic import View #utilizamos vistas de clases la View lo importamos

# Create your views here.
class BlogListView(View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'blog_list.html',context)
