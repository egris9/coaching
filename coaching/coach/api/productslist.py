from django.http import JsonResponse
from coach.models import Product

def product_list(request):
    products = Product.objects.all().values('id', 'name', 'description')
    return JsonResponse(list(products), safe=False)
