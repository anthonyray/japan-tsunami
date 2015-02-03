#http://stackoverflow.com/questions/14919065/how-to-get-simple-hello-world-dajaxice-interaction-to-work
#http://django-dajaxice.readthedocs.org/en/latest/installation.html
#http://django-dajaxice.readthedocs.org/en/latest/quickstart.html
import json
from dajaxice.decorators import dajaxice_register

@dajaxice_register
def sayhello(request):
	print request.body
	return json.dumps({'message':'Hello World'})


