from django.views import generic
from .models import Order

class IndexView(generic.ListView):
    template_name = "taxi/index.html"
    context_object_name = "latest_orders"

    def get_queryset(self):
        return Order.objects.all()[:5]

class DetailView(generic.DetailView):
    model = Order
    template_name = "taxi/detail.html"
    context_object_name = "order"
    pk_url_kwarg = "order_id" 