# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SnowPack(models.Model):
    code = models.CharField(max_length=12)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    tel = models.CharField(max_length=12)
    contact_dept = models.CharField(max_length=20, blank=True, null=True)
    contacts = models.CharField(max_length=10, blank=True, null=True)
    longitude = models.CharField(max_length=10, blank=True, null=True)
    latitude = models.CharField(max_length=10, blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    create_time = models.DateTimeField()
    create_operator = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_operator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snow_pack'


class SnowTicket(models.Model):
    snow_pack_id = models.IntegerField()
    product_code = models.CharField(max_length=20)
    market_price = models.DecimalField(max_digits=20, decimal_places=0)
    prefer_price = models.DecimalField(max_digits=20, decimal_places=0)
    spare_number = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    product_type = models.IntegerField()
    create_time = models.DateTimeField()
    create_operator = models.IntegerField()
    update_operator = models.IntegerField()
    update_time = models.DateTimeField()
    is_online = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'snow_ticket'


class SnowTicketType(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    include_board = models.IntegerField()
    day_or_hour = models.IntegerField()
    duration = models.DecimalField(max_digits=5, decimal_places=0)
    use_time = models.IntegerField()
    trail_type = models.IntegerField()
    type_name = models.CharField(max_length=20)
    create_time = models.DateTimeField()
    create_operator = models.IntegerField()
    update_time = models.DateTimeField(blank=True, null=True)
    update_operator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snow_ticket_type'


class UseTime(models.Model):
    id = models.IntegerField(primary_key=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField()
    name = models.CharField(max_length=20)
    duration = models.DecimalField(max_digits=8, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'use_time'
