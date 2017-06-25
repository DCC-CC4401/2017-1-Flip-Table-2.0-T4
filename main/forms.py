from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from main.models import Usuario, Comida, Client
from django import forms


class ClientCreateForm(UserCreationForm):
    # CHOICES = (
    #     ('1', 'AvatarEstudiante1.png',),
    #     ('2', 'AvatarEstudiante2.png',),
    #     ('3', 'AvatarEstudiante3.png',),
    #     ('4', 'AvatarEstudiante4.png',))
    # choices = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    def __init__(self, *args, **kwargs):
        super(ClientCreateForm, self).__init__(*args, **kwargs)
        # self.fields['first_name'].required = True
        # self.fields['last_name'].required = True
        self.fields['first_name'].widget.attrs.update({'autofocus': 'autofocus'})
        # self.fields['choices'].widget.attrs.update({'class': 'with-gap'})

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'image')
        # def save(self, commit=True):
        #     if not commit:
        #         raise NotImplementedError("Can't create User and Profile without database save")
        #     user = super(ClientCreateForm, self).save(commit=True)
        #     image = "default/" + dict(self.fields['choices'].choices)[self.cleaned_data['choices']]
        #     profile = Client(user=user, image=image)
        #     profile.save()
        #     return user, profile


class LoginForm(forms.Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class GestionProductosForm(forms.Form):
    idVendedor = 0
    nombre = forms.CharField(max_length=200)
    categoria = forms.IntegerField()
    descripcion = forms.CharField(max_length=500)
    stock = forms.IntegerField()
    precio = forms.IntegerField()


class editarProductosForm(forms.Form):
    foto = forms.FileField()
