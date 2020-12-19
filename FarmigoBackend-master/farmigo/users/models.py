from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class BaseUser(AbstractUser):
    USER_TYPE = (
        ('FMR', 'Farmer'),
        ('SPL', 'Supplier'),
        ('RTL', 'Retailer'),
    )
    user_type = models.CharField(max_length=3, choices=USER_TYPE, default='FMR', null=True, blank=True)
    username = models.CharField(max_length=10, null=False, blank=False, unique=True,default='Mobile Number')
    mobnumber = models.CharField(max_length=10, unique=True,default='Mobile Number')
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64,default='Address')
    district = models.CharField(max_length=64,default='District')
    state = models.CharField(max_length=32,default='State')

    def save(self, *args, **kwargs):
        self.username = self.mobnumber
        super(BaseUser, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "BaseUser"
        verbose_name_plural = "BaseUsers"

    def __str__(self):
        return self.username


class Farmer(models.Model):
    baseuser = models.OneToOneField(BaseUser, related_name='farmer', on_delete=models.CASCADE)
    op_land_area = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    first_name = models.CharField(max_length=1, null=True, blank=True)
    last_name = models.CharField(max_length=1, null=True, blank=True)

    def __str__(self):
        return self.baseuser.name

class Crop(models.Model):
    farmer = models.ForeignKey(Farmer, related_name="crop", on_delete=models.CASCADE)
    crop_name = models.CharField(max_length=32)
    crop_type = models.CharField(max_length=32)

    def __str__(self):
        return self.crop_name

class FarmerProduct(models.Model):
    PRODUCT_TYPE = (
        ('CP', 'Crop Product'),
        ('AP', 'Animal Product'),
    )
    PRODUCT_NAME = (
        ('PDY', 'Paddy'),
        ('MZE', 'Maize'),
        ('WHT', 'Wheat'),
        ('JWR', 'Jowar'),
        ('GRN', 'Groundnut'),
        ('GRM', 'Gram'),
        ('RCE', 'Rice'),
        ('BRL', 'Barley'),
    )
    farmer = models.ForeignKey(Farmer, related_name="farmer_product", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=32)
    quality_index = models.DecimalField(max_digits=4, decimal_places=2)
    product_type = models.CharField(max_length=3, choices=PRODUCT_TYPE, default='CP')

    def __str__(self):
        return self.product_name

class Livestock(models.Model):
    LIVESTOCKS = (
        ('COW', 'COW'),
        ('SHEEP', 'SHEEP'),
        ('GOAT', 'GOAT'),
        ('HEN', 'HEN'),
    )
    farmer = models.ForeignKey(Farmer, related_name="livestock", on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    number = models.IntegerField()

    def __str__(self):
        return self.name


#Retailer
class Retailer(models.Model):
    baseuser = models.OneToOneField(BaseUser, related_name='retailer', on_delete=models.CASCADE)
    description = models.CharField(max_length=512)
    def __str__(self):
        return self.name


class RetailerProduct(models.Model):
    PRODUCT_TYPE = (
        ('CP', 'Crop Product'),
        ('AP', 'Animal Product'),
    )
    retailer = models.ForeignKey(Retailer, related_name='retailer_product', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=32)
    product_price = models.FloatField()
    product_type = models.CharField(max_length=3, choices=PRODUCT_TYPE, default='CP')
    def __str__(self):
        return self.product_name


#Supplier
class Supplier(models.Model):
    baseuser = models.ForeignKey(BaseUser, related_name='supplier', on_delete=models.CASCADE)
    description = models.CharField(max_length=512)
    def __str__(self):
        return self.name

class SupplierProduct(models.Model):
    supplier = models.ForeignKey(Supplier, related_name='supplier_product', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=32)
    product_price = models.FloatField()
    
    def __str__(self):
        return self.product_name



