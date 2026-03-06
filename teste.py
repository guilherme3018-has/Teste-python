soma
def soma(*args):
    try:
      total = 0
      for n in args:
         total += flat(n)
      return total  
    except Exception as e:
         print(str(e))    