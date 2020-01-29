# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, DeleteView, TemplateView

from catalogue.forms import ProductForm, PurchaseForm, ReturnForm
from catalogue.models import Product, Purchase, Return
from authenicate.models import MyUser


class Products(ListView):
    model = Product
    template_name = 'list/index.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context.update({
            'buy_form': PurchaseForm
        })
        return context


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    http_method_names = ['get', 'post']
    success_url = '/create/'
    form_class = ProductForm
    template_name = 'list/create.html'


class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    http_method_names = ['post']
    success_url = '/'


class PurchaseCreate(LoginRequiredMixin, CreateView):
    model = Purchase
    http_method_names = ['post']
    success_url = '/'
    form_class = PurchaseForm
    template_name = 'list/purchase_create.html'

    def form_valid(self, form):
        form_add = form.save(commit=False)
        form_add.buyer_id = self.request.user.pk
        form_add.product_id = self.kwargs['pk']
        form_add.total_cost = form.instance.product.price * form.cleaned_data['quantity']
        user = MyUser.objects.get(pk=form_add.buyer_id)
        user.cash -= form_add.total_cost
        product = Product.objects.get(pk=form_add.product_id)
        product.storage -= form.cleaned_data['quantity']

        def purchase_valid():
            if product.storage < form.cleaned_data['quantity'] and user.cash < form_add.total_cost:
                return True
            return False

        if purchase_valid():
            return redirect('purchase_error')

        user.save()
        product.save()
        return super().form_valid(form)


class PurchaseError(TemplateView):
    template_name = 'list/purchase_error.html'


class PurchaseList(ListView):
    model = Purchase
    context_object_name = 'purchases'
    template_name = 'list/purchase_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context.update({
            'return_form': ReturnForm
        })
        return context


class ReturnCreate(CreateView):
    success_url = '/purchase/list/'
    template_name = 'list/return_create.html'
    form_class = ReturnForm

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
