from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        labels = {'photo':''}
        # image = forms.ImageField(widget = forms.FileInput(attrs = {"id" : "image_field", style = "height: 100px ; width : 100px ; " })
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            for field_name, field in self.fields.items():
                field.widget.attrs.update({'class': 'form-control'})