# Generated by Django 5.1.4 on 2024-12-19 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('document', 'Документ'), ('textbook', 'Учебник'), ('fantasy', 'Фэнтэзи'), ('mystery', 'Мистика'), ('historical', 'История')], max_length=100),
        ),
    ]