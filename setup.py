""" 
A UGent style for Pygments
""" 
from setuptools import setup 

setup( 
    name         = 'ugent', 
    version      = '1.1', 
    description  = __doc__, 
    author       = "Pieter Belmans", 
    install_requires = ['pygments'],
    packages     = ['ugent'], 
    entry_points = '''
    [pygments.styles]
    ugent = ugent:UGentStyle
    '''
) 
