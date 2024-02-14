import numpy as np
import pandas as pd
def aprobados(notas):
    notas = pd.Series(notas)
    return notas[notas>= 5].sort_values(ascending=False)

notas={'pepe':9,'juan':10}
print(aprobados(notas))
print(np.arange(0,10))