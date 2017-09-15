from django.db import models


class businesses(models.Model):
	gst_id = models.AutoField(null=False,primary_key=True)
	acc_no = models.BigIntegerField(null=False,unique=True)
	bus_name = models.CharField(max_length=200,null=False,unique=True)
	#gst_no = models.BigIntegerField(null=False,unique=True,default=0)

	email_id = models.EmailField(max_length=200,null=False)
	phone_no = models.BigIntegerField(null=False)
	
	hq_address = models.CharField(max_length=200,null=False)
	prod_count = models.IntegerField()
	
	turnover = models.PositiveIntegerField(null=False)
	sector = models.CharField(max_length=40,null=False)

	def __str__(self):
		return self.email_id
	
	def __str__(self):
		return self.sector
	
	def __str__(self):
		return self.hq_address

	def __str__(self):
		return self.bus_name
	
class products(models.Model):
	prod_id = models.AutoField(null=False,primary_key=True)
	prod_name = models.CharField(null=False,max_length=20)
	hsn = models.BigIntegerField(null=False,unique=True,default=0)
	
	prod_make = models.CharField(null=False,max_length=20)
	prod_type = models.CharField(null=False,max_length=20)
	
	manuf_price = models.IntegerField(null=False)
	sell_price = models.IntegerField(null=False)

	bus = models.ForeignKey(businesses, on_delete=models.CASCADE,null=True)
	applied_gst = models.IntegerField(null=False)

	def __str__(self):
		return self.prod_make
	
	def __str__(self):
		return self.prod_type

	def __str__(self):
		return self.prod_name	
	

class b2b_txn(models.Model):
	b2b_id = models.AutoField(null=False,primary_key=True)
	prod = models.ForeignKey(products, on_delete=models.CASCADE,null=True)
	
	seller_gst = models.ForeignKey(businesses, on_delete=models.CASCADE,related_name='+',null=True)
	buyer_gst = models.ForeignKey(businesses, on_delete=models.CASCADE,null=True)
	
	b2b_txn_amt = models.IntegerField()
	b2b_txn_date = models.DateField()

class b2c_txn(models.Model):
	b2c_id = models.AutoField(null=False,primary_key=True)
	prod = models.ForeignKey(products, on_delete=models.CASCADE,null=True)
	
	seller_gst = models.ForeignKey(businesses, on_delete=models.CASCADE,null=True)
	b2c_txn_amt = models.IntegerField()
	
	b2c_txn_date = models.DateField()

