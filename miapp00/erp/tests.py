from django.test import TestCase
from miapp00.wsgi import *
from erp.models import Type

#Listar query

query=Type.objects.all()

print(query)

#insercion
t=Type()
#t.name="Conductor"
#t.save()

#Edicion
#t=Type.objects.get(id=1)
#t.name="Dueño"
#t.save()

#Eliminacion
t=Type.objects.get(id=1)
t.delete()
print(t)