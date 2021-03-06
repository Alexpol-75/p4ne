from openpyxl import load_workbook
from matplotlib import pyplot

def getv(x): return x.value

# Открыть книгу Excel
wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']

# Извлечь столбцы A, C, D
list_x = list(map(getv, sheet['A'][1:]))
list_c = list(map(getv, sheet['C'][1:]))
list_d = list(map(getv, sheet['D'][1:]))

# Построить графики
pyplot.plot(list_x, list_c, label='Temperature')
pyplot.plot(list_x, list_d, label='Sun Activity')
pyplot.legend()

# Отобразить графики
pyplot.show()
