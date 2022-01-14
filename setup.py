from setuptools import setup, find_packages


setup(
    name='various_utilities',
    version='0.1',
    license='MIT', # TODO: add license
    author="Cristian Desivo",
    author_email='cdesivo92@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='', # TODO: add url
    keywords='utilities',
    install_requires=[
      ],
)
