from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(label='Autor',required=True)
    # comentario = forms.Textarea(required=True)
    post = forms.CharField(label='post',required=True)