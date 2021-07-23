from django import forms
from .models import Listing


class CreateListingForm(forms.ModelForm):
    title = forms.CharField(max_length=300)
    description = forms.CharField(max_length=1500, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['title'].label = "Job Title :"
        self.fields['description'].label = "Job Description :"
        self.fields['location'].label = "Job Location :"
        self.fields['job_type'].label = "Job Type :"
        self.fields['category'].label = "Developer Type :"
        self.fields['compensation'].labels = "Compensation :"
        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'eg : Web Developer',
            }
        )
        self.fields['description'].widget.attrs.update(
            {
                'placeholder': 'Describe the duties the job entails, any extra employee benefits, or any other info someone applying should know.',
            }
        )
        self.fields['location'].widget.attrs.update(
            {
                'placeholder': 'eg : Indianapolis',
            }
        )

    class Meta:
        model = Listing
        fields = [
            "title",
            "description",
            "location",
            "job_type",
            "category",
            "compensation",
        ]
