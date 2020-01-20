# Clasificación internacional de enfermedades

Acceso a los códigos CIE. Útil para referencias simples o para importar a bases de datos con mayor capacidad de busqueda.  
Por ahora se incluye la versión 10 sin las extensiones de los paises que las tienen. Es el puntapie inicial para hacerlo.  

## Origen de los datos

Los datos se scrapearon de [la página oficial de los códigos en español](https://icdcode.info/espanol/cie-10/codigos.html) por [@verasativa](https://github.com/verasativa) y liberado [en GitHub](https://github.com/verasativa/CIE-10).  

Esta versión incluye tambien los códigos de Chile desde [deis.cl](http://www.deis.cl/).  

## Instalacion

```
pip install cie
```

## Uso de la librería stand-alone

```python
from cie.cie10 import CIECodes
cie = CIECodes()
print(cie.info(code='X511'))
print(cie.info(code='C02.0'))
```

```
{
    'code': 'X511',
	'description': 'Viajes y desplazamientos: institucion residencial',
	'source': 'deis.cl',
	'level': 5,
	'depends_on': 'X51',
	'multiple_descriptions': ['Viajes y desplazamientos: institucion residencial', 'Viajes y desplazamientos', 'Exceso de esfuerzo, viajes y privación', 'Otras causas externas de traumatismos accidentales', 'Accidentes', 'Causas externas de morbilidad y de mortalidad']
}

{
    'code': 'C020',
	'description': 'Tumor maligno de la cara dorsal de la lengua',
	'source': 'icdcode.info',
	'level': 5,
	'depends_on': 'C02',
	'multiple_descriptions': ['Tumor maligno de la cara dorsal de la lengua', 'Tumor maligno de otras partes y de las no especificadas de la lengua', 'y de la faringe', 'y afines', 'Tumores [neoplasias] malignos', 'Tumores [neoplasias]']
}
```

## Listar valores

```python
from cie.cie10 import CIECodes
cie = CIECodes()
for code, content in cie.tree.items():
    full_info = cie.info(code=code)  # load the 'multiple_descriptions' prop
    print(code, full_info['description'])
```

```

... 

Y778 Dispositivos oftalmicos asociados con incidentes adversos: dispositivos diversos, no clasificados en otra parte
Y780 Aparatos radiologicos asociados con incidentes adversos: dispositivos de diagnostico y monitoreo
Y781 Aparatos radiologicos asociados con incidentes adversos: dispositivos terapeuticos (no quirurgicos) y de rehabilitacion
Y782 Aparatos radiologicos asociados con incidentes adversos: dispositivos protesicos y otros implantes, materiales y accesorios
Y783 Aparatos radiologicos asociados con incidentes adversos: instrumentos quirurgicos, dispositivos y materiales (inclusive suturas)
Y788 Aparatos radiologicos asociados con incidentes adversos: dispositivos diversos, no clasificados en otra parte
Y790 Dispositivos ortopedicos asociados con incidentes adversos: dispositivos de diagnostico y monitoreo

... 

```

## Buscar códigos

```python
from cie.cie10 import CIECodes
cie = CIECodes()
for code in cie.search(txt='kaposi'):
    print(code)
```


```
{'description': 'Enfermedad por VIH, resultante en sarcoma de Kaposi', 'source': 'icdcode.info', 'level': 3, 'depends_on': 'B21', 'multiple_descriptions': ['Enfermedad por VIH, resultante en sarcoma de Kaposi', 'Enfermedad por virus de la inmunodeficiencia humana [VIH], resultante en tumores malignos', 'Enfermedad por virus de la inmunodeficiencia \xadhumana [VIH]', 'Ciertas enfermedades infecciosas y parasitarias'], 'code': 'B210'}
{'description': 'Sarcoma de Kaposi', 'source': 'icdcode.info', 'level': 4, 'depends_on': 'C45-C49', 'multiple_descriptions': ['Sarcoma de Kaposi', 'Tumores malignos de los tejidos mesoteliales y de los tejidos blandos', 'y afines', 'Tumores [neoplasias] malignos', 'Tumores [neoplasias]'], 'code': 'C46'}
{'description': 'Sarcoma de Kaposi de la piel', 'source': 'icdcode.info', 'level': 5, 'depends_on': 'C46', 'multiple_descriptions': ['Sarcoma de Kaposi de la piel', 'Sarcoma de Kaposi', 'Tumores malignos de los tejidos mesoteliales y de los tejidos blandos', 'y afines', 'Tumores [neoplasias] malignos', 'Tumores [neoplasias]'], 'code': 'C460'}
{'description': 'Sarcoma de Kaposi del tejido blando', 'source': 'icdcode.info', 'level': 5, 'depends_on': 'C46', 'multiple_descriptions': ['Sarcoma de Kaposi del tejido blando', 'Sarcoma de Kaposi', 'Tumores malignos de los tejidos mesoteliales y de los tejidos blandos', 'y afines', 'Tumores [neoplasias] malignos', 'Tumores [neoplasias]'], 'code': 'C461'}
{'description': 'Sarcoma de Kaposi del paladar', 'source': 'icdcode.info', 'level': 5, 'depends_on': 'C46', 'multiple_descriptions': ['Sarcoma de Kaposi del paladar', 'Sarcoma de Kaposi', 'Tumores malignos de los tejidos mesoteliales y de los tejidos blandos', 'y afines', 'Tumores [neoplasias] malignos', 'Tumores [neoplasias]'], 'code': 'C462'}
{'description': 'Sarcoma de Kaposi de los ganglios linfáticos', 'source': 'icdcode.info', 'level': 5, 'depends_on': 'C46', 'multiple_descriptions': ['Sarcoma de Kaposi de los ganglios linfáticos', 'Sarcoma de Kaposi', 'Tumores malignos de los tejidos mesoteliales y de los tejidos blandos', 'y afines', 'Tumores [neoplasias] malignos', 'Tumores [neoplasias]'], 'code': 'C463'}
{'description': 'Sarcoma de Kaposi de otros sitios especificados', 'source': 'icdcode.info', 'level': 5, 'depends_on': 'C46', 'multiple_descriptions': ['Sarcoma de Kaposi de otros sitios especificados', 'Sarcoma de Kaposi', 'Tumores malignos de los tejidos mesoteliales y de los tejidos blandos', 'y afines', 'Tumores [neoplasias] malignos', 'Tumores [neoplasias]'], 'code': 'C467'}
{'description': 'Sarcoma de Kaposi de múltiples órganos', 'source': 'icdcode.info', 'level': 5, 'depends_on': 'C46', 'multiple_descriptions': ['Sarcoma de Kaposi de múltiples órganos', 'Sarcoma de Kaposi', 'Tumores malignos de los tejidos mesoteliales y de los tejidos blandos', 'y afines', 'Tumores [neoplasias] malignos', 'Tumores [neoplasias]'], 'code': 'C468'}
{'description': 'Sarcoma de Kaposi, de sitio no especificado', 'source': 'icdcode.info', 'level': 5, 'depends_on': 'C46', 'multiple_descriptions': ['Sarcoma de Kaposi, de sitio no especificado', 'Sarcoma de Kaposi', 'Tumores malignos de los tejidos mesoteliales y de los tejidos blandos', 'y afines', 'Tumores [neoplasias] malignos', 'Tumores [neoplasias]'], 'code': 'C469'}
```


## Uso de la librería como aplicación Django

Registra la aplicación


```
INSTALLED_APPS = (
    ...
    'cie10_django',
    ...
)
```

Migra los datos para crear la tabla e importar los datos al modelo. 

```
python manage.py migrate cie10_django
```

Uso:

```python
from cie10_django.models import CIE10
# cargar todos los datos a la base.
CIE10.start_db()

...

INFO 14472 Imporatando código Y773
INFO 14473 Imporatando código Y778
INFO 14474 Imporatando código Y780
...
14498 codigos

# ya se pueden ver los códigos en el admin de Django

# ejemplo de uso
x511 = CIE10.objects.get(code='X511')

```
