# Generated by Django 4.2.4 on 2023-08-11 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_recipe_user_alter_recipe_recipe_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['recipe_name']},
        ),
    ]