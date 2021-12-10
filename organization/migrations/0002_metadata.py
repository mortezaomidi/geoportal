# Generated by Django 3.2.9 on 2021-12-10 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='url')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization', verbose_name='organization')),
            ],
            options={
                'verbose_name': 'Organization Metadat',
                'verbose_name_plural': 'Organizations Metadata',
            },
        ),
    ]