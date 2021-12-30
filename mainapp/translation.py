



from modeltranslation.translator import register, TranslationOptions
from .models import NewsPostForm

@register(NewsPostForm)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)