from django.contrib import admin
from .models import Caja, Empleado, Venta, Compra, DetalleVenta, DetalleCompra, Producto, Proveedor, ProdProv

# Admin para Caja
@admin.register(Caja)
class CajaAdmin(admin.ModelAdmin):
    list_display = ('idCajas', 'Saldo_inicial', 'Fecha_Apertura', 'Fecha_Cierre', 'empleado')
    search_fields = ('empleado__usuario__username', 'Fecha_Apertura')
    list_filter = ('Fecha_Apertura', 'Fecha_Cierre')

# Admin para Empleado
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id_Empleados', 'usuario', 'Telefono', 'No_Documento', 'Direccion')
    search_fields = ('usuario__username', 'No_Documento')
    list_filter = ('No_Documento',)

# Admin para Venta
@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('idVentas', 'Fecha_hora_venta', 'Productos', 'Total_venta', 'Metodo_pago', 'VENT_AtGral')
    search_fields = ('Productos__Nombre', 'Metodo_pago')
    list_filter = ('Fecha_hora_venta', 'Metodo_pago')

# Admin para Compra
@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('idCompras', 'Fecha_hora_compra', 'Producto', 'Total_compra', 'Metodo_pago', 'id_proveedor')
    search_fields = ('Producto', 'Metodo_pago')
    list_filter = ('Fecha_hora_compra', 'Metodo_pago')

# Admin para DetalleVenta
@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('id_DetVta', 'idVentas', 'idProducto', 'Cant_vendida', 'Prec_uni')
    search_fields = ('idVentas__idVentas', 'idProducto__Nombre')
    list_filter = ('idVentas', 'idProducto')

# Admin para DetalleCompra
@admin.register(DetalleCompra)
class DetalleCompraAdmin(admin.ModelAdmin):
    list_display = ('id_DetCompra', 'idCompra', 'idProducto', 'Cant_Comprada', 'Prec_uni')
    search_fields = ('idCompra__idCompras', 'idProducto__Nombre')
    list_filter = ('idCompra', 'idProducto')

# Admin para Producto
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('idProducto', 'Nombre', 'Descripcion', 'Precio', 'Stock', 'Marca')
    search_fields = ('Nombre', 'Marca')
    list_filter = ('Marca', 'Stock')

# Admin para Proveedor
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id_proveedor', 'Nombre', 'CUIT', 'Telefono', 'Correo', 'Domicilio')
    search_fields = ('Nombre', 'CUIT')
    list_filter = ('CUIT',)

# Admin para ProdProv
@admin.register(ProdProv)
class ProdProvAdmin(admin.ModelAdmin):
    list_display = ('id_prod_prov', 'producto', 'proveedor')
    search_fields = ('producto__Nombre', 'proveedor__Nombre')
    list_filter = ('producto', 'proveedor')
