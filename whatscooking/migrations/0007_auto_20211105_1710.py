# Generated by Django 3.2.6 on 2021-11-05 17:10

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('whatscooking', '0006_auto_20211105_0452'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cook_time',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='default_recipe.png', upload_to='recipe_pics'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='serving_size',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='url',
            field=models.CharField(max_length=100, null=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AlterField(
            model_name='recipestep',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recipestep',
            name='order',
            field=models.IntegerField(),
        ),
    ]