from Main1 import Fibonacci

def TestFibonacci():
    assert Fibonacci(1) == [0]
    assert Fibonacci(2) == [0, 1]
    assert Fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
    assert Fibonacci(0) == []
    print("Fibonacci function works correctly")

if __name__ == '__main__':
    TestFibonacci()
