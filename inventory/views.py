from django.views.generic import CreateView, UpdateView, TemplateView, DeleteView
from django.urls import reverse_lazy
from .models import Food, Gadget
from .forms import FoodForm, GadgetForm

# Create your views here.


class HomeListView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['foods'] = Food.objects.all()  # Fetch all Food items
        context['gadgets'] = Gadget.objects.all()  # Fetch all Gadget items
        return context


class FoodCreateView(CreateView):
    model = Food
    form_class = FoodForm
    template_name = 'food_form.html'
    success_url = reverse_lazy('home')


class FoodUpdateView(UpdateView):
    model = Food
    form_class = FoodForm
    template_name = 'food_form.html'
    success_url = reverse_lazy('home')


class FoodDeleteView(DeleteView):
    model = Food
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('home')


class GadgetCreateView(CreateView):
    model = Gadget
    form_class = GadgetForm
    template_name = 'gadget_form.html'
    success_url = reverse_lazy('home')


class GadgetUpdateView(UpdateView):
    model = Gadget
    form_class = GadgetForm
    template_name = 'gadget_form.html'
    success_url = reverse_lazy('home')


class GadgetDeleteView(DeleteView):
    model = Gadget
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('home')

