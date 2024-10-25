from django.urls import path
from .views import (
    VentaListView, VentaCreateView, VentaUpdateView, VentaDeleteView,
    CajaListView, CajaCreateView, CajaUpdateView, CajaDeleteView, AperturaCajaView, CierreCajaView,
    EmpleadoListView, EmpleadoCreateView, EmpleadoUpdateView, EmpleadoDeleteView,
    CompraListView, CompraCreateView, CompraUpdateView, CompraDeleteView,
    DetalleVentaListView, DetalleVentaCreateView, DetalleVentaUpdateView, DetalleVentaDeleteView,
    DetalleCompraListView, DetalleCompraCreateView, DetalleCompraUpdateView, DetalleCompraDeleteView,
    ProductoListView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView,
    ProveedorListView, ProveedorCreateView, ProveedorUpdateView, ProveedorDeleteView,
    ProdProvListView, ProdProvCreateView, ProdProvUpdateView, ProdProvDeleteView,registrar_usuario
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Ruta para el inicio de sesión
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    
    # Rutas para la Caja
    path('cajas/apertura/', AperturaCajaView.as_view(), name='apertura_caja'),
    
    path('cajas/cierre/<int:pk>/', CierreCajaView.as_view(), name='cierre_caja'),
    
    
    # Rutas para Ventas
    path('ventas/', VentaListView.as_view(), name='ventas_list'),
    path('ventas/nueva/', VentaCreateView.as_view(), name='ventas_create'),
    path('ventas/<int:pk>/editar/', VentaUpdateView.as_view(), name='ventas_edit'),
    path('ventas/<int:pk>/eliminar/', VentaDeleteView.as_view(), name='ventas_delete'),

    # Rutas para Cajas
    path('cajas/', CajaListView.as_view(), name='cajas_list'),
    path('cajas/nueva/', CajaCreateView.as_view(), name='cajas_create'),
    path('cajas/<int:pk>/editar/', CajaUpdateView.as_view(), name='cajas_edit'),
    path('cajas/<int:pk>/eliminar/', CajaDeleteView.as_view(), name='cajas_delete'),

    # Rutas para Empleados
    path('empleados/', EmpleadoListView.as_view(), name='empleados_list'),
    path('empleados/nuevo/', EmpleadoCreateView.as_view(), name='empleados_create'),
    path('empleados/<int:pk>/editar/', EmpleadoUpdateView.as_view(), name='empleados_edit'),
    path('empleados/<int:pk>/eliminar/', EmpleadoDeleteView.as_view(), name='empleados_delete'),

    # Rutas para Compras
    path('compras/', CompraListView.as_view(), name='compras_list'),
    path('compras/nueva/', CompraCreateView.as_view(), name='compras_create'),
    path('compras/<int:pk>/editar/', CompraUpdateView.as_view(), name='compras_edit'),
    path('compras/<int:pk>/eliminar/', CompraDeleteView.as_view(), name='compras_delete'),

    # Rutas para Detalle de Ventas
    path('detalle-ventas/', DetalleVentaListView.as_view(), name='detalle_ventas_list'),
    path('detalle-ventas/nueva/', DetalleVentaCreateView.as_view(), name='detalle_ventas_create'),
    path('detalle-ventas/<int:pk>/editar/', DetalleVentaUpdateView.as_view(), name='detalle_ventas_edit'),
    path('detalle-ventas/<int:pk>/eliminar/', DetalleVentaDeleteView.as_view(), name='detalle_ventas_delete'),

    # Rutas para Detalle de Compras
    path('detalle-compras/', DetalleCompraListView.as_view(), name='detalle_compras_list'),
    path('detalle-compras/nueva/', DetalleCompraCreateView.as_view(), name='detalle_compras_create'),
    path('detalle-compras/<int:pk>/editar/', DetalleCompraUpdateView.as_view(), name='detalle_compras_edit'),
    path('detalle-compras/<int:pk>/eliminar/', DetalleCompraDeleteView.as_view(), name='detalle_compras_delete'),

    # Rutas para Productos
    path('productos/', ProductoListView.as_view(), name='productos_list'),
    path('productos/nuevo/', ProductoCreateView.as_view(), name='productos_create'),
    path('productos/<int:pk>/editar/', ProductoUpdateView.as_view(), name='productos_edit'),
    path('productos/<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='productos_delete'),

    # Rutas para Proveedores
    path('proveedores/', ProveedorListView.as_view(), name='proveedores_list'),
    path('proveedores/nuevo/', ProveedorCreateView.as_view(), name='proveedores_create'),
    path('proveedores/<int:pk>/editar/', ProveedorUpdateView.as_view(), name='proveedores_edit'),
    path('proveedores/<int:pk>/eliminar/', ProveedorDeleteView.as_view(), name='proveedores_delete'),

    # Rutas para ProdProv (relación entre Productos y Proveedores)
    path('prod-prov/', ProdProvListView.as_view(), name='prod_prov_list'),
    path('prod-prov/nuevo/', ProdProvCreateView.as_view(), name='prod_prov_create'),
    path('prod-prov/<int:pk>/editar/', ProdProvUpdateView.as_view(), name='prod_prov_edit'),
    path('prod-prov/<int:pk>/eliminar/', ProdProvDeleteView.as_view(), name='prod_prov_delete'),
    path('registro/', registrar_usuario, name='registro_usuario'),
    path('register/', registrar_usuario, name='register'),
]



