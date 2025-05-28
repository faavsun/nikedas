from .models import Categoria, Marca

def categorias_processor(request):
    categorias = Categoria.objects.all()
    return {'categorias': categorias}

def marcas_processor(request):
    marcas = Marca.objects.all()
    return {'marcas': marcas}
