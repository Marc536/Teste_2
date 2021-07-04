a = []

for i in range(10):
    a.append(int(input("Digite o %dº número:\n" % (i+1))))

soma = 0

for i in range(len(a)):
    soma = soma + a[i]

print("A soma total dos números inseridos foi de: %d\n" % (soma))