from xml.dom import ValidationErr

from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.



class PartsType(models.Model):
    name=models.CharField(max_length=200,  primary_key=True, null=False, blank=False, unique=True, editable=True, verbose_name='부품명')
    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('item_log:parts_type_list')
    class Meta:
        ordering=['name']


class Parts(models.Model):
    serial=models.CharField(max_length=200, primary_key=True, null=False, blank=False, editable=True, verbose_name='시리얼')
    category=models.ForeignKey(PartsType, null=False, blank=False, on_delete=models.CASCADE, verbose_name='부품명')
    production_date = models.DateField('제조일', null=True, blank=True, editable=True)
    discard_date = models.DateField('폐기일', null=True, blank=True, editable=True)
    #model_serial = models.ForeignKey(Product, null=True, blank=True, editable=True, on_delete=models.CASCADE, db_column="model_serial", verbose_name='리프트 번호')
    def __str__(self):
        return f'{self.serial}'
    class Meta:
        db_table = 'parts'
        ordering=['serial','production_date']
        

class Reducer(Parts):
    reducer_id =models.OneToOneField(Parts, parent_link=True, on_delete=models.CASCADE, verbose_name='감속기 시리얼')
    gear_ratio = models.FloatField(verbose_name='감속비') # 
    def __str__(self):
        return f'{self.reducer_id}'
    
    def get_absolute_url(self):
        return reverse('item_log:reducer_list')
    class Meta:
        db_table = 'reducers'
        ordering=['reducer_id']
        

class Motor(Parts):
    motor_id =models.OneToOneField(Parts, parent_link=True, on_delete=models.CASCADE, verbose_name='모터 시리얼')
    capacity = models.FloatField(verbose_name='용량') # 
    def __str__(self):
        return f'{self.motor_id}'

    def get_absolute_url(self):
        return reverse('item_log:motor_list')

    class Meta:
        db_table = 'motor'
        ordering=['motor_id']

class Break(Parts):
    break_id =models.OneToOneField(Parts, parent_link=True, on_delete=models.CASCADE, verbose_name='브레이크 시리얼')
    torque = models.FloatField(verbose_name='토크') # 
    def __str__(self):
        return f'{self.break_id}'

    def get_absolute_url(self):
        return reverse('item_log:break_list')

    class Meta:
        db_table = 'breaks'
        ordering=['break_id']

class SafetyDevice(Parts):
    safety_device_id =models.OneToOneField(Parts, parent_link=True, on_delete=models.CASCADE, verbose_name='가바나 시리얼')
    capacity = models.FloatField(verbose_name='용량') # 
    def __str__(self):
        return f'{self.safety_device_id}'

    def get_absolute_url(self):
        return reverse('item_log:safety_device_list')

    class Meta:
        db_table = 'safety_devices'
        ordering=['safety_device_id']
class ModelType(models.Model):
    types = [
        ('Single', 'Single'),
        ('Twin', 'Twin')
    ]
    model=models.CharField(max_length=200, primary_key=True, null=False, blank=False, unique=True, editable=True, verbose_name='모델명')
    type=models.CharField(max_length=200, null=False, blank=False, editable=True, verbose_name='제품 타입', choices=types)
    load_weight=models.IntegerField(default=0, verbose_name='적재하중')
    operation_section =models.IntegerField(default=0, verbose_name='운행구간')
    capacity =models.IntegerField(default=0, verbose_name='최대정원')
    rated_speed = models.IntegerField(default=0, verbose_name='정격속도')
    def __str__(self):
        return f'{self.model}'

    def get_absolute_url(self):
        return reverse('item_log:model_type_list')
    class Meta:
        db_table = 'modeltype'
        ordering=['model']



class ProductionCompany(models.Model):
    business_number=models.CharField(max_length=200, primary_key=True, null=False, blank=False, unique=True, editable=True, verbose_name='사업자번호')
    name=models.CharField(max_length=400, null=False, blank=False, editable=True, verbose_name='제조사명')
    ceo=models.CharField(max_length=100, null=False, blank=False, editable=True, verbose_name='대표')
    address=models.CharField(max_length=1000, null=False, blank=False, editable=True, verbose_name='주소')
    phone=models.CharField(max_length=100, null=False, blank=False, editable=True, verbose_name='전화번호')
    insureance_company=models.CharField(max_length=200, null=True, blank=True, editable=True, verbose_name='보험사명')
    insureance=models.CharField(max_length=200, null=True, blank=True, editable=True, verbose_name='보험상품명')
    start_date=models.DateField('보험기간 시작일', null=True, blank=True, editable=True)
    end_date=models.DateField('보장기간 종료시점', null=True, blank=True, editable=True)
    def __str__(self):
        return f'{self.name}:{self.business_number}'


    def get_absolute_url(self):
        return reverse('item_log:production_company_list')
    class Meta:
        db_table = 'production_company'
        ordering=['business_number']


class Product(models.Model):
    serial=models.CharField(max_length=200, primary_key=True, null=False, blank=False, unique=True, editable=True, verbose_name='리프트 번호')
    model=models.ForeignKey(ModelType, null=True, blank=True, on_delete=models.CASCADE, db_column="model_type", verbose_name='모델명')
    safety_device=models.OneToOneField(SafetyDevice, null=True, blank=True, on_delete=models.SET_NULL, db_column='safety_device', verbose_name='가바나')
    reducer=models.OneToOneField(Reducer, null=True, blank=True, on_delete=models.SET_NULL, db_column='reducer', verbose_name='감속기')
    motor=models.OneToOneField(Motor, null=True, blank=True, on_delete=models.SET_NULL, db_column='motor', verbose_name='모터')
    brake=models.OneToOneField(Break, null=True, blank=True, on_delete=models.SET_NULL, db_column='brake', verbose_name='브레이크')
    production_company=models.ForeignKey(ProductionCompany, null=True, blank=True, on_delete=models.SET_NULL, db_column="production_company_id", verbose_name='제조업체')
    production_date=models.DateField('제조일', null=True, blank=True, editable=True)
    discard_date=models.DateField('폐기일', null=True, blank=True, editable=True)

    def __str__(self):
        return f'{self.serial}'
    
    def get_absolute_url(self):
        return reverse('item_log:product_list')
    class Meta:
        db_table = 'products'

class SelfDiagnosis(models.Model):
    result_type=    [
        ('합', '적합'),
        ('불', '부적합')
    ]
    checklist_submit=    [
        ('제출', '제출'),
        ('미제출', '미제출')
    ]
    product = models.ForeignKey(Product, null=False, blank=False, editable=True, on_delete=models.CASCADE, db_column="product_serial", verbose_name='리프트 번호')
    check_company = models.CharField(max_length=200, null=True, blank=True, editable=True, verbose_name='점검업체')
    checker = models.CharField(max_length=200, null=True, blank=True, editable=True, verbose_name='점검자')
    date = models.DateField("점검일자", null=True, blank=True, editable=True)
    result = models.CharField(max_length=200, null=True, blank=True, editable=True, verbose_name='자체점검결과', choices=result_type)
    check_list = models.CharField(max_length=200, null=True, blank=True, editable=True, verbose_name='점검표', choices=checklist_submit)
    def __str__(self):
        return f'{self.product}'

    class Meta:
        db_table = 'self_diagnosis'
        ordering=['date', 'product']

class FaultHistory(models.Model):
    fault_type=models.TextField(verbose_name='고장유형')
    date=models.DateField(verbose_name='고장일')
    cause=models.TextField(verbose_name='고장원인')
    repair_company=models.CharField(max_length=200, verbose_name='구출기관')
    parts=models.ForeignKey(Parts, null=False, blank=False, on_delete=models.CASCADE, verbose_name='부품 시리얼')
    
    def __str__(self):
        return f'{self.date}: {self.parts}, 이력: {self.fault_type} '

    def get_absolute_url(self):
        return reverse('item_log:fault_history_list')
    class Meta:
        db_table='fault_history'
        ordering=['date', 'parts']

class CheckCompany(models.Model):
    name=models.CharField(max_length=200, null=False, blank=False, editable=True, verbose_name='검사기관')

    def get_absolute_url(self):
        return reverse('item_log:check_company_list')
    
    def __str__(self):
        return f'{self.name}'
    class Meta:
        db_table='check_company'
        ordering=['name']



class CheckHistory(models.Model):
    result_types=[('합', '적합'), ('부', ('부적합'))]
    check_type=models.CharField(max_length=200, verbose_name='검사종류')
    date=models.DateField(verbose_name='검사일', null=True, blank=True, editable=True)
    effective_duration=models.IntegerField(default=6, verbose_name='운행유효기간(개월)', null=True, blank=True, editable=True)
    inspection_agency=models.ForeignKey(CheckCompany, verbose_name='검사기관',  null=False, blank=False, editable=True, on_delete=models.DO_NOTHING)
    inspector=models.CharField(max_length=100, null=True, blank=True, editable=True, verbose_name='검사원')
    result=models.CharField(max_length=100, null=False, blank=False, editable=True, verbose_name='합격유무', choices=result_types)
    part=models.ForeignKey(Parts, on_delete=models.CASCADE, editable=True, null=True, blank=True, verbose_name='부품 시리얼')
    product=models.ForeignKey(Product, on_delete=models.CASCADE, editable=True, null=True, blank=True, verbose_name='제품 시리얼')
    
    def get_absolute_url(self):
        return reverse('item_log:check_history_list')
    class Meta:
        db_table='check_history'
        ordering=['date','product', 'part']
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_part_or_product",
                check=(
                    models.Q(part__isnull=True,product__isnull=False)|
                    models.Q(part__isnull=False,product__isnull=True)

                ),
                violation_error_message="부품이나 제품 중 하나만 선택가능합니다."
            )
        ]



class Contract(models.Model):
    part = models.ForeignKey(Parts, on_delete=models.CASCADE, editable=True, null=True, blank=True, verbose_name='부품 시리얼')
    product= models.ForeignKey(Product, on_delete=models.CASCADE, editable=True, null=True, blank=True, verbose_name='제품 시리얼')
    site_name = models.CharField(max_length=400, null=False, blank=False, editable=True, verbose_name='현장명')
    num_floors = models.IntegerField(null=True, blank=True, editable=True, verbose_name='지상층')
    num_basements = models.IntegerField(null=True, blank=True, editable=True, verbose_name='지하층')
    instalation_date=models.DateField('설치일/최초설치일',null=True, blank=True, editable=True)
    next_check_date=models.DateField('정밀안전검사예정일', null=True, blank=True, editable=True)
    withdrawal_date=models.DateField('철거예정일', null=True, blank=True,editable=True )
    safety_checker=models.CharField(max_length=200, verbose_name='안전관리자',null=True, blank=True,editable=True )
    safety_checker_phone=models.CharField(max_length=200, verbose_name='안전관리자 연락처',null=True, blank=True,editable=True )
    safety_edu_comp_date=models.DateField('안전교육 이수일', null=True, blank=True,editable=True )
    management_company=models.CharField(max_length=200, null=True, blank=True, editable=True, verbose_name='유지관리업체')
    management_comp_phone=models.CharField(max_length=200, verbose_name='유지관리업체 연락처', null=True, blank=True,editable=True )
    subcontract_company=models.CharField(max_length=200, null=True, blank=True, editable=True, verbose_name='하도급/공동수급업체')
    subcontract_comp_phone=models.CharField(max_length=200, verbose_name='하도급/공동수급업체 연락처',null=True, blank=True,editable=True )

    def get_absolute_url(self):
        return reverse('item_log:contract_list')
    class Meta:
        db_table='contract'
        ordering=['instalation_date','product', 'part']
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_part_or_product",
                check=(
                    models.Q(part__isnull=True,product__isnull=False)|
                    models.Q(part__isnull=False,product__isnull=True)

                ),
            )
        ]
    
