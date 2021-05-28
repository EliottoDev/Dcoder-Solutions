alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")

num = int(input())

out = ""

for x in range(num):
  out += alphabet[x]
  
print("".join(list(reversed(out))))