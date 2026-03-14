def solve_rabbits():
    try:
        with open('rosalind_fib.txt', 'r') as f:
            line = f.read().strip()
            n, k = map(int, line.split())

        parent, child = 1, 1

        for i in range(n - 2):
            new_generation = child + (parent * k)
            
            parent = child
            child = new_generation

        print(child)

    except FileNotFoundError:
        print("Error: 'rosalind_fib.txt' not found.")

solve_rabbits()