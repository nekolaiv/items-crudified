from inventory.models import Table, Item  # Adjust based on your app structure
from django.views import View
from django.db import connection
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Item, Table
from .forms import ItemForm, TableForm

# Create your views here.


# -------------------- TABLE VIEWS --------------------


class TableAndItemView(ListView):
    model = Table
    template_name = "table_view.html"
    context_object_name = "tables"

    def get_queryset(self):
        return Table.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        table_id = self.request.GET.get("table_id")
        selected_table = get_object_or_404(
            Table, id=table_id) if table_id else None
        items = selected_table.items.all() if selected_table else None

        context["selected_table"] = selected_table
        context["items"] = items
        return context

    def get(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            table_id = request.GET.get('table_id')
            query = request.GET.get('q', '').strip()

            selected_table = get_object_or_404(Table, id=table_id)
            items = selected_table.items.all()

            if query:
                items = items.filter(name__icontains=query)

            items_list = list(items.values('id', 'name', 'price'))
            return JsonResponse({'items': items_list})

        return super().get(request, *args, **kwargs)


class TableCreateView(CreateView):
    model = Table
    form_class = TableForm
    template_name = "table_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tables"] = Table.objects.all()
        return context

    def get_success_url(self):
        return reverse("table_view") + f"?table_id={self.object.id}"


class TableUpdateView(UpdateView):
    model = Table
    form_class = TableForm
    template_name = "table_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tables"] = Table.objects.all()
        context["selected_table"] = get_object_or_404(
            Table, id=self.kwargs["pk"])
        return context

    def get_success_url(self):
        return reverse("table_view") + f"?table_id={self.object.id}"


class TableDeleteView(DeleteView):
    model = Table
    template_name = "confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tables"] = Table.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            table_id = self.kwargs.get("table_id", self.get_object().id)
            return redirect(reverse("table_view") + f"?table_id={table_id}")

        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("table_view")

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
        context["selected_table"] = get_object_or_404(
            Table, id=self.kwargs["table_id"])
        return context

    def get_success_url(self):
        return reverse("table_view") + f"?table_id={self.kwargs['table_id']}"


class ItemUpdateView(UpdateView):
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
        context["selected_table"] = get_object_or_404(
            Table, id=self.kwargs["table_id"])
        return context

    def get_success_url(self):
        return reverse("table_view") + f"?table_id={self.kwargs['table_id']}"


class ItemDeleteView(DeleteView):
    model = Item
    template_name = "confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tables"] = Table.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            table_id = self.kwargs.get("table_id", self.get_object().table.id)
            return redirect(reverse("table_view") + f"?table_id={table_id}")

        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("table_view") + f"?table_id={self.kwargs['table_id']}"


# -------------------- ITEM VIEWS --------------------


class TruncateTableView(View):
    template_name = "confirm_truncate.html"

    def get(self, request):
        return render(request, self.template_name, {"object_type": "tables"})

    def post(self, request):
        if "confirm" in request.POST:
            Item.objects.filter(table__isnull=False).delete()
            Table.objects.all().delete()
            return redirect(reverse("table_view"))

        return redirect(reverse("table_view"))


class TruncateTableView(View):
    template_name = "confirm_truncate.html"

    def get(self, request):
        return render(request, self.template_name, {"object_type": "tables"})

    def post(self, request):
        if "confirm" in request.POST:
            Item.objects.filter(table__isnull=False).delete()
            Table.objects.all().delete()
            return redirect(reverse("table_view"))

        return redirect(reverse("table_view"))


class TruncateItemView(View):
    template_name = "confirm_truncate.html"

    def get(self, request):
        return render(request, self.template_name, {"object_type": "items"})

    def post(self, request):
        if "confirm" in request.POST:
            Item.objects.all().delete()
            return redirect(reverse("table_view"))

        return redirect(reverse("table_view"))
