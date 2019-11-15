from django import  forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length=30,
    widget=forms.TextInput(
        attrs={'class': 'form-control', 
        'placeholder': 'Enter todo e.g. Learn how to play guitar',
        'aria-label': 'Todo', 
        'aria-describedby':'add-btn'}
    ))
