from django.db import models

class Post(models.Model):
	title = models.CharField(max_length = 200)
	body = models.TextField()
	timestamp = models.DateTimeField(auto_now_add = True)
	cover = models.ImageField()

	def __str__(self):
		return f"{self.id}.{self.title}"

class Images(models.Model):
	image = models.ImageField(upload_to = 'images/',blank=True,null=True)
	post = models.ForeignKey(Post,on_delete=models.CASCADE)

	def __str__(self):
		# return f"{self.id}.{self.title}"+"Image"
		 return self.post.title + " Image"


	



   