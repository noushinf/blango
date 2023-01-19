from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django_registration.forms import RegistrationForm
from blango_auth.models import User


class BlangoRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User


@login_required
def profile(request):
    return render(request, "blango_auth/profile.html")
# Create your views here.
