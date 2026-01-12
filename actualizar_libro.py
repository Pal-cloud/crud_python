#!/usr/bin/env python
import os
import sys
import django

# Configurar Django
sys.path.append('.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_libros.settings')
django.setup()

from sistema_libros.models import Libro
from datetime import date

def actualizar_libro():
    try:
        # Buscar el libro con ID 1
        libro = Libro.objects.get(id=1)
        
        print(f"📖 Libro actual: {libro.titulo} - {libro.autor}")
        
        # Actualizar los datos
        libro.titulo = 'Tengo miedo miedo'
        libro.autor = 'Pedro Lemebel'
        libro.descripcion = 'Una colección de crónicas urbanas que retrata con intensidad la realidad marginal y diversa de Santiago de Chile.'
        libro.fecha_publicacion = date(1997, 1, 1)
        libro.isbn = '9789562391840'
        libro.save()
        
        print(f"✅ Libro actualizado: {libro.titulo} - {libro.autor}")
        
        # Mostrar todos los libros
        print("\n📚 Todos los libros:")
        for l in Libro.objects.all():
            print(f"  {l.id}: {l.titulo} - {l.autor} ({l.fecha_publicacion.year})")
            
    except Libro.DoesNotExist:
        print("❌ No se encontró el libro con ID 1")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    actualizar_libro()
