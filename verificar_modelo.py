import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoBiblioteca.settings')
django.setup()

from sril.models import Libro

def extraer_paginas_para_todos():
    print("🚀 EXTRACCIÓN DE NÚMERO DE PÁGINAS")
    print("=" * 50)
    
    libros_con_pdf = Libro.objects.filter(archivo_pdf__isnull=False)
    
    print(f"📚 Libros con PDF: {libros_con_pdf.count()}")
    
    for i, libro in enumerate(libros_con_pdf, 1):
        print(f"\n[{i}/{libros_con_pdf.count()}] 📖 {libro.titulo}")
        print(f"   📄 Páginas actuales: {libro.numero_paginas}")
        
        # Extraer páginas
        if libro.extraer_numero_paginas():
            libro.save()
            print(f"   ✅ Nuevas páginas: {libro.numero_paginas}")
        else:
            print("   ❌ No se pudieron extraer las páginas")
    
    print("\n" + "=" * 50)
    print("✅ EXTRACCIÓN COMPLETADA")

if __name__ == "__main__":
    extraer_paginas_para_todos()