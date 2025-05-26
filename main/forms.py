from django import forms
from . models import Comment, Contact

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "email", "comment")
        widgets = {
            "name": forms.TextInput(attrs={"class": "input-class", 'placeholder': "Name"}),
            "email": forms.EmailInput(attrs={"class": "input-class", 'placeholder': 'Email'}),
            "comment": forms.Textarea(attrs={"class": "textarea-class", "rows": 4, "placeholder": "Your Comment"}),
        }

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "message")
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500",
                "placeholder": "Your Name"
            }),
            "email": forms.EmailInput(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500",
                "placeholder": "Your Email"
            }),
            "message": forms.Textarea(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500",
                "placeholder": "Your Message",
                "rows": 5
            }),
        }