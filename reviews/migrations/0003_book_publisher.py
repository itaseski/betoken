# Generated by Django 3.2 on 2022-01-29 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_book_contributor'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='reviews.publisher'),
        ),
    ]
