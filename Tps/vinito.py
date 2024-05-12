#consigna: https://vjudge.net/problem/SPOJ-GERGOVIA

def wineTrade(demanda,n):
    work = 0
    acc = 0
    
    for i in range(n):
        acc += demanda[i]
        work += abs(acc)  
        
    return work



while True:
    caso = int(input()) 
     
    if caso == 0:
        break 
    
    demanda = list(map(int, input().split()))

    print(wineTrade(demanda, len(demanda)))

