import matplotlib.pyplot as plt

lines = []
with open('optHist27.txt') as f:
    lines = f.readlines()

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

scalingFactor = 0.010686
for index, funcValue in enumerate(funcValues):
    funcValues[index] = funcValues[index]*scalingFactor

plt.plot(iterations, funcValues)
plt.xlabel('Iterations')
plt.ylabel('KSFailure')
plt.title('Optimization Convergence History of Subsonic Aerothermal KSFailure  Minimization')
plt.show()
        
