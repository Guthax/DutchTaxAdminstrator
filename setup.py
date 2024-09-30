from setuptools import setup

requirements = [
    # TODO: put your package requirements here
    "PyQt6",
    "jsonpickle"
]

setup(
    name='DutchTaxAdministrator',
    version='0.0.1',
    description="Software for tax administration for zzp",
    author="NA",
    author_email='NA',
    url='https://github.com/guthax/DutchTaxAdministrator',
    packages=['dutchtaxadministrator', 'dutchtaxadministrator.images',
              'dutchtaxadministrator.tests'],
    package_data={'dutchtaxadministrator.images': ['*.png']},
    entry_points={
        'console_scripts': [
            'DutchTaxAdministrator=dutchtaxadministrator.DutchTaxAdministrator:main'
        ]
    },
    install_requires=requirements,
    zip_safe=False,
    keywords='DutchTaxAdministrator',
    classifiers=[
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
