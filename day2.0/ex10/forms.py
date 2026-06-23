from django import forms
from .models import People


class SearchForm(forms.Form):
    min_date = forms.DateField(
        label="Movies minimum release date",
        widget=forms.DateInput(attrs={"type": "date"})
    )
    max_date = forms.DateField(
        label="Movies maximum release date",
        widget=forms.DateInput(attrs={"type": "date"})
    )
    diameter = forms.IntegerField(
        label="Planet diameter greater than"
    )
    gender = forms.ChoiceField(
        label="Character gender"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        genders = People.objects.exclude(
            gender__isnull=True
        ).values_list(
            "gender", flat=True
        ).distinct().order_by("gender")

        self.fields["gender"].choices = [(g, g) for g in genders]