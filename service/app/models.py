from django.db import models


class Menu(models.Model):
	slug = models.SlugField(primary_key=True, unique=True, verbose_name="Url")
	title = models.CharField(max_length=50, verbose_name="Название")
	parent = models.ForeignKey(
		to="self",
		on_delete=models.SET_DEFAULT,
		null=True, blank=True,
		related_name="child",
		verbose_name="Родитель",
		default=None
	)

	def __str__(self):
		return self.title
