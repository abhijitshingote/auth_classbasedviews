from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Authorization(models.Model):
	authorizationid=models.CharField(max_length=11,blank=False)
	memberid=models.CharField(max_length=11,blank=False)
	ndc_no=models.CharField(max_length=11,blank=False)
	startdate=models.DateField()
	enddate=models.DateField()
	createdate=models.DateTimeField(auto_now_add=True)
	updatedate=models.DateTimeField(auto_now=True )
	createdby=models.ForeignKey(User,on_delete=models.CASCADE)
	updatedby=models.ForeignKey(User,on_delete=models.CASCADE,related_name="updatedby")

	def __str__(self):
		return self.authorizationid

	def get_absolute_url(self):
		from django.urls import reverse
		return reverse('auth_detail', args=[str(self.id)])
		# return reverse('auths')