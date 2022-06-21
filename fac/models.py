from django.db import models
from bases.models import ClaseModelo, ClaseModelo2
from inv.models import Producto
#para los signals
from django.db.models.signals import post_save   #post_save -> para vigilar un modelo despues de haberse guadado y el post_delete vigila despus de haberse eliminado
from django.dispatch import receiver
from django.db.models import Sum

class Cliente(ClaseModelo):
    NAT = 'Natural' 
    JUR = 'Juridica'

    TIPO_CLIENTE = [
        (NAT,'Natural'),
        (JUR,'Juridica'),
    ]  

    nombres = models.CharField(
        max_length=100
    )
    apellidos = models.CharField(
        max_length=100
    )
    celular = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    tipo=models.CharField(
        max_length=10,
        choices=TIPO_CLIENTE,
        default=NAT
    )

    def __str__(self):
        return '{} {}'.format(self.apellidos, self.nombres) 

    def save(self):
        self.nombres = self.nombres.upper()
        self.apellidos = self.apellidos.upper()
        super(Cliente, self).save()

    class Meta:
        verbose_name_plural = 'Clientes'

class FacturaEnc(ClaseModelo2):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)
    
    def __str__(self):
        return self.id

    def save(self):
        self.total = self.sub_total - self.descuento
        super(FacturaEnc, self).save()
    
    class Meta:
        verbose_name = 'Encabezado Factura'
        verbose_name_plural = 'Encabezado Facturas'
        permissions = [
            ('sup_caja_facturaenc','Permisos de Supervisor de Caja Encaezado')
        ]


class FacturaDet(ClaseModelo2):
    factura = models.ForeignKey(FacturaEnc, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.BigIntegerField(default=0)
    precio = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return self.producto
    
    def save(self):
        self.sub_total = float(float(int(self.cantidad))*float(self.precio))
        self.total = self.sub_total - float(self.descuento)
        super(FacturaDet, self).save()

    class Meta:
        verbose_name = 'Detalle Factura'
        verbose_name_plural = 'Detalle Facturas'
        permissions = [
            ('sup_caja_facturadet','Permisos de Supervisor de Caja Detalle')
        ]

@receiver(post_save, sender=FacturaDet)
def detalle_fac_guardar(sender, instance, **kwargs):
    factura_id = instance.factura.id
    producto_id = instance.producto.id

    enc = FacturaEnc.objects.get(pk=factura_id)
    if enc:
        sub_total = FacturaDet.objects.filter(factura=factura_id).aggregate(sub_total=Sum('sub_total')).get('sub_total',0)
        descuento = FacturaDet.objects.filter(factura=factura_id).aggregate(descuento=Sum('descuento')).get('descuento',0)
        # print(sub_total)
        # print(descuento)
        # if sub_total['sub_total__sum']==None and descuento['descuento__sum']==None:
        #     sub_total['sub_total__sum']=0
        #     descuento['descuento__sum']=0
        enc.sub_total = sub_total
        enc.descuento = descuento
        enc.save()
    
    prod = Producto.objects.filter(pk=producto_id).first()
    if prod:
        cantidad = int(prod.existencia) - int(instance.cantidad)
        prod.existencia = cantidad
        prod.save()
