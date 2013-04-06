# coding: utf-8
from django.db import models

class News(models.Model):
    title = models.CharField(verbose_name=u'Заголовок', max_length=255)
    date = models.DateField(verbose_name=u'Date',name=u'Date2',auto_now=True,auto_now_add=True)
    summary = models.CharField(verbose_name=u'Краткое описание',max_length=255, help_text=u'Такие дела')
    fulltext = models.CharField(verbose_name=u'Описание', max_length=1000,help_text=u'Сама новость')

    def __unicode__(self):
        return u'%s' % self.title
    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'