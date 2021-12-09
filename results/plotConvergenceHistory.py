import numpy as np
import matplotlib.pyplot as plt
import niceplots
import os

dir_name = "/home/lhalim/git/optHist/results"
direct = os.listdir(dir_name)

for item in direct:
    if item.endswith(".png"):
        os.remove(os.path.join(dir_name, item))

jobs = [19,20,22,23,27,28,29,33,34,35]
jobs = [19,20,22,23,27,28,29]

for number in jobs:
    lines = []
    with open('optHist' + str(number) + '.txt') as f:
        lines = f.readlines()

    vec_ATE = [19,20,22,23]
    vec_AT = [27,28,33,34]
    vec_KS = [19,22,27,29,33,35]
    vec_SUB = [19,20,27,28,29]

    if number in vec_ATE:
        case = 'Aerothermoelastic'
    elif number in vec_AT:
        case = 'Aerothermal'
    else:
        case = 'Aeroelastic'

    if number in vec_KS:
        objFunc = 'KSFailure'
    else:
        objFunc = 'Temperature'

    if number in vec_SUB:
        regime = 'Subsonic'
    else:
        regime = 'Supersonic'

    iteration = 0
    iterations = []
    funcValues = []
    for index, line in enumerate(lines):
        if line[0:15]=='Objective Value':
            iteration += 1
            iterations.append(iteration)
            funcValues.append(float(line[20:]))

    #print(iterations)
    #print(funcValues)

    scalingFactor = 1 #0.010686
    for index, funcValue in enumerate(funcValues):
        funcValues[index] = funcValues[index]*scalingFactor

    niceplots.setRCParams()

    plt.plot(iterations, funcValues)
    plt.xlabel('Iterations')
    plt.ylabel(objFunc)
    plt.savefig(case + '_' + objFunc + '_' + regime + '.png')
    plt.clf()
    #plt.show()


