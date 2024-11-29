from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Blog(models.Model):
    image = models.ImageField(upload_to='Images/blog')
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.category}"

class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    
    def __str__(self):
        return f"Comment by {self.name} on {self.blog.title}"
    
class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email Address")
    text = models.TextField(verbose_name="Your Message")

    def __str__(self):
        return f"{self.text[:50]}... by {self.name}"
    
class Project(models.Model):
    image = models.ImageField(upload_to='Images/project')
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.category}"





