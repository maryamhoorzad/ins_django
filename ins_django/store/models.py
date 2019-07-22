from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField( default="cslug")
    picture = models.FileField(upload_to="static/product_pics/")
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children')

    class Meta :
        ordering = ('name', )
        unique_together = ('slug', 'parent',)
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('productlist', args=[self.slug])

    def __str__(self):
        full_path = [self.name]
        k=self.parent

        while k is not None:
            full_path.append(k.name)
            k=k.parent

        return '->'.join(full_path[::-1])


class Brand(models.Model):
    english_name = models.CharField(max_length=30)
    persian_name = models.CharField(max_length=30)
    brand_desc = models.TextField()
    picture = models.FileField(upload_to="static/product_pics/")

    class Meta :
        pass

    def __str__(self):
        return self.english_name


class Product(models.Model):
    name = models.CharField(max_length=30)
    sous_titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, default="slug")
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    picture = models.FileField(upload_to="static/product_pics/")
    category = models.ManyToManyField(Category, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete= models.CASCADE)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('productdetail', args=[self.id, self.slug])

    def get_cat_list(self):
        k = self.category
        breadcrumb =["shop"]
        while k is not None:
            breadcrumb.append(k.slug)   #can i use slug instead of name ?
            k=k.parent

        for i in range(len(breadcrumb)-1):
            breadcrumb[i]= '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]
        





