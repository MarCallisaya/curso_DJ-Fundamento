from django.db import models

# Create your models here.
# manejar clases de python 

#se aplica herencia, ya que se te aplicando model
#estamos dicinedo que el estudiante se convierta en modelo, es decir, ya es una tabla
class Curso(models.Model): #uno
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField() # vacio no tiene limite
    fecha_inicio = models.DateField()


    def __str__(self):
        return self.nombre #solo vamos a devolver el nombre del curso
    
class Estudiante(models.Model): #Muchos
    # por defecto tendremos un campo id auto incrementable 1 en 1
    #ci = models.CharField(max_length=15,primary_key=True) #Para tener un primary key personalizado
    nombre = models.CharField(max_length=100) #esto hace que el texto tenga como 100 caracteres
    correo = models.EmailField(unique=True)   #esto hace que solo pueda haber un correo registrado por estudiante
    fecha_registro = models.DateTimeField(auto_now_add=True) # se va a agregar solo con la fecha del sistema, hay que verificar que este con la hora correcta en la zona horaria
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    
    #la cara de a clase
    def __str__(self):
        return self.nombre #solo vamos a devolver el nombre del estudiante

