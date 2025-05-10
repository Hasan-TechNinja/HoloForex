from django import forms
from . models import Comment

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "email", "comment")
        widgets = {
            "name": forms.TextInput(attrs={"class": "input-class", 'placeholder': "Name"}),
            "email": forms.EmailInput(attrs={"class": "input-class", 'placeholder': 'Email'}),
            "comment": forms.Textarea(attrs={"class": "textarea-class", "rows": 4, "placeholder": "Your Comment"}),
        }
