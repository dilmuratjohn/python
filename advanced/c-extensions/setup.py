from distutils.core import setup, Extension

module = Extension('myModule', soures = ['myModule.c'])

setup(name = 'PackageName',version = '1.0', description = 'This is a package for myModule', ext_modules = [module])
