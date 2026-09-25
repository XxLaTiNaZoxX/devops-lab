import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from promedio import calcular_promedio

def test_promedio_normal():
    assert calcular_promedio([2, 4, 6]) == 4

def test_promedio_lista_vacia():
    assert calcular_promedio([]) == 0

def test_promedio_un_elemento():
    assert calcular_promedio([10]) == 10
