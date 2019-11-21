import multiprocessing

def calc_square(number):
    print(f'Square: {number * number}')

def calc_quad(number):
    print(f'Quad: {number * number * number * number}')

if __name__ == "__main__":
    print(f'Starting execution of {__name__}...')
    number = 7
    p1 = multiprocessing.process(target=calc_square, args=(number,))
    p2 = multiprocessing.process(target=calc_quad, args=(number,))
    # Will execute both in parallel
    p1.start()
    p2.start()
    # Joins threads back to the parent process, which is this
    # program
    p1.join()
    p2.join()

# This program reduces the time of execution by running tasks in parallel
    print(result)