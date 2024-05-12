import heapq

#ordeno el conjunto para agarrar los k ultimos elementos que son los mayores y asi maximizo
def sumaSelectiva(X, k):
    X = sorted(X)
    n = len(X)
    S = X[n-k:n] #agarro los k elementos
    return sum(s for s in S)

X = [5,6,9,11,5,7,17,8,2,10,5]
k = 5
print(sumaSelectiva(X,k)) # expected result: 17 + 11 + 10 + 9 + 8 = 55
#Complejidad: O(n log n)

#Vamos a usar un minHeap
def sumaSelectivaMasEficiente(X, k): 
    n = len(X)
    minHeap = X[:k]
    heapq.heapify(minHeap) #O(k log k)
    
    for i in range(k,n): #O(n)
        minimo = heapq.heappop(minHeap)
        if X[i] > minimo:
            heapq.heappush(minHeap, X[i]) #O(log k)
        else:
            heapq.heappush(minHeap, minimo) #O(log k)
    
    return sum(minHeap)

#Complejidad: O(n log k + k log k) = O(n log k)
print(sumaSelectiva(X,k))