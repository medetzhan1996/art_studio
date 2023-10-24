from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string


class Project(models.Model):
    """ Модель проекта """
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    article = models.CharField(max_length=12, unique=True,
                               default=get_random_string(12).upper())
    purpose = models.TextField()
    color = models.CharField(max_length=7)  # as HEX code
    area = models.DecimalField(max_digits=5, decimal_places=2)
    width = models.DecimalField(max_digits=5, decimal_places=2)
    length = models.DecimalField(max_digits=5, decimal_places=2)
    ceiling_height = models.DecimalField(max_digits=5, decimal_places=2)
    is_draft = models.BooleanField(default=True)


class Visualization(models.Model):
    """ Модель Визуализации проекта """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    view_type = models.CharField(max_length=10, choices=[
        ('left', 'Левый'), ('right', 'Правый')])
    image = models.ImageField(upload_to='visualizations/')


class Plan(models.Model):
    """ Модель Планировки """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    view_type = models.CharField(max_length=10, choices=[
        ('left', 'Левый'), ('right', 'Правый')])
    image = models.ImageField(upload_to='plans/')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['project', 'view_type'],
                name='unique_project_viewtype_for_plan'),
        ]


class Detail(models.Model):
    """ Возможные типы деталей проекта """
    TYPES = (
        ('3d_visualization', '3D Визуализация'),
        ('room_data', 'Исходные данные помещения'),
        ('furniture_layout', 'План расстановки мебели'),
        ('furniture_specifications', 'Спецификации мебели и сантехники'),
        ('lighting_equipment_layout', 'План расстановки осветительного оборудования'),
        ('lighting_device_attachment', 'План привязки осветительных приборов'),
        ('socket_layout', 'План расстановки розеток'),
        ('floor_covering_layout', 'План напольных покрытий'),
        ('ceiling_layout', 'План потолка'),
        ('wall_finishing_layout', 'Развертки стен с отделкой'),
        ('finishing_materials_specifications', 'Спецификации отделочных материалов'),
        ('custom_furniture', 'Мебель индивидуального изготовления'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    detail_type = models.CharField(max_length=50, choices=TYPES)
    file = models.FileField(
        upload_to='details/',
        validators=[FileExtensionValidator(['jpg', 'png', 'pdf'])])
