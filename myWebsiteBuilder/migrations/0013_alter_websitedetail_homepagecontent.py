# Generated by Django 3.2.3 on 2021-07-16 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myWebsiteBuilder', '0012_websitedetail_homepagecontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitedetail',
            name='homepageContent',
            field=models.TextField(blank=True, null=True),
        ),
    ]