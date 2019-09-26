import random, time, threading
import psutil
from tqdm import tqdm

'''
@author Matheus Carvalho, Yukiko Sasaki
'''

# Definicao do numero de iteracoes desejados
NUMBER_OF_ITERATIONS = 100


class MyThread(threading.Thread):
    def run(self):
        # Definição da barra com iterações e descrição do nome
        bar = tqdm(total=NUMBER_OF_ITERATIONS, desc=self.name)


        #  loop for para definir as atividades e refresh da barra
        for i in range(NUMBER_OF_ITERATIONS):
            random.randint(1, 100) * random.randint(1, 100)
            bar.update()
            time.sleep(random.randint(1, 6)/10)
        bar.close()


threads = []

# Função do psutil para contar o número de núcleos lógicos
cpu_count = psutil.cpu_count(logical=True)

# Laço para iniciar os núcleos da máquina e iniciar as iterações
for i in range(cpu_count):
    t = MyThread()
    threads.append(t)
    t.start()

# Laço para adicionar as threads dentro da lista
for t in threads:
    t.join()
print('\nThreads terminadas')

