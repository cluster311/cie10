from django.db import models
import logging
logger = logging.getLogger(__name__)


class Source(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class CIE10(models.Model):
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(null=True, blank=True)
    depends_on = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    level = models.IntegerField(default=0)
    source = models.ForeignKey(Source, null=True, blank=True, on_delete=models.SET_NULL, related_name='codes')

    def __str__(self):
        return self.code

    @classmethod
    def start_db(cls):
        logger.info('Comenzando importacion de códigos CIE10')
        from cie.cie10 import CIECodes
        cie = CIECodes()
        c = 0
        for code, content in cie.tree.items():
            c += 1
            logger.info(f'{c} Imporatando código {code}')
            source, created = Source.objects.get_or_create(name=content['source'])
            c10, created = CIE10.objects.get_or_create(code=code)
            c10.description = content['description']
            c10.source = source
            c10.level = content['level']
            c10.save()
        
        for code, content in cie.tree.items():
            logger.info(f'Vinculando código {code}')
            c10 = CIE10.objects.get(code=code)
            if c10.level > 0:
                depon_code = content.get('depends_on', '')    
                depon = CIE10.objects.get(code=depon_code)
                c10.depends_on = depon
                c10.save()
        
        return c