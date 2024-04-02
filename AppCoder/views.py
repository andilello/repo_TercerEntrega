from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario
from AppCoder.models import Profesor
from AppCoder.models import Alumno
from AppCoder.models import Entregable
from AppCoder.forms import ProfesorFormulario
from AppCoder.forms import AlumnoFormulario
from AppCoder.forms import EntregableFormulario
# Create your views here.



def inicio(request):
    return render( request , "padre.html")


def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def ver_profesores(request):
    profesores = Profesor.objects.all()
    dicc = {"profesores": profesores}
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    dicc = {"alumnos": alumnos}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def ver_entregables(request):
    entregable = Entregable.objects.all()
    dicc = {"entregables": entregables}
    plantilla = loader.get_template("entregables.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def alumnos(request):
    return render(request , "alumnos.html")

def profesores(request):
    return render(request , "profesores.html")

def entregables(request):
    return render(request , "entregables.html" )







def curso_formulario(request):

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=datos["nombre"] , camada=datos["camada"])
            curso.save()
            return render(request , "formulario.html")


    return render(request , "formulario.html")

def buscar_curso(request):

    return render(request, "buscar_curso.html")



def buscar(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render( request , "resultado_busqueda.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")
    

def elimina_curso(request , id ):
    curso = Curso.objects.get(id=id)
    curso.delete()

    curso = Curso.objects.all()

    return render(request , "cursos.html" , {"cursos":curso})




def editar(request , id):

    curso = Curso.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()

            curso = Curso.objects.all()

            return render(request , "cursos.html" , {"cursos":curso})


        
    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre , "camada":curso.camada})
    
    return render( request , "editar_curso.html" , {"mi_formulario": mi_formulario , "curso":curso})


def profesor_formulario(request):
    if request.method == "POST":
        mi_formulario = ProfesorFormulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            Profesor.objects.create(**datos)
            return render(request, "formulario_profesor.html", {"mensaje": "Profesor creado correctamente"})
    else:
        mi_formulario = ProfesorFormulario()
    return render(request, "formulario_profesor.html", {"mi_formulario": mi_formulario})


def editar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = ProfesorFormulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            for clave, valor in datos.items():
                setattr(profesor, clave, valor)
            profesor.save()
            return render(request, "formulario_profesor.html", {"mensaje": "Profesor editado correctamente"})
    else:
        mi_formulario = ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido, 
                                                    'email': profesor.email, 'especialidad': profesor.especialidad})
    return render(request, "editar_profesor.html", {"mi_formulario": mi_formulario, "profesor": profesor})

def elimina_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    return render(request, "formulario_profesor.html", {"mensaje": "Profesor eliminado correctamente"})



def alumno_formulario(request):
    if request.method == "POST":
        mi_formulario = AlumnoFormulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            Alumno.objects.create(**datos)
            return render(request, "formulario_alumno.html", {"mensaje": "Alumno creado correctamente"})
    else:
        mi_formulario = AlumnoFormulario()
    return render(request, "formulario_alumno.html", {"mi_formulario": mi_formulario})


def editar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = AlumnoFormulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            for clave, valor in datos.items():
                setattr(alumno, clave, valor)
            alumno.save()
            return render(request, "formulario_alumno.html", {"mensaje": "Alumno creado correctamente"})
    else:
        mi_formulario = AlumnoFormulario(initial={'nombre': alumno.nombre, 'apellido': alumno.apellido, 'email': alumno.email, 'fecha_nacimiento': alumno.fecha_nacimiento})
    return render(request, "editar_alumno.html", {"mi_formulario": mi_formulario, "alumno": alumno})

def elimina_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    return render(request, "formulario_alumno.html", {"mensaje": "Alumno eliminado correctamente"})


def entregable_formulario(request):
    if request.method == "POST":
        mi_formulario = EntregableFormulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            Entregable.objects.create(**datos)
            return render(request, "formulario_entregable.html", {"mensaje": "Entregable creado correctamente"})
    else:
        mi_formulario = EntregableFormulario()
    return render(request, "formulario_entregable.html", {"mi_formulario": mi_formulario})


def editar_entregable(request, id):
    entregable = Entregable.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = EntregableFormulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            for clave, valor in datos.items():
                setattr(entregable, clave, valor)
            entregable.save()
            return render(request, "formulario_entregable.html", {"mensaje": "Entregable editado correctamente"}) 
    else:
        mi_formulario = EntregableFormulario(initial={'titulo': entregable.titulo, 'descripcion': entregable.descripcion, 'fecha_de_entrega': entregable.fecha_de_entrega, 'entregado': entregable.entregado})
    return render(request, "editar_entregable.html", {"mi_formulario": mi_formulario, "entregable": entregable})

def elimina_entregable(request, id):
    entregable = Entregable.objects.get(id=id)
    entregable.delete()
    return render(request, "formulario_entregable.html", {"mensaje": "Entregable eliminado correctamente"})  



