from django.shortcuts import render, redirect

from .models import Company
# Create your views here.
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib import messages  # import messages

class Login(View):
    form_class =LoginForm
    initial = {'key': 'value'}
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        print(form)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)
            if user is not None:

                login(request, user)
                return redirect('dashboard_view')
            else:
                messages.info(request, 'invalid credentials')
                return redirect('login')

        return render(request, self.template_name, {'form': form})

class Dashboard(View):
    def get(self, request):
        template_name = "welcome.html"
        user_instance = Company.objects.filter(user=request.user)
        company_show = []
        for company in user_instance:
            company_instance = Company.objects.filter(role=company.role).last()
            company_show.append(company_instance)
        context = {'company': company_show}
        return render(request, template_name,context)
