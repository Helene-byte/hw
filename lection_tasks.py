# import os
# filename = 'letstry.txt'
# with open(filename, 'w') as f:
#     index = 0
#     while os.path.getsize(filename)<3000000:
#         f.write(f'{str(index)}\n')
#         index +=1
import timeit


def case_1():
    summa=0
    with open('letstry.txt')as f:
        data = f.readlines()
        for line in data:
            if line.strip().isnumeric():
                summa+=int(line)
        print("Sum:", summa)

def case_2():
    summa=0
    with open('letstry.txt')as f:
        for line in f:
            if line.strip().isnumeric():
                summa+=int(line)
        print("Sum:", summa)

def case_3():

    with open('letstry.txt')as f:

        numbers=(int(line) for line in f if line.strip().isnumeric())
        print("Sum:", sum(numbers))

print(timeit.timeit(case_1, number=1))
print(timeit.timeit(case_2, number=1))
print(timeit.timeit(case_3, number=1))