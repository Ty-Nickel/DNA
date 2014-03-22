from django.forms import ModelForm
from dna.models import Dna
from profiles.models import DnaProfile


class DnaForm(ModelForm):
    class Meta:
        model = Dna


class DnaProfileForm(ModelForm):
    class Meta:
        model = DnaProfile