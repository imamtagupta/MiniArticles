from django import forms

class NewMessage(forms.Form):
    title = forms.CharField(max_length=255,
    widget = forms.TextInput(attrs = {
            'class':"form-control",
            'placeholder':"Enter title here..",
            "autocomplete":"off"
        }
    ))

    description = forms.CharField(max_length=255,
    widget = forms.TextInput(attrs = {
            'class':"form-control",
            'placeholder':"Enter description here..",
            "autocomplete":"off",
        }),
    required=False)

    image = forms.ImageField(required=False,
        widget=forms.FileInput(
            attrs={
                "type":"file",
                "class":"form-control",
                "accept":"image/*",
        })
    )

    video = forms.FileField(required=False,max_length=255,
    widget=forms.FileInput(
        attrs = {
            "type":"file",
            "class":"form-control",
            "accept":"video/*",
        }
    ))

    ytvideo = forms.CharField(max_length=255,
    widget = forms.TextInput(attrs = {
            'class':"form-control",
            'placeholder':"Emben youtube vide here..",
            "autocomplete":"off",
        }),
    required=False)