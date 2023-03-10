# Generated by Django 4.0.3 on 2022-12-17 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('experiences', '0002_rename_experiencemodel_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='service',
            name='detail',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
    ]
