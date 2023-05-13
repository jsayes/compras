from django.shortcuts import render
from examencompras.models import Persona
# Create your views here.
def base(request):
    return render(request, 'base.html')


def descuento(request):
    if request.method == 'POST':
        total_compras = float(request.POST['total_compras'])
        if total_compras <= 100.00:
            descuento = 0
        elif 101.00 <= total_compras <= 200.00:
            descuento = 0.15
        elif 201.00 <= total_compras <= 300.00:
            descuento = 0.20
        else:
            descuento = 0
        total_con_descuento = total_compras - (total_compras * descuento)
        persona = Persona(total_compras=total_con_descuento)
        persona.save()
        return render(request, 'descuento.html', {'persona': persona})
    else:
        return render(request, 'descuento.html')