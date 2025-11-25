from django import forms
class ContactForm(forms.Form):
    
    name=forms.CharField(label='Name')
    email=forms.EmailField(label='Mail')
    title=forms.CharField(label='Title')
    message=forms.CharField(label='Message', widget=forms.Textarea)
    
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['placeholder']=\
            ""
        self.fields['name'].widget.attrs['class']='form-control'
        
        self.fields['email'].widget.attrs['placeholder']=\
            ""
        self.fields['email'].widget.attrs['class']='form-control'
        
        self.fields['title'].widget.attrs['placeholder']=\
            ""
        self.fields['title'].widget.attrs['class']='form-control'
        
        self.fields['message'].widget.attrs['placeholder']=\
            ""
        self.fields['message'].widget.attrs['class']='form-control'