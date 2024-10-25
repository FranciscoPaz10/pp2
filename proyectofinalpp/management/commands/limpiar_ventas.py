from django.core.management.base import BaseCommand
from proyectofinalpp.models import Venta

class Command(BaseCommand):
    help = 'Limpia ventas con productos no válidos'

    def handle(self, *args, **kwargs):
        # Filtra todas las ventas con un producto no válido
        ventas_invalidas = Venta.objects.filter(Productos__isnull=True)
        for venta in ventas_invalidas:
            print(f'Eliminando venta inválida: {venta}')
            venta.delete()
        self.stdout.write(self.style.SUCCESS('Ventas inválidas eliminadas.'))
