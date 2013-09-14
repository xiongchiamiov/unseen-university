from jsonview.decorators import json_view

from api.models import Script

@json_view
def index(request):
    return [script.humanReadable() for script in Script.objects.order_by('name')]

@json_view
def detail(request, script):
    return Script.objects.get(name=script).humanReadable()

