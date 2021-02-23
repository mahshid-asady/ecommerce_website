from django.shortcuts import render

# Create your views here.
from eshop_products.models import MainTopSlider, Product,ProductCategory
from site_settings.models import MainLogo,SocialLinks


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def home(request):
    slides = MainTopSlider.objects.all()
    latest_products = Product.objects.order_by('-id').all()[:8]
    sample_product_category= Product.objects.get_products_by_category(category_name='laptop').last()
    sample_product_category1 = Product.objects.get_products_by_category(category_name='mobile').last()
    sample_product_category2 = Product.objects.get_products_by_category(category_name='digital').last()
    most_visit_products= Product.objects.order_by('-visit_count').all()
    discount_products= Product.objects.filter(discount=True).all()[:2]




    context = {
        'slides': slides,
        'latest_products': latest_products,
        'sample_product_category': sample_product_category,
        'sample_product_category1':sample_product_category1,
        'sample_product_category2':sample_product_category2,
        'most_visit_products':most_visit_products,
        'discount_products':discount_products,



    }
    return render(request, 'home.html',context)


def header(request):
    logo = MainLogo.objects.first()

    context = {
        'logo': logo,
    }
    return render(request, 'shared/Header.html', context)


def privacy(request):
    return render(request, 'privacy_policy.html')


def faq(request):
    return render(request, 'faq.html')


def coming_soon(request):
    return render(request, 'coming_soon.html')


def footer_partial(request):

    social= SocialLinks.objects.first()

    context= {

        'social': social,




    }
    return render(request, 'shared/Footer.html', context)