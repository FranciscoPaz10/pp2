from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Empleado(models.Model):
    id_Empleados = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación con el usuario
    Telefono = models.CharField(max_length=15)
    No_Documento = models.IntegerField()
    Direccion = models.CharField(max_length=45)

    def __str__(self):
        return f'{self.usuario.username} - {self.No_Documento}'  # Mostrar el usuario y el documento


class Caja(models.Model):
    idCajas = models.AutoField(primary_key=True)
    Saldo_inicial = models.FloatField()
    Saldo_final = models.FloatField(null=True, blank=True)  # Agregar este campo
    Fecha_Apertura = models.DateTimeField()
    Fecha_Cierre = models.DateTimeField(null=True, blank=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def __str__(self):
        return f'Caja {self.idCajas} - Empleado: {self.empleado.usuario.username}'



class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=45)
    Descripcion = models.CharField(max_length=45)
    Precio = models.FloatField()
    Stock = models.FloatField()
    Marca = models.CharField(max_length=45)

    def __str__(self):
        return self.Nombre


class Venta(models.Model):
    METODO_PAGO_OPCIONES = [
        ('Efectivo', 'Efectivo'),
        ('Tarjeta Débito', 'Tarjeta Débito'),
        ('Tarjeta Crédito', 'Tarjeta Crédito'),
        ('Transferencia', 'Transferencia'),
    ]

    idVentas = models.AutoField(primary_key=True)
    Fecha_hora_venta = models.DateTimeField(default=timezone.now)
    Garantias = models.CharField(max_length=30)
    Productos = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Precio_uni = models.FloatField()
    Cantidad_vendida = models.FloatField()
    Metodo_pago = models.CharField(max_length=50, choices=METODO_PAGO_OPCIONES)
    Total_venta = models.FloatField(blank=True, null=True)
    VENT_AtGral = models.CharField(max_length=45)

    def calcular_total(self):
        return self.Precio_uni * self.Cantidad_vendida

    def save(self, *args, **kwargs):
        # Calculamos el total de la venta antes de guardarla
        self.Total_venta = self.calcular_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Venta {self.idVentas} - Total: {self.Total_venta}'


class Compra(models.Model):
    idCompras = models.AutoField(primary_key=True)
    Fecha_hora_compra = models.DateTimeField()
    Nro_Compra = models.IntegerField()
    Metodo_pago = models.CharField(max_length=50)
    Producto = models.CharField(max_length=50)
    Precio = models.FloatField()
    Cantidad = models.FloatField()
    Total_compra = models.FloatField()
    id_proveedor = models.IntegerField()

    def __str__(self):
        return f'Compra {self.idCompras}'


class DetalleVenta(models.Model):
    id_DetVta = models.AutoField(primary_key=True)
    idVentas = models.ForeignKey(Venta, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Cant_vendida = models.CharField(max_length=45)
    Prec_uni = models.FloatField()

    def __str__(self):
        return f'Detalle Venta {self.id_DetVta}'


class DetalleCompra(models.Model):
    id_DetCompra = models.AutoField(primary_key=True)
    idCompra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Cant_Comprada = models.CharField(max_length=45)
    Prec_uni = models.FloatField()

    def __str__(self):
        return f'Detalle Compra {self.id_DetCompra}'


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    CUIT = models.IntegerField()
    Telefono = models.IntegerField()
    Correo = models.CharField(max_length=45)
    Domicilio = models.CharField(max_length=45)
    Nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.Nombre


class ProdProv(models.Model):
    id_prod_prov = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return f'Prod_Prov {self.id_prod_prov}'



