from django.db import models

class roll(models.Model):
	name = models.CharField(max_length=20)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	age = models.PositiveSmallIntegerField(default=10)
	email = models.EmailField(max_length=254, default='abc@xyz.com')
	college_Rollno = models.PositiveSmallIntegerField(default=125045)
	def __unicode__(self):
		return self.name