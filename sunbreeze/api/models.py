from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
#from django_countries.fields import CountryField

# Create your models here.

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)

class i_stock(models.Model):
    title = models.CharField(default= "" , max_length=100)
    price = models.FloatField(default=0)
    slug = models.SlugField(default="")
    quantity = models.IntegerField(default=1)
    description = models.TextField(default="")
    image = models.ImageField(upload_to='pictures/%Y/%m/%d', max_length=255)
  
    def __str__(self):
        return self.title

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True, blank=True)
	email = models.CharField(max_length=200, null=True, blank=True)
	device = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		if self.name:
			name = self.name
		else:
			name = self.device
		return str(name)

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total