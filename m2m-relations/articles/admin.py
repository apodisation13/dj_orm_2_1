from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, TagThrough


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_tag = 0
        has_tag = False
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                is_main_tag += 1
            if form.cleaned_data.get('tag'):
                has_tag = True

        if is_main_tag < 1 and has_tag:
            raise ValidationError('Укажите основной раздел')
        elif is_main_tag > 1:
            raise ValidationError('Основным может быть только один раздел')

        return super().clean()


class TagThroughInline(admin.TabularInline):
    model = TagThrough
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagThroughInline]
    # list_display = ['title', 'published_at']
    # search_fields = ['title']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
