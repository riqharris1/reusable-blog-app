from django import forms
from .models import p
 
 
class BlogPostForm(forms.ModelForm):
 
    class Meta:
        model = Post
        fields = ('title', 'content','image')