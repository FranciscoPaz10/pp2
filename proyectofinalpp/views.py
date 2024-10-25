from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Venta, Caja, Empleado, Compra, DetalleVenta, DetalleCompra, Producto, Proveedor, ProdProv
from .forms import VentaForm, CajaForm, CajaCierreForm, EmpleadoForm, CompraForm, DetalleVentaForm, DetalleCompraForm, ProductoForm, ProveedorForm, ProdProvForm,CajaAperturaForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages


# Página de inicio (autenticación requerida)
@login_required
def inicio(request):
    ventas = Venta.objects.all()
    cajas = Caja.objects.all()
    compras = Compra.objects.all()

    context = {
        'ventas': ventas,
        'cajas': cajas,
        'compras': compras,
    }
    
    return render(request, 'inicio.html', context)

# Vistas para Ventas
class VentaListView(LoginRequiredMixin, ListView):
    model = Venta
    template_name = 'ventas/lista_ventas.html'
    context_object_name = 'ventas'

class VentaCreateView(LoginRequiredMixin, CreateView):
    model = Venta
    form_class = VentaForm
    template_name = 'ventas/crear_venta.html'
    success_url = reverse_lazy('ventas_list')

class VentaUpdateView(LoginRequiredMixin, UpdateView):
    model = Venta
    form_class = VentaForm
    template_name = 'ventas/editar_venta.html'
    success_url = reverse_lazy('ventas_list')

class VentaDeleteView(LoginRequiredMixin, DeleteView):
    model = Venta
    template_name = 'ventas/eliminar_venta.html'
    success_url = reverse_lazy('ventas_list')

# Vistas para Cajas
class CajaListView(LoginRequiredMixin, ListView):
    model = Caja
    template_name = 'cajas/lista_cajas.html'
    context_object_name = 'cajas'

class CajaCreateView(LoginRequiredMixin, CreateView):
    model = Caja
    form_class = CajaForm
    template_name = 'cajas/crear_caja.html'
    success_url = reverse_lazy('cajas_list')

    def form_valid(self, form):
        # Asigna el empleado relacionado con el usuario autenticado
        caja = form.save(commit=False)
        caja.empleado = Empleado.objects.get(usuario=self.request.user)
        caja.save()
        return super().form_valid(form)



class CajaUpdateView(LoginRequiredMixin, UpdateView):
    model = Caja
    form_class = CajaForm
    template_name = 'cajas/editar_caja.html'
    success_url = reverse_lazy('cajas_list')

class CajaDeleteView(LoginRequiredMixin, DeleteView):
    model = Caja
    template_name = 'cajas/eliminar_caja.html'
    success_url = reverse_lazy('cajas_list')

# Vista para Cierre de Caja

class CierreCajaView(UpdateView):
    model = Caja
    form_class = CajaCierreForm
    template_name = 'cajas/cierre_caja.html'
    success_url = reverse_lazy('cajas_list')

    def get_queryset(self):
        # Filtrar solo cajas que no han sido cerradas
        return Caja.objects.filter(Fecha_Cierre__isnull=True)

    def form_valid(self, form):
        caja = form.save(commit=False)
        caja.Fecha_Cierre = form.cleaned_data['Fecha_Cierre']  # Cierra la caja con la fecha proporcionada
        caja.save()
        return super().form_valid(form)



# Vista para Apertura de Caja
class AperturaCajaView(LoginRequiredMixin, UpdateView):
    model = Caja
    form_class = CajaForm
    template_name = 'cajas/apertura_caja.html'
    success_url = reverse_lazy('cajas_list')

# Vistas para Empleados
class EmpleadoListView(LoginRequiredMixin, ListView):
    model = Empleado
    template_name = 'empleados/lista_empleados.html'
    context_object_name = 'empleados'

class EmpleadoCreateView(CreateView):
    model = Empleado
    fields = ['Telefono', 'No_Documento', 'Direccion']  # Incluye los campos que deseas
    template_name = 'empleado_form.html'
    success_url = reverse_lazy('empleados_list')


    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Asigna el usuario logueado
        return super().form_valid(form)
class EmpleadoUpdateView(LoginRequiredMixin, UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/editar_empleado.html'
    success_url = reverse_lazy('empleados_list')

class EmpleadoDeleteView(LoginRequiredMixin, DeleteView):
    model = Empleado
    template_name = 'empleados/eliminar_empleado.html'
    success_url = reverse_lazy('empleados_list')

# Vistas para Compras
class CompraListView(LoginRequiredMixin, ListView):
    model = Compra
    template_name = 'compras/lista_compras.html'
    context_object_name = 'compras'

class CompraCreateView(LoginRequiredMixin, CreateView):
    model = Compra
    form_class = CompraForm
    template_name = 'compras/crear_compra.html'
    success_url = reverse_lazy('compras_list')

class CompraUpdateView(LoginRequiredMixin, UpdateView):
    model = Compra
    form_class = CompraForm
    template_name = 'compras/editar_compra.html'
    success_url = reverse_lazy('compras_list')

class CompraDeleteView(LoginRequiredMixin, DeleteView):
    model = Compra
    template_name = 'compras/eliminar_compra.html'
    success_url = reverse_lazy('compras_list')

# Vistas para DetalleVenta
class DetalleVentaListView(LoginRequiredMixin, ListView):
    model = DetalleVenta
    template_name = 'detalle_ventas/lista_detalle_ventas.html'
    context_object_name = 'detalle_ventas'

class DetalleVentaCreateView(LoginRequiredMixin, CreateView):
    model = DetalleVenta
    form_class = DetalleVentaForm
    template_name = 'detalle_ventas/crear_detalle_venta.html'
    success_url = reverse_lazy('detalle_ventas_list')

class DetalleVentaUpdateView(LoginRequiredMixin, UpdateView):
    model = DetalleVenta
    form_class = DetalleVentaForm
    template_name = 'detalle_ventas/editar_detalle_venta.html'
    success_url = reverse_lazy('detalle_ventas_list')

class DetalleVentaDeleteView(LoginRequiredMixin, DeleteView):
    model = DetalleVenta
    template_name = 'detalle_ventas/eliminar_detalle_venta.html'
    success_url = reverse_lazy('detalle_ventas_list')

# Vistas para DetalleCompra
class DetalleCompraListView(LoginRequiredMixin, ListView):
    model = DetalleCompra
    template_name = 'detalle_compras/lista_detalle_compras.html'
    context_object_name = 'detalle_compras'

class DetalleCompraCreateView(LoginRequiredMixin, CreateView):
    model = DetalleCompra
    form_class = DetalleCompraForm
    template_name = 'detalle_compras/crear_detalle_compra.html'
    success_url = reverse_lazy('detalle_compras_list')

class DetalleCompraUpdateView(LoginRequiredMixin, UpdateView):
    model = DetalleCompra
    form_class = DetalleCompraForm
    template_name = 'detalle_compras/editar_detalle_compra.html'
    success_url = reverse_lazy('detalle_compras_list')

class DetalleCompraDeleteView(LoginRequiredMixin, DeleteView):
    model = DetalleCompra
    template_name = 'detalle_compras/eliminar_detalle_compra.html'
    success_url = reverse_lazy('detalle_compras_list')

# Vistas para Productos
class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'productos/lista_productos.html'
    context_object_name = 'productos'

class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/crear_producto.html'
    success_url = reverse_lazy('productos_list')

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/editar_producto.html'
    success_url = reverse_lazy('productos_list')

class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'productos/eliminar_producto.html'
    success_url = reverse_lazy('productos_list')

# Vistas para Proveedores
class ProveedorListView(LoginRequiredMixin, ListView):
    model = Proveedor
    template_name = 'proveedores/lista_proveedores.html'
    context_object_name = 'proveedores'

class ProveedorCreateView(LoginRequiredMixin, CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedores/crear_proveedor.html'
    success_url = reverse_lazy('proveedores_list')

class ProveedorUpdateView(LoginRequiredMixin, UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedores/editar_proveedor.html'
    success_url = reverse_lazy('proveedores_list')

class ProveedorDeleteView(LoginRequiredMixin, DeleteView):
    model = Proveedor
    template_name = 'proveedores/eliminar_proveedor.html'
    success_url = reverse_lazy('proveedores_list')

# Vistas para ProdProv
class ProdProvListView(LoginRequiredMixin, ListView):
    model = ProdProv
    template_name = 'prod_prov/lista_prod_prov.html'
    context_object_name = 'prod_prov'

class ProdProvCreateView(LoginRequiredMixin, CreateView):
    model = ProdProv
    form_class = ProdProvForm
    template_name = 'prod_prov/crear_prod_prov.html'
    success_url = reverse_lazy('prod_prov_list')

class ProdProvUpdateView(LoginRequiredMixin, UpdateView):
    model = ProdProv
    form_class = ProdProvForm
    template_name = 'prod_prov/editar_prod_prov.html'
    success_url = reverse_lazy('prod_prov_list')

class ProdProvDeleteView(LoginRequiredMixin, DeleteView):
    model = ProdProv
    template_name = 'prod_prov/eliminar_prod_prov.html'
    success_url = reverse_lazy('prod_prov_list')

from .forms import RegistroUsuarioForm

from django.contrib.auth.models import Group, Permission

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Asigna grupo y permisos basados en si es admin o no
            if form.cleaned_data['is_admin']:
                # Asigna permisos de administrador
                admin_group, created = Group.objects.get_or_create(name='Admin')
                user.groups.add(admin_group)
                permisos_admin = Permission.objects.all()  # Todos los permisos para el admin
                user.user_permissions.set(permisos_admin)
            else:
                # Asigna el usuario al grupo "Gestores" (crea el grupo si no existe)
                gestores_group, created = Group.objects.get_or_create(name='Gestores')
                user.groups.add(gestores_group)
                
                # Asignar permisos específicos de usuarios comunes
                permiso = Permission.objects.get(codename='add_caja')  # Ejemplo de permiso específico
                user.user_permissions.add(permiso)

            return redirect('login')  # Redirige al login después del registro
    else:
        form = RegistroUsuarioForm()

    return render(request, 'registration/registro.html', {'form': form})