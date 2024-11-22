from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)  # Optional description
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Optional price
    availability = models.BooleanField(default=True)  # Indicates if the product is available
    quantity = models.IntegerField(default=0, blank=True)  # Optional field for inventory quantity
    delivery_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Optional delivery price


    # Fields specific to dry fruits and nuts
    origin = models.CharField(max_length=255, blank=True)  # e.g., country of origin
    storage_instructions = models.TextField(blank=True)  # Storage instructions (dry, cool place, etc.)
    packaging = models.CharField(max_length=255, blank=True)  # Packaging type (e.g., airtight, sealed, etc.)

    # Fields specific to perfumes and attars
    fragrance_type = models.CharField(max_length=255, blank=True)  # E.g., floral, woody, spicy
    volume = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # Volume in ml
    ingredients = models.TextField(blank=True)  # List of ingredients

    # Fields specific to dress/body washing/cleaning items
    brand = models.CharField(max_length=255, blank=True)  # Brand name
    fragrance = models.CharField(max_length=255, blank=True)  # Fragrance type (optional)
    usage_instructions = models.TextField(blank=True)  # How to use the product (optional)
    
    
    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f"Image for {self.product.name}"



