# -*- coding: utf-8 -*-
from unicodedata import normalize

class formattString:

    @staticmethod
    def strFormatt(string):
        string = formattString.get_tirar_url(string)
        string = formattString.remover_acentos(string)
        string = formattString.unwanted_character(string)

        return string

    @staticmethod
    def get_tirar_url(str):
        vaRetorno = ' '.join(i for i in str.split() if not ('https://' or 'http://') in i)
        vaRetorno = ' '.join(i for i in vaRetorno.split() if not ('@') in i)

        return vaRetorno
    @staticmethod
    def remover_acentos(txt, codif='utf-8'):
        return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')
    @staticmethod
    def unwanted_character(s):
        chars_to_remove = ['a', 'ao', 'ja', 'antes', 'após', 'ate', 'com', 'contra', 'de', 'desde', 'em', 'entre', 'para', 'per','perante']
        chars_to_remove += ['por', 'sem', 'sob', 'sobre', 'trás', 'aquela', 'dum', 'nisto']
        chars_to_remove += ['da', 'um', 'uns', 'uma', 'por', 'e', 'do', 'umas', 'que', 'como', 'do', 'aquele', 'no', 'na', 'nos']
        chars_to_remove += ['-', '_', 'tem', 'muito', 'que', 'o', 'seu', 'nosso', 'pelo', 'pela', 'os', 'te', 'eu', 'ou', 'nosso', 'vosso', 'tu']
        chars_to_remove += ['todo', 'das', 'dos', 'os', 'as', 'se', 'voce']

        return ' '.join([c for c in s.split() if c not in chars_to_remove])


