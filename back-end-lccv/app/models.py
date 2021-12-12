from enum import unique
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NaturezasDespesa(models.Model):
    id_natureza_despesa = models.AutoField(primary_key=True)
    cod_natureza_despesa = models.CharField(max_length=8)
    desc_natureza_despesa = models.CharField(max_length=60)
    
    def __str__(self) -> str:
        return self.desc_natureza_despesa

class Fornecedores(models.Model):
    id_fornecedor = models.AutoField(primary_key=True)
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=20)
    id_user_cad = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'user_cad')
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'user_alt', null=True)
    dt_cad = models.DateField(null=True, blank=True, auto_now=True)

    def __str__(self) -> str:
        return self.razao_social
    
class NotasFiscais(models.Model):
    id_nota_fiscal = models.AutoField(primary_key=True)
    id_fornecedor = models.ForeignKey(Fornecedores, on_delete=models.Case)
    id_natureza_despesa = models.ForeignKey(NaturezasDespesa, on_delete=models.Case)
    numero = models.IntegerField()
    ano = models.IntegerField()
    id_user_cad = models.ForeignKey(User, on_delete=models.CASCADE, related_name= '%(class)s_user_cad')
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.ForeignKey(User, on_delete=models.CASCADE, related_name= '%(class)s_user_alt', null=True)
    dt_cad = models.DateField(null=True, blank=True, auto_now=True)
    
    def __str__(self) -> str:
        return str(self.id_fornecedor) + '/' + str(self.id_natureza_despesa)

class ItensNotaFiscal(models.Model):
    id_item_nota_fiscal = models.AutoField(primary_key=True)
    id_nota_fiscal = models.ForeignKey(NotasFiscais, on_delete=models.Case)
    qtd = models.IntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    produto_servico = models.CharField(max_length=100)
    vinculado = models.CharField(max_length=1)
    id_user_cad = models.ForeignKey(User, on_delete=models.CASCADE, related_name= '%(class)s_user_cad')
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.ForeignKey(User, on_delete=models.CASCADE, related_name= '%(class)s_user_alt', null=True)
    dt_cad = models.DateField(null=True, blank=True, auto_now=True)
    
    def __str__(self) -> str:
        return str(self.id_nota_fiscal) + '/' + str(self.qtd)
    
class EstadosBem(models.Model):
    id_estado_bem = models.AutoField(primary_key=True)
    estado_bem = models.CharField(max_length=80)
    descricao = models.CharField(max_length=255)
    ativo = models.CharField(max_length=1)
    
    def __str__(self) -> str:
        return self.estado_bem
    
class SituacoesUsoBem(models.Model):
    id_situacao_uso_bem = models.AutoField(primary_key=True)
    situacao_uso_bem = models.CharField(max_length=80)
    descricao = models.CharField(max_length=255)
    ativo = models.CharField(max_length=1)
    
    def __str__(self) -> str:
        return self.situacao_uso_bem
    
class Marcas(models.Model):
    id_marca = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=80)
    id_user_cad = models.ForeignKey(User, on_delete=models.CASCADE, related_name= '%(class)s_user_cad')
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.ForeignKey(User, on_delete=models.CASCADE, related_name= '%(class)s_user_alt', null=True)
    dt_cad = models.DateField(null=True, blank=True, auto_now=True)
    
    def __str__(self) -> str:
        return self.marca
    
class Bens(models.Model):
    id_bem = models.AutoField(primary_key=True)
    id_nota_fiscal = models.ForeignKey(NotasFiscais, on_delete=models.Case)
    tombamento = models.CharField(max_length=10)
    id_estado_bem = models.ForeignKey(EstadosBem, on_delete=models.Case)
    id_situacao_uso_bem = models.ForeignKey(SituacoesUsoBem, on_delete=models.Case)
    valor_aquisicao = models.DecimalField(max_digits=7, decimal_places=2)
    id_marca = models.ForeignKey(Marcas, on_delete=models.Case)
    data_lim_garantia = models.DateField()
    data_fim_garantia = models.DateField()
    data_inicio_uso = models.DateField()
    observacoes = models.TextField()
    id_user_cad = models.ForeignKey(User, on_delete=models.CASCADE, related_name= '%(class)s_user_cad')
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.ForeignKey(User, on_delete=models.CASCADE, related_name= '%(class)s_user_alt', null=True)
    dt_cad = models.DateField(null=True, blank=True, auto_now=True)
        
        
class ItensOrcamento(models.Model):
    id_item_orcamento = models.AutoField(primary_key=True)
    id_orcamento_id = models.AutoField
    id_produto_id = models.AutoField
    qtd = models.IntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    id_user_cad = models.ForeignKey(User, on_delete=models.CASCADE, related_name= '%(class)s_user_cad')
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.ForeignKey(User, on_delete=models.CASCADE, related_name= '%(class)s_user_alt', null=True)
    dt_cad = models.DateField(null=True, blank=True, auto_now=True)
    
    