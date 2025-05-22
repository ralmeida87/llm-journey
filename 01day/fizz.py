# fizzbuzz_20.py
for n in range(0, 200):
    word = "FizzBuzz" if n % 5 == 0 else "Fizz" if n % 2 == 0 else "Buzz" if n % 5 == 0 else n
    print(word)
