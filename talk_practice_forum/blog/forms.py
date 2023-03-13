from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'author', 'body')

        # Bootstrap styling for add post form. Attaches to the html tag class to add bootstrap css styles of 'form-control'
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Add a concise title'}),
            'subtitle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'What is your post about?'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Add your content here...'}),
        }
             