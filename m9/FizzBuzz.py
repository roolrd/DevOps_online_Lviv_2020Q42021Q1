def fizzbuzz(n):
    if n%3==0 and n%5==0:
        return "FizzBuzz"
    elif n%5==0:
        return "Buzz"
    elif n%3==0:
        return "Fizz"
    else:
        return n
    
for i in range(1,100):
    print(fizzbuzz(i))
