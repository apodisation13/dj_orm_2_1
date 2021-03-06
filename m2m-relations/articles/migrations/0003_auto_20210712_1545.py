# Generated by Django 3.2.5 on 2021-07-12 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210712_1536'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tagthrough',
            options={'verbose_name': 'Тэг', 'verbose_name_plural': 'Тэги'},
        ),
        migrations.AlterField(
            model_name='tagthrough',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article', verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='tagthrough',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.tag', verbose_name='Тэг'),
        ),
    ]
