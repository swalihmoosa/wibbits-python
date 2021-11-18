# Generated by Django 3.2.9 on 2021-11-18 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_alter_review_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='testimonials')),
                ('logo', models.FileField(upload_to='testimonials\\logo')),
                ('description', models.TextField(max_length=255)),
                ('name', models.CharField(max_length=125)),
                ('role', models.CharField(max_length=125)),
                ('company_name', models.CharField(max_length=125)),
                ('is_featured', models.BooleanField()),
            ],
        ),
    ]
