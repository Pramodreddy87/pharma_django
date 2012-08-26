from django.db import models

class Adminlogin(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=135, db_column='UserName') # Field name made lowercase.
    password = models.CharField(max_length=135, db_column='Password') # Field name made lowercase.
    class Meta:
        db_table = u'adminlogin'

class Articles(models.Model):
    id = models.IntegerField(primary_key=True)
    article_title = models.CharField(max_length=1500)
    article_description = models.TextField()
    created_on = models.DateTimeField()
    updated_on = models.CharField(max_length=135, blank=True)
    category = models.CharField(max_length=135, blank=True)
    article_content = models.TextField(blank=True)
    class Meta:
        db_table = u'articles'

class Documents(models.Model):
    id = models.IntegerField(primary_key=True)
    article_id = models.IntegerField()
    doc_path = models.CharField(max_length=600, blank=True)
    doc_name = models.CharField(max_length=600, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'documents'

class UserComments(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=135)
    comment = models.TextField(blank=True)
    dateposted = models.DateTimeField(null=True, blank=True)
    article_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'user_comments'
