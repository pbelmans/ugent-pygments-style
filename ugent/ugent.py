# -*- coding: utf-8 -*-
"""
    pygments.styles.ugent
    ~~~~~~~~~~~~~~~~~~~~~~

    A style based on the University of Ghent's color scheme
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Whitespace

def dec2hex(n):
    return hex(n).lstrip('0x').zfill(2)

def RGBdec2hex(r, g, b):
    return ''.join(['#', dec2hex(r), dec2hex(g), dec2hex(b)]);

class UGentStyle(Style):
    ugent_colors = {
        # Pantone 534: global
        'ugentblue': RGBdec2hex(*[36,71,127]),
        # Pantone 130: generic colour
        'ugentyellow': RGBdec2hex(*[250,178,10]),
        
        # Pantone 103c: Faculty of Literature & Philosophy
        'ugent-lw': RGBdec2hex(*[214,198,0]),
        # Pantone 485c: Faculty of Law
        'ugent-re': RGBdec2hex(*[238,39,34]),
        # Pantone 292c: Faculty of Science
        'ugent-we': RGBdec2hex(*[131,194,236]),
        # Pantone 702: Faculty of Medicine and Health Sciences
        'ugent-ge': RGBdec2hex(*[232,80,118]),
        # Pantone 272c: Faculty of Engineering and Architecture
        'ugent-tw': RGBdec2hex(*[116,121,197]),
        # Pantone 556c: Faculty of Economics and Business Administration
        'ugent-eb': RGBdec2hex(*[113,165,136]),
        # Pantone 2583c: Faculty of Veterinary Medicine
        'ugent-di': RGBdec2hex(*[145,94,182]),
        # Pantone 1655c: Faculty of Psychology and Educational Sciences
        'ugent-pp': RGBdec2hex(*[244,106,37]),
        # Pantone 3262c: Faculty of Bioscience Engineering
        'ugent-la': RGBdec2hex(*[74,194,182]),
        # Pantone purple: Faculty of Pharmaceutical Sciences
        'ugent-fw': RGBdec2hex(*[163,43,155]),
        # Pantone 375c: Faculty of Political and Social Sciences
        'ugent-ps': RGBdec2hex(*[159,217,93]),
    }
    
    default_style = ""
    
    styles = {
        Whitespace:                 '#bbbbbb',
        
        Comment:                    'italic #888888',
        Comment.Preproc:            'noitalic ' + ugent_colors['ugentblue'],
        Comment.Special:            'noitalic ' + ugent_colors['ugentblue'],
        
        Keyword:                    ugent_colors['ugent-eb'],
        Keyword.Constant:           ugent_colors['ugentblue'],
        Keyword.Pseudo:             ugent_colors['ugentblue'],
        Keyword.Reserved:           'bold ' + ugent_colors['ugent-re'],
        Keyword.Type:               'bold ' + ugent_colors['ugent-re'],
        
        Operator.Word:              ugent_colors['ugent-eb'],
        
        Name.Attribute:             ugent_colors['ugentblue'],
        Name.Builtin:               ugent_colors['ugentblue'],
        Name.Builtin.Pseudo:        'italic ' + ugent_colors['ugent-pp'],
        Name.Class:                 'bold ' + ugent_colors['ugentblue'],
        Name.Constant:              ugent_colors['ugent-pp'],
        Name.Decorator:             'italic ' + ugent_colors['ugent-re'],
        Name.Entity:                'italic ' + ugent_colors['ugent-pp'],
        Name.Exception:             ugent_colors['ugent-re'],
        Name.Function:              'bold ' + ugent_colors['ugentblue'],
        Name.Label:                 'bold ' + ugent_colors['ugent-eb'],
        Name.Namespace:             'bold ' + ugent_colors['ugentblue'],
        Name.Tag:                   ugent_colors['ugentblue'],
        Name.Variable:              'noitalic',
        
        String:                     'noitalic #5566aa',
        String.Escape:              'noitalic ' + ugent_colors['ugent-pp'],
        String.Interpol:            ugent_colors['ugent-re'],
        String.Regex:               '#cc7799',
        Number:                     '#002255',
        
        Error:                      'bg:#F00'
    }

