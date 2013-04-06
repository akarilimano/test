# coding: utf-8
from django.db import models

class News(models.Model):
    title = models.CharField(verbose_name=u'Заголовок', max_length=255)

    def __unicode__(self):
        return u'%s' % self.title
    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'