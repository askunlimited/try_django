from django import forms
from .models import Article



class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'content']


    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        qs = Article.objects.filter(title__icontains=title)

        if qs.exists():
            self.add_error("title", f"{title} is already taken")

        return cleaned_data




# class ArticleForm(forms.Form):
#     title = forms.CharField()
#     content = forms.CharField()

#     # def cleaned_data(self):
#     #     cleaned_data = self.changed_data
#     #     title = cleaned_data.get('title')
#     #     return title
    
#     def clean_data(self):
#         cleaned_data = self.cleaned_data
#         title = cleaned_data.get('title')
#         if title.lower().strip() == 'The office':
#             raise forms.ValidationError("This title is taken")

#         print('all data: ', cleaned_data )
#         return cleaned_data