'''
Autor: Ibon Reinoso y Alumnos Las Palmas
Fecha: 15/06/2023
Contacto: BigBayData.com

'''


def calcularRecall(matrix):
    '''
    Dada una Matriz 2x2...
    # A   B
    # C   D 
    '''
    valA = matrix[0][0]
    valB = matrix[0][-1]
    valC = matrix[-1][0]
    valD = matrix[-1][-1]
    recall1 = valA / (valA + valB)
    recall2 = valD / (valC + valD)
    return (recall1 + recall2) / 2

def calcularAccuracy(matrix):
    '''
    Dada una Matriz 2x2...
    # A   B
    # C   D 
    '''
    valA = matrix[0][0]
    valB = matrix[0][-1]
    valC = matrix[-1][0]
    valD = matrix[-1][-1]
    return (valA + valD) / (valA + valB + valC + valD)
    
def calcularPrecission(matrix):
    '''
    Dada una Matriz 2x2...
    # A   B
    # C   D 
    '''
    valA = matrix[0][0]
    valB = matrix[0][-1]
    valC = matrix[-1][0]
    valD = matrix[-1][-1]
    prec1 = valA / (valA + valC)
    prec2 = valD / (valB + valD)
    return (prec1 + prec2) / 2

def calcularF1(matrix):
    recall, precission = calcularRecall(matrix) , calcularPrecission(matrix)
    return (2 * recall * precission) / (recall + precission)


'''
A continuación, se muestran las dos matrices de confusión 2x2

de los dos modelos.

'''    
MATRIZ_IN_1 = [
    [ 100, 5  ], # A, B
    [ 15, 300 ]  # C, D
    ]

MATRIZ_IN_2 = [
    [ 90, 105  ], # A, B
    [ 25, 200 ]  # C, D
    ]

print('INPUT: MATRIZ_IN_1         vs        MATRIZ_IN_2')
print('##################################################')
print( 'Acc:',calcularAccuracy(MATRIZ_IN_1),'    ', calcularAccuracy(MATRIZ_IN_2) )
print( 'Rec.:',calcularRecall(MATRIZ_IN_1),'    ', calcularRecall(MATRIZ_IN_2) )
print( 'Prec:',calcularPrecission(MATRIZ_IN_1),'    ', calcularPrecission(MATRIZ_IN_2) )
print( 'F1_: ',calcularF1(MATRIZ_IN_1), '    ',calcularF1(MATRIZ_IN_2))
