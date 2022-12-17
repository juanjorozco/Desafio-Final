from django.shortcuts import render
from django.http import HttpResponse
from AppFinal.models import Personal,Estudios,Experiencia
from django.core import serializers
from AppFinal.forms import PersonalForm,EstudiosForm,ExperienciaForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView

def inicio(request):
    return render(request,'AppFinal/inicio.html')

def informacion(request):
    return render(request,'AppFinal/informacion.html')

def list(request):
    return render(request,'AppFinal/list.html')

def busqueda(request):
    return render(request,'AppFinal/busqueda.html')

def leer_personal(request):
    personal_all = Personal.objects.all()
    return HttpResponse(serializers.serialize('json',personal_all))

def leer_estudios(request):
    estudios_all = Estudios.objects.all()
    return HttpResponse(serializers.serialize('json',estudios_all))

def leer_experiencia(request):
    experiencia_all = Experiencia.objects.all()
    return HttpResponse(serializers.serialize('json',experiencia_all))

class PersonalList(ListView):
    model = Personal
    template = 'AppFinal/personal_list.html'

class PersonalCreate(CreateView):
    model = Personal
    fields = '__all__'
    success_url = '/AppFinal/informacion/'

class EstudiosList(ListView):
    model = Estudios
    template = 'AppFinal/estudios_list.html'

class EstudiosCreate(CreateView):
    model = Estudios
    fields = '__all__'
    success_url = '/AppFinal/informacion/'

class ExperienciaList(ListView):
    model = Experiencia
    template = 'AppFinal/experiencia_list.html'

class ExperienciaCreate(CreateView):
    model = Experiencia
    fields = '__all__'
    success_url = '/AppFinal/informacion/'

class PersonalEdit(UpdateView):
    model = Personal
    fields = '__all__'
    success_url = '/AppFinal/personal/list/'

class PersonalDetail(DetailView):
    model = Personal
    template = 'AppFinal/personal_detail.html'

class PersonalDelete(DeleteView):
    model = Personal
    success_url = '/AppFinal/personal/list/'

class EstudiosEdit(UpdateView):
    model = Estudios
    fields = '__all__'
    success_url = '/AppFinal/estudios/list/'

class EstudiosDetail(DetailView):
    model = Estudios
    template = 'AppFinal/estudios_detail.html'

class EstudiosDelete(DeleteView):
    model = Estudios
    success_url = '/AppFinal/estudios/list/'

class ExperienciaEdit(UpdateView):
    model = Experiencia
    fields = '__all__'
    success_url = '/AppFinal/experiencia/list/'

class ExperienciaDetail(DetailView):
    model = Experiencia
    template = 'AppFinal/experiencia_detail.html'

class ExperienciaDelete(DeleteView):
    model = Experiencia
    success_url = '/AppFinal/experiencia/list/'

def busquedaEdad(request):
    return render(request,'AppFinal/busquedaEdad.html')

def edad(request):
    edad_views = request.GET["edad"]
    personal_todos=Personal.objects.filter(edad=edad_views)
    return render(request,"AppFinal/resultadoEdad.html",{"edad":edad_views,"personal":personal_todos})

def busquedaAños(request):
    return render(request,'AppFinal/busquedaAños.html')

def años(request):
    años_views = request.GET["años"]
    experiencia_todos=Experiencia.objects.filter(años_experiencia=años_views)
    return render(request,"AppFinal/resultadoAños.html",{"años":años_views,"experiencia":experiencia_todos})

def busquedaIdiomas(request):
    return render(request,'AppFinal/busquedaIdiomas.html')

def idiomas(request):
    idiomas_views = request.GET["idiomas"]
    estudios_todos=Estudios.objects.filter(idiomas=idiomas_views)
    return render(request,"AppFinal/resultadoIdiomas.html",{"idiomas":idiomas_views,"estudios":estudios_todos})
