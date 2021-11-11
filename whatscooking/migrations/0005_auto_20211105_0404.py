# Generated by Django 3.2.6 on 2021-11-05 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('whatscooking', '0004_collection_collectiontitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('order', models.CharField(max_length=3)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_steps', to='whatscooking.collection')),
            ],
        ),
        migrations.DeleteModel(
            name='CollectionTitle',
        ),
    ]
