from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name='home.html'

class SnackListView(TemplateView):
    template_name='snack_list.html'