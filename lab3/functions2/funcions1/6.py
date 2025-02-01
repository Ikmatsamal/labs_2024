string = "We are ready"
def Convert(string):
  li = list(string.split(" "))
  print(*li[::-1])
Convert(string)