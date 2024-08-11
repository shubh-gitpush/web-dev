from django import forms
from blog_app.models import Post,comment,Reply

class postform(forms.ModelForm):
    class Meta:
        model=Post
        fields=['author','title','text','image','image2','video_file','text2']
        widgets={
            'title':forms.TextInput(attrs={'class':'tetxinputclass'}),
            'text2':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}), #attrs means attribute and the classes it is connected with
            'image':forms.FileInput(attrs={'class': 'fileinputclass'}),
            'image2': forms.FileInput(attrs={'class': 'fileinputclass'}),
            'video_file': forms.FileInput(attrs={'class': 'fileinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),

        }
class commentform(forms.ModelForm):
    class Meta:
        model=comment
        fields=('author','text')
        widgets={
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        }
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['text',]



