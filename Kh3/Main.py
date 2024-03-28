import json
from Fabric import Fabric
import numpy
import matplotlib.pyplot as plt


with open('E-R.json') as param:
    templates = json.load(param)  # подгружаем оттуда информацию

time_of_modeling = templates['time_of_modeling'] #как словарь
step = templates['step']
sum_of_elems = templates['sum_of_elems']
elements = [Fabric.serialize(templates['elems'][str(i)], step) for i in range(templates['sum_of_elems'])] #массив из элементов обращаясь к Fabric ,открывает доступ к elems , шаг расчета

nodes = [] #иницализация массива, для хранения узлов

for i in range(sum_of_elems):
    if elements[i].get_node_start() not in nodes: #если узла начала нет , то добавляем
        nodes.append(elements[i].get_node_start())
    if elements[i].get_node_end() not in nodes:#если узла конца нет , то добавляю 
        nodes.append(elements[i].get_node_end())

nodes = tuple(sorted(nodes)) #создание кортежа

matrixA = numpy.eye((len(nodes) - 1), sum_of_elems)  # numpy.eye создает матрицу с еденицами по главной диагонали

# Заполнение матрицы
for i in range(len(nodes) - 1):
    for j in range(sum_of_elems):
        if elements[j].get_node_end() == i + 1:
            matrixA[i][j] = 1
        elif elements[j].get_node_start() == i + 1:
            matrixA[i][j] = -1
        else:
            matrixA[i][j] = 0

# создаем транспонируемую матрицу
matrixAt = numpy.transpose(matrixA)

# создаем матрицу проводимостей
matrixY = numpy.eye(sum_of_elems, sum_of_elems)

for i in range(len(elements)):
    matrixY[i][i] = (1 / (elements[i].get_impedance()))

# создаем матрицу E
matrixE = numpy.zeros(sum_of_elems)
matrixE = matrixE[:, numpy.newaxis] #делаем вектор стоблец

def set_matrixE(matrixE, elements, quantity, t):
    for i in range(quantity):
        matrixE[i][0] = elements[i].get_volt(t)
    return matrixE

matrixJ = numpy.zeros(sum_of_elems)

for i in range(sum_of_elems):
    matrixJ[i] = elements[i].get_circuit()

matrixJ = matrixJ[:, numpy.newaxis]

def calculate(matrixA, matrixAt, matrixY, matrixE, matrixJ):
    matrixAY = numpy.dot(matrixA, matrixY) # перемножение
    matrixAYAt = numpy.dot(matrixAY, matrixAt)
    matrixYE = numpy.dot(matrixY, matrixE)
    matrixJ_YE = matrixJ + matrixYE
    matrix_minus_A = (-1) * matrixA 
    marixA_J_YE = numpy.dot(matrix_minus_A, matrixJ_YE)

    return numpy.linalg.solve(matrixAYAt, marixA_J_YE)

def set_new_fi(uzl, quantity, elems, Fi):
    for j in range(len(uzl) - 1):
        for i in range(quantity):
            if elems[i].get_node_start() == j + 1:
                elems[i].set_fi_start(Fi[j][0])
            elif elems[i].get_node_end() == j + 1:
                elems[i].set_fi_end(Fi[j][0])
            elif elems[i].get_node_start() == uzl[len(uzl) - 1]:
                elems[i].set_fi_start(0)
            elif elems[i].get_node_end() == uzl[len(uzl) - 1]:
                elems[i].set_fi_end(0)

def set_new_param(quantity, elems):
    for i in range(quantity):
        elems[i].set_current()
        elems[i].set_volt()

array_of_circuits = [0]
array_of_times = [0]
array_of_volt = [0]
time = 0


while (time < time_of_modeling):
    matrixE = set_matrixE(matrixE, elements, sum_of_elems,time)
    matrixFi = calculate(matrixA, matrixAt, matrixY, matrixE, matrixJ)
    set_new_fi(nodes, sum_of_elems, elements, matrixFi)
    set_new_param(sum_of_elems, elements)
    array_of_volt.append(elements[1].get_volt_for_graph())
    array_of_times.append(time)
    array_of_circuits.append(elements[1].get_current_for_graph())
    time += step


fig, ax = plt.subplots()
ax.plot(array_of_times, array_of_circuits, label="I(t)")  # Данные осей
ax.plot(array_of_times, array_of_volt, label="U(t)")
ax.set_ylabel('Ток,А / Напряжение, В')
ax.set_xlabel('Время, с')
ax.legend()
ax.minorticks_on()
plt.show()