from django import forms
from .models import Post

# Список запрещённых слов из задания
FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'publication_attribute']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Стилизация Bootstrap
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['publication_attribute'].widget.attrs.update({'class': 'form-check-input'})

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title:
            title_lower = title.lower()
            for word in FORBIDDEN_WORDS:
                if word in title_lower:
                    raise forms.ValidationError(f'Заголовок содержит запрещённое слово: "{word}"')
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if content:
            content_lower = content.lower()
            for word in FORBIDDEN_WORDS:
                if word in content_lower:
                    raise forms.ValidationError(f'Содержимое содержит запрещённое слово: "{word}"')
        return content