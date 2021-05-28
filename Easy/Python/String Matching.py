times = int(input())

for x in range(times):
  
  cadena, buscar = str(input()).split(" ")
  print("Yes" if buscar in cadena else "No")