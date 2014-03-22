from django.forms import ModelForm
# from profile.models import Profile
from models import DnaProfile
from django import forms


# class ProfileForm(ModelForm):
#     class Meta:
#         model = Profile

class DnaProfileManager(ModelForm):
    class Meta:
        model = DnaProfile
        exclude = ('user',)


class DnaQuickSearch(forms.Form):
    DBS1179_left = forms.DecimalField()
    DBS1179_right = forms.DecimalField()
    D21S11_left = forms.DecimalField()
    D21S11_right = forms.DecimalField()
    D7S820_left = forms.DecimalField()
    D7S820_right = forms.DecimalField()
    CSF1PO_left = forms.DecimalField()
    CSF1PO_right = forms.DecimalField()
    D3S1358_left = forms.DecimalField()
    D3S1358_right = forms.DecimalField()
    TH01_left = forms.DecimalField()
    TH01_right = forms.DecimalField()
    D13S317_left = forms.DecimalField()
    D13S317_right = forms.DecimalField()
    D16S539_left = forms.DecimalField()
    D16S539_right = forms.DecimalField()
    D2S1338_left = forms.DecimalField()
    D2S1338_right = forms.DecimalField()
    D19S433_left = forms.DecimalField()
    D19S433_right = forms.DecimalField()
    vWA_left = forms.DecimalField()
    vWA_right = forms.DecimalField()
    TPOX_left = forms.DecimalField()
    TPOX_right = forms.DecimalField()
    D18S51_left = forms.DecimalField()
    D18S51_right = forms.DecimalField()
    AMEL_left = forms.CharField()
    AMEL_right = forms.CharField()
    D5S818_left = forms.IntegerField()
    D5S818_right = forms.IntegerField()
    FGA_left = forms.DecimalField()
    FGA_right = forms.DecimalField()






