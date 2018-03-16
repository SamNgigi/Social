from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    # Below we set custom labels to the form field.

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Wewe ni nani. Who are you? Eeeh....aaah ah.. wewe ni nani. Tuambie'
        self.fields['email'].label = 'Email Address'
