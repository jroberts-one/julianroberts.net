# Generated by Django 3.2.6 on 2021-09-10 04:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('whatscooking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeasurementQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MeasurementUnits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='author',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='vegan',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='vegetarian',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cook_time',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='directions',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='serving_size',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='RecipeIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whatscooking.ingredient')),
                ('quantity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whatscooking.measurementquantity')),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whatscooking.recipe')),
                ('unit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whatscooking.measurementunits')),
            ],
        ),
        migrations.CreateModel(
            name='PantryIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whatscooking.ingredient')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]