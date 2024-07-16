from django_web_components import component


@component.register('testcomponent')
class TestComponent(component.Component):
    template_name = 'components/testcomponent.html'
    context = {
        'title': 'Test Component',
        'description': 'This is a test component.'
    }


