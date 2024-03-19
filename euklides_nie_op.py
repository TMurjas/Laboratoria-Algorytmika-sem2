
def silnia(n):
    if n==0: return 1
    else: return n*silnia(n-1)

def NWDIter(a,b):
    while a!=b:
        if a>b: a=a-b
        else: b=b-1
    return a

def nwdRek(a,b):
    if a!=b:
        if a>b: return nwdRek(a-b,b)
        else: return nwdRek(a,b-a)
    return a

def nwdIIIter(a,b):
    while b!=0:
        temp=bb=a%b
        a=temp
    return a

def funkcja(i):
  if (i<3):
    return 1 
  elif (i % 2 ==0):
    return(i-3) + funkcja(i-1)+1
  else:
    return funkcja(i-1) % 7
  
def rek(n):
   if n>=1:
      return

def nwdRek(a,b):
    if b!=0: return nwdRek(b, a%b)

def tab_rek(n,tab):
    if n==0:
       return tab
    else:
      pom=tab[0]
      
      for i in range(n):
         if pom<tab[i]:
            pom=tab[i]
        
      tab[n]=pom
      return tab_rek(n-1,tab)
    
def dobinarnej(n, b):
   if n>1:
      print(str((n%2)))
      b+=str((int(n%2)))
      print(type(b))
      print(b,"wynik")
      return dobinarnej(n/2,b)
    return (b+"1")


if __name__ == '__main__':
   #n= int(input("N: "))
   #print(silnia(n))
   #a= int(input("A: "))
   #b= int(input("B: "))
   #print(NWDIter(a,b))
   #print(nwdRek(a,b))

   print(funkcja(1))
   print(funkcja(2))
   print(funkcja(3))
   print(funkcja(4))
   print(funkcja(5))
   print(funkcja(6))
   print(funkcja(7))
   print(funkcja(8))

   #Zadanie 2. Napisz funkcję rekurencyjną, która odwraca elementy tablicy.
   tablica=[1, 2, 3, 4, 5]

   tab_rek(len(tablica),tablica)
