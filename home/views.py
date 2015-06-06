from django.views.generic import TemplateView

# Create your views here.
class landing(TemplateView):
	template_name = 'landing.html'

	def get_coontext_data(self):
		context = super(landing, self).get_coontext_data()
		context['title'] = 'Chilango Django'
		context['meta_description'] = 'Mi primer pagina con Django'
		return context