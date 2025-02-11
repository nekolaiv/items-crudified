from django.views.generic import CreateView, UpdateView, TemplateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Food
from .forms import FoodForm

# Create your views here.


class HomeListView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['foods'] = Food.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            query = request.GET.get('q', '')
            foods = list(Food.objects.filter(
                name__icontains=query).values('id', 'name', 'price'))
            return JsonResponse({'foods': foods})

        return super().get(request, *args, **kwargs)


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
