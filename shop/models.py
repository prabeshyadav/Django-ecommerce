from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField;
    product_name=models.CharField(max_length=10);
    price= models.DecimalField(max_digits=10, decimal_places=2)

    category= models.CharField(max_length=50,default='');
    subcaregory= models.CharField(max_length=50,default='');
    desc=models.CharField(max_length=50);
    pub_date=models.DateField();
    image= models.ImageField(upload_to='shop/image',default='')

    def __str__(self):
        return self.product_name
    
    