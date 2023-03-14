from django import forms
from .models import Post, Category


# category_choices = [
#     ('Musicianship', 'Musicianship'), 
#     ('Technique', 'Technique'), 
#     ('Creative', 'Creative'), 
#     ('Repertoire', 'Repertoire'),
# ]

category_choices = Category.objects.all().values_list('name', 'name')

category_list = []

for x in category_choices:
    category_list.append(x)



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'author', 'category', 'body')

        # Bootstrap styling for add post form. Attaches to the html tag class to add bootstrap css styles of 'form-control'
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Add a concise title'}),
            'subtitle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'What is your post about?'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices=category_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Add your content here...'}),
        }
             

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'category', 'body')

        # Bootstrap styling for edit post form. Attaches to the html tag class to add bootstrap css styles of 'form-control'
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Add a concise title'}),
            'subtitle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'What is your post about?'}),
            'category': forms.Select(choices=category_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Add your content here...'}),
        }