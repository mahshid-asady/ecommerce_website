from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
# Create your views here.
from eshop_cart.forms import CartAddProductForm
from eshop_comment.forms import CommentForm
from eshop_comment.models import Comment
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
    if product is None or not product.active:
        raise ("not valid")

    comments =product.comments.filter(active=True, parent__isnull=True)
    new_comment=None
    if request.method == 'POST':
        # comment has been added
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None
            # get parent comment id from hidden input
            try:
                # id integer e.g. 15
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            # if parent_id has been submitted get parent_obj id
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                # if parent object exist
                if parent_obj:
                    # create replay comment object
                    replay_comment = comment_form.save(commit=False)
                    # assign parent_obj to replay comment
                    replay_comment.parent = parent_obj
            # normal comment
            # create comment object but do not save to database
            new_comment = comment_form.save(commit=False)
            # assign ship to the comment
            new_comment.product = product
            # save
            new_comment.save()

    else:
        comment_form = CommentForm()
    cart_form= CartAddProductForm()

    context = {
        'product': product,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'cart_form': cart_form

    }
    return render(request, 'products/product_detail.html', context)
