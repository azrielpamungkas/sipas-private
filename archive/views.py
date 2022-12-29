from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q  # new

from .models import IncomingMail, OutgoingMail

# Create your views here.
class IncomingMailListView(LoginRequiredMixin, ListView):
    model = IncomingMail
    paginate_by = 4
    template_name = "incoming/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(IncomingMailListView, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

class IncomingSearch(LoginRequiredMixin, ListView):
    model = IncomingMail
    paginate_by=4
    template_name = "incoming/index.html"
    

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = self.model.objects.filter(
            Q(id_mail__icontains=query)
            | Q(id_enter__icontains=query)
            | Q(sender__icontains=query)
            | Q(date__icontains=query)
            | Q(regarding__icontains=query)
        )
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super(IncomingSearch, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['query'] = self.request.GET.get('q')
        return context

class IncomingMailDetailView(LoginRequiredMixin, DetailView):
    model = IncomingMail
    template_name = "incoming/detail.html"


class IncomingMailCreateView(LoginRequiredMixin, CreateView):
    model = IncomingMail
    fields = "__all__"


class IncomingMailUpdateView(LoginRequiredMixin, UpdateView):
    model = IncomingMail
    fields = "__all__"


class IncomingMailDeleteView(LoginRequiredMixin, DeleteView):
    model = IncomingMail
    success_url = reverse_lazy("incoming-mail-list")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class OutgoingMailListView(LoginRequiredMixin, ListView):
    model = OutgoingMail
    paginate_by = 4
    template_name = "outgoing/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(OutgoingMailListView, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

class OutgoingSearch(LoginRequiredMixin, ListView):
    model = OutgoingMail
    template_name = "outgoing/index.html"
    paginate_by = 4


    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = self.model.objects.filter(
            Q(id_mail__icontains=query)
            | Q(date__icontains=query)
            | Q(to_send__icontains=query)
            | Q(regarding__icontains=query)
        )
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super(OutgoingSearch, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['query'] = self.request.GET.get('q')
        return context

class OutgoingMailDetailView(LoginRequiredMixin, DetailView):
    model = OutgoingMail
    template_name = "outgoing/detail.html"


class OutgoingMailCreateView(LoginRequiredMixin, CreateView):
    model = OutgoingMail
    fields = "__all__"


class OutgoingMailUpdateView(LoginRequiredMixin, UpdateView):
    model = OutgoingMail
    fields = "__all__"


class OutgoingMailDeleteView(DeleteView):
    model = OutgoingMail
    success_url = reverse_lazy("outgoing-mail-list")


incoming_list = IncomingMailListView.as_view()
incoming_search = IncomingSearch.as_view()
incoming_detail = IncomingMailDetailView.as_view()
incoming_create = IncomingMailCreateView.as_view()
incoming_update = IncomingMailUpdateView.as_view()
incoming_delete = IncomingMailDeleteView.as_view()

outgoing_list = OutgoingMailListView.as_view()
outgoing_search = OutgoingSearch.as_view()
outgoing_detail = OutgoingMailDetailView.as_view()
outgoing_create = OutgoingMailCreateView.as_view()
outgoing_update = OutgoingMailUpdateView.as_view()
outgoing_delete = OutgoingMailDeleteView.as_view()
