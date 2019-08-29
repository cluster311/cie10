# Clasificación internacional de enfermedades

Acceso a los códigos CIE. Útil para referencias simples o para importar a bases de datos con mayor capacidad de busqueda.  
Por ahora se incluye la versión 10 sin las extensiones de los paises que las tienen. Es el puntapie inicial para hacerlo.  

## Origen de los datos

Los datos se scrapearon de [la página oficial de los códigos en español](https://icdcode.info/espanol/cie-10/codigos.html) por [@verasativa](https://github.com/verasativa) y liberado [en GitHub](https://github.com/verasativa/CIE-10).  

Esta versión incluye tambien los códigos de Chile desde [deis.cl](deis.cl).  

## Instalacion

```
pip install cie
```

## Uso de la librería

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