def principal():
     try:
        if p < 0:
            raise ValueError("Value provided cannot be negative")
        else:
         return p
     except ValueError as e:
      print("error: ", e)

def rate():
    try:
        if r < 0:
            raise ValueError("Value provided cannot be negative")
        else:
         return r
    except ValueError as e:
         print("error: ", e)
def time():
    try:
        if t < 0:
            raise ValueError("Value provided cannot be negative")
        else:
           return t
    except ValueError as e:
        print("error: ", e)
    
def simple_interest():
    p = principal()
    r = rate()
    t = time()
    return ((p*r*t)/100)
   
# while True:
p = float(input("Principal Amount: ").strip())
r = float(input("Annual Interest Rate in %: ").strip())
t = float(input("Time Period in Years: ").strip())
SI = simple_interest()

print(f"Simple Interest: N{SI}K")