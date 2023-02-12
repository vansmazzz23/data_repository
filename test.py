def main():
    array = []
    d = set()
    for i in range(150):
        array.append(i)
        print(array[i])

    for i in range(150):
        array[i] = pow(array[i], 4)
        print(array[i])

    for i in range(150):
        array[i] = pow(array[i], 4)
        print(array[i])

    for i in range(150):
        d.add(array[i])

    print(len(d))

if __name__ == '__main__':
    C11 = [14]
    C = [[0 for _ in range(len(C11) * 2)] for _ in range(len(C11 * 2))]
    print(C)