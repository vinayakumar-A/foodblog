# Generated by Django 3.1.3 on 2020-11-21 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food_post',
            name='text',
            field=models.TextField(default='exit', verbose_name='About Food'),
            preserve_default=False,
        ),
    ]