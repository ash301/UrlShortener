import random
import string
from django.conf import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)



def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):

	# newcode = ''
	# for _ in range(size):
	# 	newcode += random.choice(chars)
	# return newcode

	return ''.join(random.choice(chars) for _ in range(size)) 


def create_shortcode(instance, size=SHORTCODE_MIN):
	newcode = code_generator(size = size)
	Klass = instance.__class__
	qs_exists = Klass.objects.filter(shortcode = newcode).exists()
	if(qs_exists):
		return create_shortcode(size=size)
	return newcode
