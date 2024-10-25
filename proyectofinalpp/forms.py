from django import forms
from .models import Venta, Caja, Empleado, Compra, DetalleVenta, DetalleCompra, Producto, Proveedor, ProdProv
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
# Formulario para Ventas
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['Fecha_hora_venta', 'Garantias', 'Productos', 'Precio_uni', 'Metodo_pago', 'Cantidad_vendida', 'Total_venta', 'VENT_AtGral']
        labels = {
            'Fecha_hora_venta': 'Fecha y Hora de la Venta',
            'Garantias': 'Garantías',
            'Productos': 'Producto',
            'Precio_uni': 'Precio Unitario',
            'Metodo_pago': 'Método de Pago',
            'Cantidad_vendida': 'Cantidad Vendida',
            'Total_venta': 'Total de la Venta',
            'VENT_AtGral': 'Venta General',
        }
        widgets = {
            'Fecha_hora_venta': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'Garantias': forms.TextInput(attrs={'class': 'form-control'}),
            'Productos': forms.Select(attrs={'class': 'form-control'}),
            'Precio_uni': forms.NumberInput(attrs={'class': 'form-control'}),
            'Metodo_pago': forms.Select(attrs={'class': 'form-control'}),
            'Cantidad_vendida': forms.NumberInput(attrs={'class': 'form-control'}),
            'Total_venta': forms.NumberInput(attrs={'class': 'form-control'}),
            'VENT_AtGral': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(VentaForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False

# Formulario para Cajas
class CajaForm(forms.ModelForm):
    class Meta:
        model = Caja
        fields = ['Saldo_inicial', 'Fecha_Apertura',  'empleado']
        labels = {
            'Saldo_inicial': 'Saldo Inicial',
            'Fecha_Apertura': 'Fecha de Apertura',
            
            'empleado': 'Empleado',
        }
        widgets = {
            'Saldo_inicial': forms.NumberInput(attrs={'class': 'form-control'}),
            'Fecha_Apertura': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        
        }

# Formulario para apertura de caja
class CajaAperturaForm(forms.ModelForm):
    class Meta:
        model = Caja
        fields = ['Saldo_inicial', 'Fecha_Apertura']
        labels = {
            'Saldo_inicial': 'Saldo Inicial',
            'Fecha_Apertura': 'Fecha y Hora de Apertura',
        }
        widgets = {
            'Saldo_inicial': forms.NumberInput(attrs={'class': 'form-control'}),
            'Fecha_Apertura': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
                'value': timezone.now().strftime('%Y-%m-%dT%H:%M')
            }),
        }

# Formulario para cierre de caja
class CajaCierreForm(forms.ModelForm):
    class Meta:
        model = Caja
        fields = ['Fecha_Cierre', 'Saldo_final']
        labels = {
            'Fecha_Cierre': 'Fecha de Cierre',
            'Saldo_final': 'Saldo Final',
        }
        widgets = {
            'Fecha_Cierre': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'Saldo_final': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# Formulario para Empleados
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['Telefono', 'No_Documento', 'Direccion']
        labels = {
            'Telefono': 'Teléfono',
            'No_Documento': 'Número de Documento',
            'Direccion': 'Dirección',
        }

    def clean_Telefono(self):
        telefono = self.cleaned_data['Telefono']
        if len(str(telefono)) != 10:
            raise ValidationError("El número de teléfono debe tener exactamente 10 dígitos.")
        return telefono

# Formulario para Compras
class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['Fecha_hora_compra', 'Nro_Compra', 'Metodo_pago', 'Producto', 'Precio', 'Cantidad', 'Total_compra', 'id_proveedor']
        labels = {
            'Fecha_hora_compra': 'Fecha y Hora de la Compra',
            'Nro_Compra': 'Número de Compra',
            'Metodo_pago': 'Método de Pago',
            'Producto': 'Producto',
            'Precio': 'Precio',
            'Cantidad': 'Cantidad',
            'Total_compra': 'Total de la Compra',
            'id_proveedor': 'ID del Proveedor',
        }

# Formulario para Detalle de Ventas
class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['idVentas', 'idProducto', 'Cant_vendida', 'Prec_uni']
        labels = {
            'idVentas': 'ID de la Venta',
            'idProducto': 'ID del Producto',
            'Cant_vendida': 'Cantidad Vendida',
            'Prec_uni': 'Precio Unitario',
        }

# Formulario para Detalle de Compras
class DetalleCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleCompra
        fields = ['idCompra', 'idProducto', 'Cant_Comprada', 'Prec_uni']
        labels = {
            'idCompra': 'ID de la Compra',
            'idProducto': 'ID del Producto',
            'Cant_Comprada': 'Cantidad Comprada',
            'Prec_uni': 'Precio Unitario',
        }

# Formulario para Productos
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['Nombre', 'Descripcion', 'Precio', 'Stock', 'Marca']
        labels = {
            'Nombre': 'Nombre del Producto',
            'Descripcion': 'Descripción',
            'Precio': 'Precio',
            'Stock': 'Stock',
            'Marca': 'Marca',
        }

# Formulario para Proveedores
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['CUIT', 'Telefono', 'Correo', 'Domicilio', 'Nombre']
        labels = {
            'CUIT': 'CUIT',
            'Telefono': 'Teléfono',
            'Correo': 'Correo Electrónico',
            'Domicilio': 'Domicilio',
            'Nombre': 'Nombre del Proveedor',
        }

# Formulario para Prod_Prov
class ProdProvForm(forms.ModelForm):
    class Meta:
        model = ProdProv
        fields = ['producto', 'proveedor']
        labels = {
            'producto': 'Producto',
            'proveedor': 'Proveedor',
        }


class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    is_admin = forms.BooleanField(label="Registrar como Admin", required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user