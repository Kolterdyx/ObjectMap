from django.db import models


# Create your models here.


class Auditable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Object(Auditable):
    filepath = models.CharField(max_length=1000)
    tags = models.ManyToManyField('Tag', related_name='objects')


class Tag(Auditable):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.name} - {self.color}'

    class Meta:
        ordering = ['name']
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_tag_name')
        ]


class Query(Auditable):
    query = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=6)

    class Meta:
        ordering = ['name']
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_query_name')
        ]

    def __str__(self):
        return f'{self.name} - {self.color}'
