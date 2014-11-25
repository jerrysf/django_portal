from django.db import models

class Products(models.Model):
    product_id = models.IntegerField(default=0)
    product_name = models.CharField(max_length=200)
    bu_name = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Products'
    
class Sublevels(models.Model):
    sublevel_id = models.IntegerField(default=0)
    sublevel_name = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = 'Sub Levels'
        verbose_name_plural = 'Sub Levels'
    
class Subcomponents(models.Model):
    subcomponent_id = models.IntegerField(default=0)
    subcomponent_name = models.CharField(max_length=200)    

    class Meta:
        verbose_name = 'Sub Components'
        verbose_name_plural = 'Sub Components'
    
class ID_mapping(models.Model):
    subcomponent_id = models.IntegerField(default=0)
    product_id = models.IntegerField(default=0)
    sublevel_id = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'ID Mapping'
        verbose_name_plural = 'ID Mapping'    
    
class Product_Phases(models.Model):
    product_id = models.IntegerField()
    entity_build = models.IntegerField()
    QT_sanity_minorRegression_SWBT = models.IntegerField()
    majorRegression = models.IntegerField()
    fullRegression = models.IntegerField()
    neve = models.IntegerField()
    timestamp = models.DateTimeField('data upload time')
    contact_name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Product Phases'
        verbose_name_plural = 'Product Phases' 
    
class Subcomponent_Phases(models.Model):
    subcomponent_id = models.IntegerField(default=0)
    component_CI_pre_commit_phase = models.IntegerField()
    UT_MT = models.IntegerField()
    SCT_build = models.IntegerField()
    SCT_FT = models.IntegerField()
    Promotion = models.IntegerField()
    Additional = models.IntegerField()
    timeStamp = models.DateTimeField('data upload time')
    contact_name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Subcomponent Phases'
        verbose_name_plural = 'Subcomponent Phases'     
    
class Sublevel_Phases(models.Model):
    sublevel_id = models.IntegerField(default=0)
    entity_build = models.IntegerField()
    QT_sanity_minorRegression_SWBT = models.IntegerField()
    fullRegression = models.IntegerField()
    neve = models.IntegerField()
    timestamp = models.DateTimeField('data upload time')
    contact_name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Sublevel Phases'
        verbose_name_plural = 'Sublevel Phases' 
    
class WMP_Phases(Product_Phases):

    class Meta:
        verbose_name = 'WMP Phases'
        verbose_name_plural = 'WMP Phases' 
    
class DCM_Phases(Product_Phases):

    class Meta:
        verbose_name = 'DCM Phases'
        verbose_name_plural = 'DCM Phases' 
    
class TDD_LTE_Phases(Product_Phases):

    class Meta:
        verbose_name = 'TDD-LTE Phases'
        verbose_name_plural = 'TDD-LTE Phases' 

class WMP_cplane_Phases(Sublevel_Phases):

    class Meta:
        verbose_name = 'WMP Cplane Phases'
        verbose_name_plural = 'WMP Cplane Phases' 

class WMP_dl_phy_Phases(Subcomponent_Phases):

    class Meta:
        verbose_name = 'WMP dl phy Phases'
        verbose_name_plural = 'WMP dl phy Phases'   
    