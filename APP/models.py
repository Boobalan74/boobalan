from django.db import models



class UserPersonalModel(models.Model):

    user_image = models.ImageField(upload_to='profileimages/')
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField(null=True, blank=True)   
    phone = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


    def __str__(self):
        return self.lastname, self.state, self.country


class ImageModel(models.Model):

    image = models.ImageField(upload_to='images/')
    pdf_file = models.FileField(upload_to='pdfs/')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.name 