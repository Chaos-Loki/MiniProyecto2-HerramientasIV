from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django_currentuser.db.models import CurrentUserField
# Create your models here.

class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
        
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

#class producto, este va a detallar las especificaciones del producto
#debe usarse tambien en caso de añadir como de mostrar en pantalla
#debe de tener nombre, descripcion, precio, imagen y categoria

class Categories(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
        ordering = ["name"]
        
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to="media")
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/category/{self.slug}"
    

class Product(models.Model):
    
    class Meta:
        verbose_name_plural = 'Product Profiles'
        verbose_name = 'Product'
        ordering = ["category"]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    details = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(upload_to="product")
    is_active = models.BooleanField(default=True)
    category = models.OneToOneField(Categories, default=False, on_delete=models.CASCADE)
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/product/{self.slug}"
    

