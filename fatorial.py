#--------------------------------------------------------------------
# Fibonacci por Threading
# Al Richard - 20061, Al Timbó - 20056
#--------------------------------------------------------------------

from threading import Thread

#--------------------------------------------------------------------
# Resultados Parciais
#--------------------------------------------------------------------

resultados = []

#--------------------------------------------------------------------
# Multiplicador
#--------------------------------------------------------------------

def multiplicar(lista: list[int]) -> None:
    resultados.append(1)
    for num in lista: resultados[-1] *= num

#--------------------------------------------------------------------
# Main
#--------------------------------------------------------------------

if __name__ == '__main__':
    # Entrada
    N = int(input('Digite um inteiro positivo: '))
    T = int(input('Informe o número desejado de threads: '))

    # Setup
    threads = []
    seq = list(range(1, N+1))
    if N%T: seq += [1]*(T-N%T)

    # Start
    for i in range(T):
        intervalo = seq[i*(len(seq)//T):(i+1)*(len(seq)//T)]
        t = Thread(target=multiplicar, args=(intervalo, ))
        t.start()
        threads.append(t)
    
    # Join
    for t in threads: t.join()

    # Resultado
    fatorial = 1
    for p in resultados: fatorial *= p
    print(f'{N}! = {fatorial}')

#--------------------------------------------------------------------