from django.views.generic import TemplateView


class TestPage(TemplateView):
    template_name = 'blog/test.html'


class ThanksPage(TemplateView):
    template_name = 'blog/thanks.html'


class HomePage(TemplateView):
    template_name = 'blog/base.html'
