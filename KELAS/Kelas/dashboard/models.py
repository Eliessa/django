from email.policy import default
from pyexpat import model
from django.db import models
from sqlalchemy import null, true

# Create your models here.
class Jenis(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()
    
    def __str__(self):
        return self.nama
        
class Barang(models.Model):
    kodebrg=models.CharField(max_length=8, default="BRG")
    nama=models.CharField(max_length=50)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    link_gbr=models.CharField(max_length=150, blank=True)
    waktu_posting=models.DateTimeField(auto_now_add=True)
    jenis_id=models.ForeignKey(Jenis,on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return "{} | {} | {}".format(self.kodebrg,self.nama,self.harga)

class Transaksi(models.Model):
    kodetrans=models.CharField(max_length=10, default="TR")
    tgltrans=models.DateTimeField(auto_now_add=True)
    total=models.BigIntegerField()
    
    def __str__(self):
        return self.kodetrans

class DetailTransaksi(models.Model):
    kodetrans=models.CharField(max_length=10)
    kodebrg=models.CharField(max_length=8)
    qty=models.IntegerField()
    subtotal=models.BigIntegerField()
    
    def __str__(self):
        return "{}. {}".format(self.kodetrans,self.kodebrg)

class ItemModel(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 80, blank = False)
    price = models.IntegerField
 
    class Meta:
        ordering = ['name']
 
    def __str__(self):
        return f"{self.name}:{self.price}"
    
    