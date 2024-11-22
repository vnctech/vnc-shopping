from django.contrib import admin
from .models import Category, Subcategory, Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Number of empty forms to display

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'subcategory', 'price', 'availability', 'quantity')
    list_filter = ('category', 'subcategory', 'availability')
    search_fields = ('name', 'category__name', 'subcategory__name')
    ordering = ('name',)
    inlines = [ProductImageInline]
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'category', 'subcategory', 'price', 'availability', 'quantity', 'delivery_price')
        }),
        ('Dry Fruits and Nuts', {
            'fields': ('origin', 'storage_instructions', 'packaging')
        }),
        ('Perfumes and Attars', {
            'fields': ('fragrance_type', 'volume', 'ingredients')
        }),
        ('Dress/Body Wash/Cleaning Items', {
            'fields': ('brand', 'fragrance', 'usage_instructions')
        }),
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
    search_fields = ('product__name',)

# Registering models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
