from xml.dom import ValidationErr

from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Item(models.Model):
    item_id = models.CharField(max_length=200, primary_key=True, null=False, blank=False, unique=True, editable=True, verbose_name='부품 시리얼')
    category_name = models.CharField(max_length=200, null=False, blank=False, editable=True, verbose_name='부품 명')
    production_date = models.DateField('생산일')
    

    def __str__(self):
        return f'부품:{self.category_name}, item_id:{self.item_id}'
    
class Buyer(models.Model):
    phoneNumberRegex = RegexValidator(regex = r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$', message='잘못 된 형식의 연락처를 입력했습니다.')
    name=models.CharField(max_length=200, verbose_name='업체명')
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 20, unique = True, verbose_name='연락처')
    address = models.CharField(max_length=1000, verbose_name='주소')
    ceo_name = models.CharField(max_length=200, editable=True, verbose_name='대표명')

    def __str__(self):
        return f'업체_ID:{self.id}, 업체명:{self.name}, 대표명:{self.ceo_name}, 연락처:{self.phoneNumber}, 주소:{self.address},'
    
class SalesHistory(models.Model):
    sales_date = models.DateField('판매일')
    #date_of_delivery = models.DateField('인도일')
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, verbose_name='구매자')
    item_id = models.OneToOneField(Item, db_column='item_id', unique=True, on_delete=models.CASCADE, verbose_name='부품')
    price = models.IntegerField(verbose_name = "상품가격", default=0)
    
            
class InspectionLog(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='부품')
    inspection_date = models.DateField('검사일')
    log = models.TextField(help_text="Comment contents", blank=False, null=False, verbose_name='검사 내용')#models.CharField(max_length=5000)

    def __str__(self):
        return f'아이디:{self.item_id}, 검사일:{self.inspection_date}, 내용:{self.log}'