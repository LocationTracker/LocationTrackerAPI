from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User
from core.models import PerfilUsuario
from .forms import UserForm


def create_user(request):
    user = User()
    user_form = UserForm(instance=user)

    ProfileInlineFormset = inlineformset_factory(User, PerfilUsuario,
                                                 fields=('cpf', 'telefone', 'foto'))
    formset = ProfileInlineFormset(instance=user)
    if request.method == "POST":
        user_form = UserForm(request.POST, request.FILES, instance=user)
        formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

        if user_form.is_valid():
            created_user = user_form.save(commit=False)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)
            created_user.set_password(request.POST['password'])
            if formset.is_valid():
                created_user.save()
                formset.save()
                return HttpResponseRedirect('/')

    return render(request, "public/create_usuario.html", {
        "form": user_form,
        "formset": formset
    })
