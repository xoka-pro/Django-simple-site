from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=80, null=False, unique=True)

    def __str__(self):
        return f'{self.name}'


class Author(models.Model):
    fullname = models.CharField(max_length=150, unique=True)
    born_date = models.CharField(max_length=100, null=False)
    born_location = models.CharField(max_length=150, null=False)
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.fullname}'


class Quote(models.Model):
    text = models.TextField(max_length=1000, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.text}'

    def get_quote_text(self):
        return self.text

    def get_quote_author(self):
        return self.author

    def get_quote_tags(self):
        tags = self.tags.all()
        return tags
