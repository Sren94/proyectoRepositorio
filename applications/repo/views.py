from django.shortcuts import render
from django.views.generic import ListView
from .models import Archive
class ArchiveList(ListView):
    context_object_name = 'arch'
    template_name='archives/listArchive.html'
    paginate_by=10  
    ordering='id'
    
    def get_queryset(self):
        #print('++++++++++++++++++++++++++++')
        search = self.request.GET.get('Search','')
        print(f'{search}')
        list= Archive.objects.filter(
            #aqui hace una busqueda al momento de enlazar la peticion
            title__icontains=search
            )
        #print(list)
        return list
    