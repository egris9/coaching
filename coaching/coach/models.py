from django.db import models
from django.contrib.auth.models import User

import random

def generate_random_id():
    return random.randint(10000, 99999)  # Adjust the range as needed



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    class Type(models.TextChoices):
        Client = 'client'
        Coache = 'coach'

    def __str__(self):
        return self.type
    type = models.CharField(max_length=7, choices=Type.choices, default=Type.Client)



class Training_session(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    Profile = models.OneToOneField(User, on_delete=models.CASCADE, default=generate_random_id())
    img = models.ImageField(upload_to="sessions/%y/%m/%d", null=True)
    start_time = models.DateTimeField(null=True)    
    end_time = models.DateTimeField(null=True)   
    location = models.CharField(max_length=100,null=True)
    participant_limit = models.IntegerField(null=True)
    

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Training_session, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)




class Product(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(null=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, null=True)
    product_of_the_week = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - Id {self.id}"

class ProductImages(models.Model):
    id = models.AutoField(primary_key=True)
    urls = models.ImageField(upload_to="products/%y/%m/%d")
    type = models.CharField(max_length=50)

    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    #convertir un objet en chaîne de caractères
    def __str__(self):
        return f"{self.product.name} - Image {self.urls}"
    

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_name = models.CharField(max_length=255)
    exp = models.DateField()
    cvv = models.CharField(max_length=4)

    product = models.ManyToManyField(Product, through="OrderToProduct")

    def __str__(self):
        return f"Order {self.id} - {self.first_name} {self.last_name} - Total: {self.order_total}"

class OrderToProduct(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey("Order", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price=models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Order {self.order_id} - {self.product_name} - Quantity {self.quantity}"

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart {self.id} - Total: {self.total}"

class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    cart_id = models.ForeignKey("Cart", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    #chose what to display in admin 
    def __str__(self):
        return f"CartItem {self.id} - Product id {self.product.id} - Quantity: {self.quantity} - Price: {self.price}"

