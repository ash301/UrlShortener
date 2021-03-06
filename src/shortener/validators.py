from django.core import validators
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator




def validate_url(value):
	url_validator = URLValidator()
	try:
		url_validator(value)
	except:
		raise ValidationError("Invalid url for this field")
	return value

def validate_dot_com(value):
	if not "com" in value:
		raise ValidationError("This is not a valid url becz of no .com")
	return value
