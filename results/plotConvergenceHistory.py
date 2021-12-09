import matplotlib.pyplot as plt
import niceplots

number = str(28)

lines = []
with open('optHist' + number + '.txt') as f:
    lines = f.readlines()

case = 'Aerothermal'
objFunc = 'Temperature'

iteration = 0
iterations = []
funcValues = []
for index, line in enumerate(lines):
    if line[0:15]=='Objective Value':
        iteration += 1
        iterations.append(iteration)
        funcValues.append(float(line[20:]))

print(iterations)
print(funcValues)

scalingFactor = 1 #0.010686
for index, funcValue in enumerate(funcValues):
    funcValues[index] = funcValues[index]*scalingFactor

niceplots.setRCParams()

plt.plot(iterations, funcValues)
plt.xlabel('Iterations')
plt.ylabel(objFunc)
plt.savefig(case + '_' + objFunc + number + '.png')
#plt.show()


