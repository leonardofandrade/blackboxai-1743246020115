from django.db import models
from django.utils import timezone

class ProcedureType(models.Model):
    name = models.CharField('Nome', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de Procedimento'
        verbose_name_plural = 'Tipos de Procedimentos'

class DocumentType(models.Model):
    name = models.CharField('Nome', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documentos'

class ExtractionRequest(models.Model):
    request_date = models.DateTimeField('Data da Solicitação', default=timezone.now)
    requested_by = models.CharField('Solicitado por', max_length=100)
    additional_info = models.TextField('Informações Adicionais', blank=True, null=True)

    def __str__(self):
        return f'Solicitação #{self.id} - {self.requested_by}'

    class Meta:
        verbose_name = 'Solicitação de Extração'
        verbose_name_plural = 'Solicitações de Extração'

class ExtractionRequestProcedure(models.Model):
    extraction_request = models.ForeignKey(
        ExtractionRequest,
        on_delete=models.CASCADE,
        related_name='procedures',
        verbose_name='Solicitação de Extração'
    )
    procedure_type = models.ForeignKey(
        ProcedureType,
        on_delete=models.PROTECT,
        verbose_name='Tipo de Procedimento'
    )
    year = models.IntegerField('Ano')
    number = models.IntegerField('Número')
    additional_info = models.TextField('Informações Adicionais', blank=True, null=True)

    def __str__(self):
        return f'Procedimento {self.procedure_type} - {self.number}/{self.year}'

    class Meta:
        verbose_name = 'Procedimento da Solicitação'
        verbose_name_plural = 'Procedimentos da Solicitação'

class ExtractionRequestDocument(models.Model):
    extraction_request = models.ForeignKey(
        ExtractionRequest,
        on_delete=models.CASCADE,
        related_name='documents',
        verbose_name='Solicitação de Extração'
    )
    document_type = models.ForeignKey(
        DocumentType,
        on_delete=models.PROTECT,
        verbose_name='Tipo de Documento'
    )
    year = models.IntegerField('Ano')
    number = models.IntegerField('Número')
    attached_file = models.FileField('Arquivo Anexo', upload_to='documents/')
    additional_info = models.TextField('Informações Adicionais', blank=True, null=True)

    def __str__(self):
        return f'Documento {self.document_type} - {self.number}/{self.year}'

    class Meta:
        verbose_name = 'Documento da Solicitação'
        verbose_name_plural = 'Documentos da Solicitação'
