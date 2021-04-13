from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from eshop_cart.forms import CartAddProductForm
from eshop_products.models import Product, ProductGallery, MainTopSlider
from eshop_products_category.models import ProductCategory


class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.all()


def products_categories_partial(request):
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'products/products_categories_partial.html', context)


class ProductsListByCategory(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 2

    def get_queryset(self,category_slug=None):
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(name__iexact=category_name, slug=category_slug)
        if category is None:
            raise Http404('صفحه ی مورد نظر یافت نشد')
        return Product.objects.get_products_by_category(category_name)


class SearchProductsView(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 4

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.get_active_products()


def product_detail(request, *args, **kwargs):
    selected_product_id = kwargs['productId']
    product = Product.objects.get_by_id(selected_product_id)
    if product is None or not product.available:
        raise ("not valid")

    related_product_pictures = ProductGallery.objects.filter(product_id=selected_product_id)
    pictures = MainTopSlider.objects.all()
    cart_form= CartAddProductForm()

    context = {
        'product': product,
        'related_product_pictures': related_product_pictures,
        "pictures": pictures,
        'cart_form': cart_form

    }
    return render(request, 'products/product_detail.html', context)
