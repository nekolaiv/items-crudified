from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Item, Table
from .forms import ItemForm, TableForm

# Create your views here.


# -------------------- TABLE VIEWS --------------------

from django.http import JsonResponse


class TableAndItemView(ListView):
    model = Table
    template_name = "table_view.html"
    context_object_name = "tables"

    def get_queryset(self):
        """Fetch all tables to be listed in the aside section."""
        return Table.objects.all()

    def get_context_data(self, **kwargs):
        """Prepare context data for rendering the selected table and its items."""
        context = super().get_context_data(**kwargs)

        table_id = self.request.GET.get("table_id")
        selected_table = get_object_or_404(
            Table, id=table_id) if table_id else None
        items = selected_table.items.all() if selected_table else None

        context["selected_table"] = selected_table
        context["items"] = items  # Items belonging to the selected table
        return context

    def get(self, request, *args, **kwargs):
        """Handles AJAX search filtering and normal GET requests."""
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            table_id = request.GET.get('table_id')
            query = request.GET.get('q', '').strip()

            if table_id and query:
                selected_table = get_object_or_404(Table, id=table_id)
                items = list(selected_table.items.filter(
                    name__icontains=query).values('id', 'name', 'price'))
                return JsonResponse({'items': items})

            return JsonResponse({'items': []})  # Return empty if no query

        return super().get(request, *args, **kwargs)  # Normal page load


class TableCreateView(CreateView):
    model = Table
    form_class = TableForm
    template_name = "table_form.html"
    success_url = reverse_lazy("table_view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tables"] = Table.objects.all()
        return context


class TableDeleteView(DeleteView):
    model = Table
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("table_")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tables"] = Table.objects.all()
        return context

# -------------------- ITEM VIEWS --------------------


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = "item_form.html"

    def form_valid(self, form):
        form.instance.table = get_object_or_404(
            Table, id=self.kwargs["table_id"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tables"] = Table.objects.all()
        return context

    def get_success_url(self):
        return reverse("table_view") + f"?table_id={self.kwargs['table_id']}"


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = "item_form.html"
    fields = ["name", "description", "price"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tables"] = Table.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy("item_list", kwargs={"table_id": self.object.table.id})


class ItemDeleteView(DeleteView):
    model = Item
    template_name = "confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tables"] = Table.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy("item_list", kwargs={"table_id": self.object.table.id})
