from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Item, Table
from .forms import ItemForm, TableForm

# Create your views here.


# -------------------- TABLE VIEWS --------------------

class TableAndItemView(ListView):
    model = Table  # Base model to allow ListView usage
    template_name = "home.html"
    context_object_name = "tables"

    def get_queryset(self):
        return Table.objects.all()  # Get all tables for the aside section

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        table_id = self.request.GET.get("table_id")
        query = self.request.GET.get("q", "").strip()

        selected_table = None
        items = None

        if table_id:
            selected_table = get_object_or_404(Table, id=table_id)
            items = selected_table.items.all()

            # Apply search filter only if a query is provided
            if query:
                items = items.filter(name__icontains=query)

        context["selected_table"] = selected_table
        context["items"] = items  # Filtered items in the selected table
        # Keep search query for the input field
        context["search_query"] = query

        return context


class TableCreateView(CreateView):
    model = Table
    template_name = TableForm
    fields = ["name"]
    success_url = reverse_lazy("table_list")


# class TableDetailView(DetailView):
#     model = Table
#     template_name = "tables/table_detail.html"
#     context_object_name = "table"


class TableDeleteView(DeleteView):
    model = Table
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("table_list")

# -------------------- ITEM VIEWS --------------------


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = "item_form.html"

    def form_valid(self, form):
        form.instance.table = get_object_or_404(
            Table, id=self.kwargs["table_id"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("home") + f"?table_id={self.kwargs['table_id']}"


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = "item_form.html"
    fields = ["name", "description", "price"]

    def get_success_url(self):
        return reverse_lazy("item_list", kwargs={"table_id": self.object.table.id})


class ItemDeleteView(DeleteView):
    model = Item
    template_name = "confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("item_list", kwargs={"table_id": self.object.table.id})
