from django.contrib import admin

from . import models

# Register your models here.
class FornecedoresForm(admin.ModelAdmin):
    readonly_fields = ['id_user_cad', 'id_user_alt']
    search_fields = ['razao_social', 'cnpj', 'email', 'telefone']
    # list_filter
    
    def save_model(self, request, obj, form, change):
        if change:
            obj.id_user_alt = request.user
        else:
            obj.id_user_cad = request.user
        
        obj.save()
    
admin.site.register(models.NaturezasDespesa)
admin.site.register(models.Fornecedores, FornecedoresForm)
admin.site.register(models.NotasFiscais)
admin.site.register(models.ItensNotaFiscal)
admin.site.register(models.EstadosBem)
admin.site.register(models.SituacoesUsoBem)
admin.site.register(models.Marcas)
admin.site.register(models.Bens)
admin.site.register(models.ItensOrcamento)