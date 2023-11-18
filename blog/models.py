from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    
    def __str__(self):
        category_names = ', '.join(category.name for category in self.categories.all())
        return f'Title: {self.title} | Categories: {category_names}'    

    # def __str__(self):
    #     return ' Title: ' + self.title + ' | Category:  ' + str(self.categories.get().name)
    
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.author} on '{self.post}'"