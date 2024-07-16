from setuptools import setup, find_packages

setup(
    name='colorate_console',
    version='0.3.6',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'colorize=colorate_console.colorizer:main'
        ],
    },
    author='Bouquet Cédric',
    author_email='cedric-bouquet-7@outlook.fr',
    description="Colorateur de textes dans un terminal",
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    python_requires='>=3.0',
    url='https://github.com/bouquet-cedric/module-python',
)
