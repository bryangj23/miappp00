from django.test import TestCase
from miapp00.wsgi import *
from erp.models import *

#Listar query

#query=Type.objects.all()

#print(query)

#insercion
#t=Type()
#t.name="Conductor"
#t.save()

#Edicion
#t=Type.objects.get(id=1)
#t.name="Dueño"
#t.save()

#Eliminacion
#t=Type.objects.get(id=1)
#t.delete()
#print(t)

categorias=Category()
categorias=Category.objects.all()
print(categorias)

#De esta forma igual funciona
clientes=Client.objects.all()
print(clientes)