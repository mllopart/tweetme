from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
                                  DetailView,
                                  ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )

from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Tweet


# Create #########################

class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    #success_url = reverse_lazy("tweet:detail")
    login_url = "/admin/"

    # def form_valid(self, form):
    #     if self.request.user.is_authenticated():
    #         form.instance.user = self.request.user
    #         return super(TweetCreateView, self).form_valid(form)
    #     else:
    #         form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue"])
    #         return self.form_invalid(form)


# Retrieve #########################

class TweetDetailView(DetailView):
    template_name = "tweets/detail_view.html"
    queryset =Tweet.objects.all()

class TweetListView(ListView):

    template_name = "tweets/list_view.html"

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q", None)

        if query is not None:
            qs = qs.filter(
                           Q(content__icontains=query) |
                           Q(user__username__icontains=query)
                           )

        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        # print(context)
        return context

# Update #########################

class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset =Tweet.objects.all()
    form_class = TweetModelForm
    #success_url = reverse_lazy("tweet:list")
    template_name = 'tweets/update_view.html'

# Delete #########################

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model =Tweet
    success_url = reverse_lazy("tweet:list")
    template_name = 'tweets/delete_view.html'
