from django.contrib import admin
from .models import Customer, Product, Order, OrderItem

# Customize the admin panel for the Customer model


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

# Customize the admin panel for the Product model


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'digital', 'image', 'category')
    list_filter = ('category',)
    search_fields = ('name',)

    actions = ['set_category_school', 'set_category_online']

    def set_category_school(self, request, queryset):
        queryset.update(category='School Product')

    def set_category_online(self, request, queryset):
        queryset.update(category='Online Product')

    set_category_school.short_description = "Set category to School Product"
    set_category_online.short_description = "Set category to Online Product"
# Create an inline admin for OrderItem to display within the Order admin


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

# Customize the admin panel for the Order model


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date_ordered', 'complete', 'transaction_id')
    list_filter = ('complete', 'date_ordered')
    inlines = [OrderItemInline]

# Customize the admin panel for the OrderItem model


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity', 'date_added')

# Customize the admin panel for the ShippingAddress model
