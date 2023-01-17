from django.contrib import admin
from familyTree.models import *
from django.contrib.auth.models import *
# Register your models here.

admin.site.register(BigParent)
# admin.site.register(Parent)
# admin.site.register(PChild)

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display=('pSawirka','magacDhamaysiran','waalidka','number','tiradaXaasaska','magacKuGalid','password')
    # ordering: 
    search_fields=('pSawirka','magacDhamaysiran','waalidka')


@admin.register(PChild)
class PChildAdmin(admin.ModelAdmin):
    list_display=('cSawirka','magacDhamaysiran','waalidka','number','magacaHooyada','magacKuGalid','password')
    # ordering: 
    search_fields=('cSawirka','magacDhamaysiran','waalidka')
admin.site.unregister(Group)
admin.site.unregister(User)