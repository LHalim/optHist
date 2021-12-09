import numpy as np
import matplotlib.pyplot as plt
import niceplots
import os

dir_name = "/home/lhalim/git/optHist/tacs_results"
direct = os.listdir(dir_name)

for item in direct:
    if item.endswith(".png"):
        os.remove(os.path.join(dir_name, item))

jobs = [1,2]
jobs = [1]

for number in jobs:
    lines = []
    with open('optHist' + str(number) + '.txt') as f:
        lines = f.readlines()

    vec_KS = [2]

    if number in vec_KS:
        objFunc = 'KSFailure'
    else:
        objFunc = 'Temperature'

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

    plt.plot(iterations, funcValues,color='C1')
    plt.xlabel('Iterations')
    plt.ylabel(objFunc)
    plt.savefig('TACS_' + objFunc + '_CH.png')
    plt.clf()
    #plt.show()


