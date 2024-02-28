'''
Pequeno e simples quebrador de senhas
que utiliza o método de força bruta escrito
em python e distribuído sob a licença GPL3.

você deve ter recebido uma cópia da liceça
juntamente com o código-fonte, caso contrário: https://www.gnu.org/licenses/gpl-3.0.en.html#license-text

Programa criado por: Luiz Gabriel Magalhães Trindade.
'''

from sys import argv
from multiprocessing import Process, Queue
from pyzipper import AESZipFile as AES
from time import time
start = time()

lista = []

zip_file = argv[1]
pasta = zip_file.replace(".zip", "")
wordlist = argv[2]

with open(wordlist, "r") as file:
    passwords = [password.strip().encode("utf-8") for password in file]
    lista = passwords

def Task(argf, queue):
    for pswd in argf:
        try:
            with AES(zip_file, "r") as ref:
                ref.extractall(pasta, pwd=pswd)
                print("-"*50)
                print(f"A senha é: {pswd.decode('utf-8')}")
                print("-"*50)
                end = time()
                tempo = float(end - start)
                print(f"Tempo total: {tempo}")
                print("Programa criado por: \"Luiz Gabriel Magalhães Trindade.\"")
                print("Licenciado sob a licença GPL3.")
                print("https://www.gnu.org/licenses/gpl-3.0.en.html#license-text\n")
                queue.put("success")
                return
        except: pass

lista.sort()
print("Wordlist carregada!")

x = int(len(lista)/4)

part1 = set(lista[:x])
part2 = set(lista[x:x*2])
part3 = set(lista[x*2:x*3])
part4 = set(lista[x*3:])

queue = Queue()

t1 = Process(target=Task, args=(part1, queue))
t2 = Process(target=Task, args=(part2, queue))
t3 = Process(target=Task, args=(part3, queue))
t4 = Process(target=Task, args=(part4, queue))

t1.start()
t2.start()
t3.start()
t4.start()

for i in range(4):
    if queue.get() == "success":
        t1.terminate()
        t2.terminate()
        t3.terminate()
        t4.terminate()
        break