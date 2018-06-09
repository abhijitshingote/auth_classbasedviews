from django.shortcuts import render
from django.views.generic import (TemplateView,
	ListView,
	DetailView,
	CreateView,
	UpdateView)
from .models import Authorization
# Create your views here.

class AuthListView(ListView):
	model=Authorization

class AuthDetailView(DetailView):
	model=Authorization

class AuthCreateView(CreateView):
	model=Authorization
	fields= [
		'authorizationid',
		'memberid',
		'ndc_no',
		'startdate',
		'enddate'

	]

	def form_valid(self, form):
		form.instance.createdby = self.request.user
		return super().form_valid(form)


class AuthUpdateView(UpdateView):
	model=Authorization
	template_name_suffix = '_update_form'
	fields= [
		'authorizationid',
		'memberid',
		'ndc_no'


	]

	def form_valid(self, form):
		form.instance.updatedby = self.request.user
		return super().form_valid(form)
