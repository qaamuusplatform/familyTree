# Generated by Django 4.1.5 on 2023-01-17 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('familyTree', '0006_parent_simbarent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='simBarent',
        ),
        migrations.AddField(
            model_name='parent',
            name='bigWaalid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='familyTree.bigparent'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='waalidka',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='familyTree.parent'),
        ),
    ]
