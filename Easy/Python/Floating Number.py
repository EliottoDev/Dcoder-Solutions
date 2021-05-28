from decimal import Decimal

times = int(input())

for x in range(times):
  number = str(input())
  dex = Decimal(number).quantize(Decimal("1.00"))
  print (dex)