from django.db import models


class JobRelatedItemsMixins(models.Model):
	class Meta:
		abstract = True
