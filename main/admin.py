from django.contrib import admin
from .models import Category, Size, Product, ProductImage, ProductSize


class ProductImageInline(admin.TabularInline):
    # для того чтобы в админке выводить эту модель вместе с моделью продуктов
    model = ProductImage
    # extra = 1 одно поле, можно 5 10 и тд
    extra = 1


class ProductSizeInline(admin.TabularInline):
    # для того чтобы в админке выводить эту модель вместе с моделью продуктов
    model = ProductSize
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    # что мы будем видеть при списке продуктов
    list_display = ["name", "category", "color", "price"]
    # поля по которым можно производить фильтрацию
    list_filter = ["category", "color"]
    # поля по которым будет происходить поиск
    search_fields = ["name", "color", "description"]
    # поля которые позволяют заполнять параметры из тех параметров которые
    #  уже есть в данном случае удобно читаемая ссылка
    prepopulated_fields = {"slug": ("name",)}
    # что показывать дополнительно на странице товара
    inlines = [ProductImageInline, ProductSizeInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


class SizeAdmin(admin.ModelAdmin):
    list_display = ["name"]


# теперь зарегистрируем, можно либо с помощью декоратора либо с помощью admin.site.register
admin.site.register(Category, CategoryAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Product, ProductAdmin)
