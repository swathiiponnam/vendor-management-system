from django.db import models

# Create your models here.
class vendor(models.Model):
    vendor_name = models.CharField(max_length=20)
    contact_details = models.TextField()
    vendor_address = models.TextField()
    vendor_code = models.CharField(max_length=20,primary_key=True,default=1)
    on_time_delivery_rate = models.FloatField(blank=True,null=True)
    quality_rating_avg = models.FloatField(blank=True,null=True)
    average_response_time = models.FloatField(blank=True,null=True)
    fulfillment_rate = models.FloatField(blank=True,null=True)

    def __str__(self):
        return self.vendor_code


class purchase_order(models.Model):
    vendor = models.ForeignKey(vendor,on_delete=models.CASCADE)
    po_number = models.CharField(max_length=10,primary_key=True)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=10)
    quality_rating = models.FloatField()
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField()

    def __str__(self):
        return self.po_number


class historical_performance(models.Model):
    vendor = models.ForeignKey(vendor,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
    


