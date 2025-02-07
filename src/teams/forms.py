from django import forms

from .models import Team


class TeamCreateForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ["name"]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name.startswith("man") or name.endswith("city"):
            raise forms.ValidationError("Cannot enter this team")

        return name
