import psutil

def getCPU():
    return psutil.cpu_percent(interval=1, percpu=True)
    
def numberCPU():
    return psutil.cpu_count(logical=True)

print("Núcleos: {}".format(numberCPU()))

while(1):
    # Atualizar linha sem criar nova
    print("Percentual de uso: {}".format(getCPU()))