from django.forms import ModelForm

from .models import Invitation


class InvitationForm(ModelForm):
    class Meta:  # meta class to configure behavior
        model = Invitation
        # exclude what you dont want to see in the model form
        exclude = ('from_user', 'timestamp')
