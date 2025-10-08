def Fibonacci(n):
    """
    Return the first n Fibonacci numbers as a list.
    Fibonacci sequence used: 0, 1, 1, 2, 3, ...
    If n <= 0 : returns []
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

def Display(n=10):
    """Print first n Fibonacci numbers (default n=10)."""
    seq = Fibonacci(n)
    print(f"Fibonacci series (first {n}): {', '.join(map(str, seq))}")

if __name__ == '__main__':
    import sys
    # Allow optional command-line argument for n
    n = 10
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
        except ValueError:
            print("Invalid argument. Using default n = 10.")
    Display(n)
