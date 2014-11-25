from django.contrib import admin
from polls.models import Products, Sublevels, WMP_Phases, Subcomponents, ID_mapping, DCM_Phases, TDD_LTE_Phases, WMP_cplane_Phases, WMP_dl_phy_Phases


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'product_name', 'bu_name')
    
    fieldsets = [
        ('Please input ID:',    {'fields': ['product_id']}),
        ('Please provide name Information:',    {'fields': ['product_name', 'bu_name']}),
        ]

class WMP_PhasesAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'entity_build', 'QT_sanity_minorRegression_SWBT', 'majorRegression', 'fullRegression', 'neve', 'timestamp', 'contact_name')
    
class DCM_PhasesAdmin(WMP_PhasesAdmin):
    pass    

class TDD_LTE_PhasesAdmin(WMP_PhasesAdmin):
    pass

    
admin.site.register(Products, ProductsAdmin)

admin.site.register(Sublevels)

admin.site.register(Subcomponents)

admin.site.register(ID_mapping)

admin.site.register(WMP_Phases, WMP_PhasesAdmin)

admin.site.register(DCM_Phases, DCM_PhasesAdmin)

admin.site.register(TDD_LTE_Phases, TDD_LTE_PhasesAdmin)

admin.site.register(WMP_cplane_Phases)

admin.site.register(WMP_dl_phy_Phases)
