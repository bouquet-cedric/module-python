from setuptools import setup

setup(
    name='day_date',
    version='0.3.8',
    entry_points={
        'console_scripts': [
            # Exemple de point d'entrée de script
            'day_date=day_date:main',
        ],
    },
    requires=['colorate_console'],
    author='Bouquet Cédric',
    author_email='cedric-bouquet-7@outlook.fr',
    description="Calcule le jour de la semaine d'une date donnée",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.0',
    url='https://github.com/bouquet-cedric/module-python',
)
