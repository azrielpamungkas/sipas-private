from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from .forms import CustomUserCreationFrom, NewPassword
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView

from django.db.models import Q  # new


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from django.shortcuts import render

# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"


class SignUpView(LoginRequiredMixin, CreateView):
    form_class = CustomUserCreationFrom
    success_url = reverse_lazy("admin-list")
    template_name = "auth/signup.html"


class UserListView(LoginRequiredMixin, ListView):
    model = User
    paginate_by = 5
    template_name = "archive/admin_list.html"


class SearchUser(LoginRequiredMixin, ListView):
    model = User
    paginate_by = 5
    template_name = "archive/admin_list.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = self.model.objects.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(username__icontains=query)
        )
        return object_list


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ["first_name", "last_name", "username", "email"]
    success_url = reverse_lazy("admin-list")


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy("admin-list")


from django.http import HttpResponse


class ResetAdminPassword(LoginRequiredMixin, View):
    def setup(self, request, *args, **kwargs):
        self.pk = kwargs["pk"]
        self.user_target = User.objects.get(pk=self.pk)
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        user = self.user_target
        user.set_password("8semarang")
        user.last_login = None
        user.save()
        return HttpResponseRedirect(reverse("admin-list"))


@login_required
def new_password(request):
    user_instance = get_object_or_404(User, pk=request.user.id)
    if request.user.last_login == None:
        if request.method == "POST":
            form = NewPassword(request.POST)
            if form.is_valid():
                user_instance.set_password(form.cleaned_data["password"])
                user_instance.save()
                return HttpResponseRedirect(reverse("admin-list"))
            else:
                print("Form not valid")
        else:
            form = NewPassword()
        return render(request, "auth/new_password.html", {"form": form})
    return HttpResponseRedirect(reverse("admin-list"))
