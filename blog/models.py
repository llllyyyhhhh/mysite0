from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from read_statistics.models import ReadNumExpandMethod, ReadDetail
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class BlogType(models.Model):
    type_name = models.CharField(max_length=15, verbose_name='类型名称')

    def __str__(self):
        return self.type_name

class Blog(models.Model, ReadNumExpandMethod):
    title = models.CharField(max_length=50, verbose_name='标题')
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE, related_name='blog_blog', verbose_name='类型')
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    read_details = GenericRelation(ReadDetail)
    created_time = models.DateTimeField(verbose_name='影片发行时间')
    last_updated_time = models.DateTimeField(auto_now=True)
    '''
    def get_read_num(self):
        try:
            return self.readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0
    '''

    def get_url(self):
        return reverse('blog_detail', kwargs={'blog_pk': self.pk})

    def get_email(self):
        return self.author.email

    def __str__(self):
        return "<Blog: %s>" % self.title
    class Meta:
        ordering = ['-created_time']
'''
class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE)
'''
