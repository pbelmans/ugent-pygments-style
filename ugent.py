# -*- coding: utf-8 -*-
"""
    pygments.styles.ua
    ~~~~~~~~~~~~~~~~~~~~~~

    A style based on the University of Ghent's color scheme
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Whitespace


class UGentStyle(Style):
    def dec2hex(n):
        return hex(n).lstrip('0x').zfill(2)
    
    def RGBdec2hex(r, g, b):
        return ''.join(['#', dec2hex(r), dec2hex(g), dec2hex(b)]);

    ugent_colors = {
        # Pantone 534: global
        'ugentblue': [36,71,127],
        # Pantone 130: generic colour
        'ugentyellow': [250,178,10],
        
        # Pantone 103c: Faculty of Literature & Philosophy
        'ugent-lw': [214,198,0],
        # Pantone 485c: Faculty of Law
        'ugent-re': [238,39,34],
        # Pantone 292c: Faculty of Science
        'ugent-we': [131,194,236],
        # Pantone 702: Faculty of Medicine and Health Sciences
        'ugent-ge': [232,80,118],
        # Pantone 272c: Faculty of Engineering and Architecture
        'ugent-tw': [116,121,197],
        # Pantone 556c: Faculty of Economics and Business Administration
        'ugent-eb': [113,165,136],
        # Pantone 2583c: Faculty of Veterinary Medicine
        'ugent-di': [145,94,182],
        # Pantone 1655c: Faculty of Psychology and Educational Sciences
        'ugent-pp': [244,106,37],
        # Pantone 3262c: Faculty of Bioscience Engineering
        'ugent-la': [74,194,182],
        # Pantone purple: Faculty of Pharmaceutical Sciences
        'ugent-fw': [163,43,155],
        # Pantone 375c: Faculty of Political and Social Sciences
        'ugent-ps': [159,217,93],
    }
    
    default_style = ""
    
    uablue = '#003d64'
    uared = '#7e002f'
    vividbrown = '#d79a46'
    green = '#007e11'
    
    styles = {
        Whitespace:                 '#bbbbbb',
        
        Comment:                    'italic #888888',
        Comment.Preproc:            'noitalic ' + uablue,
        Comment.Special:            'noitalic ' + uablue,
        
        Keyword:                    green,
        Keyword.Constant:           uablue,
        Keyword.Pseudo:             uablue,
        Keyword.Reserved:           'bold ' + uared,
        Keyword.Type:               'bold ' + uared,
        
        Operator.Word:              green,
        
        Name.Attribute:             uablue, 
        Name.Builtin:               uablue,
        Name.Builtin.Pseudo:        'italic ' + vividbrown,
        Name.Class:                 'bold ' + uablue,
        Name.Constant:              vividbrown,
        Name.Decorator:             'italic ' + uared,
        Name.Entity:                'italic ' + vividbrown,
        Name.Exception:             uared,
        Name.Function:              'bold ' + uablue,
        Name.Label:                 'bold ' + green,
        Name.Namespace:             'bold ' + uablue,
        Name.Tag:                   uablue,
        Name.Variable:              'noitalic',
        
        String:                     'noitalic #5566aa',
        String.Escape:              'noitalic ' + vividbrown,
        String.Interpol:            uared,
        String.Regex:               '#cc7799',
        Number:                     '#002255',
        
        Error:                      'bg:#F00'
    }

