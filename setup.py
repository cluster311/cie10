import setuptools

print(setuptools.find_packages())

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='cie',
    version='0.207',
    license='MIT',
    author="Andrés Vazquez",
    author_email="andres@data99.com.ar",
    description="Lista de Códigos CIE10 en español como librería python simple o para uso dentro de django como app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cluster311/cie10",
    include_package_data=True,  # for ZIP file
    packages=['cie', 'cie10_django'],
    extras_require={
        'django':  ["Django>=1.11"],
    },
    classifiers=[
     'Programming Language :: Python :: 3',
     'Programming Language :: Python :: 3.6',
     'License :: OSI Approved :: MIT License',
     'Operating System :: OS Independent',
     'Intended Audience :: Developers',
     'Framework :: Django',
     'Framework :: Django :: 2.2',
    ],
    python_requires='>=3.6',
)
