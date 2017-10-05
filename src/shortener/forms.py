from django import forms

from .validators import validate_url, validate_dot_com

class SubmitUrlForm(forms.Form):
	url = forms.CharField(label='Submit URL',validators=[validate_url, validate_dot_com])

	

	# def clean_url(self):
	# 	url = self.cleaned_data['url']
	# 	if not "com" in url:
	# 		raise forms.ValidationError("This is not a valid url becz of no .com")



	# 	print(url)
	# 	url_validator = URLValidator()

	# 	try:
	# 		url_validator(url)
	# 	except:
	# 		raise forms.ValidationError("Invalid Url for ths field")
	# 	return url	