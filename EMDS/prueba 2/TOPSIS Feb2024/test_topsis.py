import numpy as np
import pandas as pd
from main import calculate_weighted_matrix  # Reemplaza 'tu_script' con el nombre de tu archivo de script

def test_calculate_weighted_matrix():
    # Define datos de prueba
    normalized_matrix = pd.DataFrame({
        'C1': [0.1, 0.2, 0.3],
        'C2': [0.3, 0.2, 0.1],
        'C3': [0.5, 0.5, 0.5],
        'C4': [0.2, 0.3, 0.4],
        'C5': [0.4, 0.4, 0.4]
    })

    weights = pd.Series([0.2, 0.3, 0.1, 0.2, 0.2])

    # Calcular la matriz ponderada
    weighted_matrix = calculate_weighted_matrix(normalized_matrix, weights)

    # Verificar los cálculos
    expected_weighted_matrix = pd.DataFrame({
        'C1': [0.02, 0.06, 0.03],
        'C2': [0.06, 0.06, 0.01],
        'C3': [0.005, 0.015, 0.005],
        'C4': [0.04, 0.09, 0.04],
        'C5': [0.08, 0.12, 0.08]
    })