import random
import time

#todo O(n + m)
def main(list):
    max_element = 0
    max_list = []

    for i in list:  #todo O(n)
        if i == 0:
            break
        if i > max_element:
            max_element = i
        if i == max_element:
            max_list.append(i)  #todo O(1)

    count = 0
    for i in max_list:  #todo O(m)
        if i == max_element:
            count += 1

    print(f'len_1 = {len(list)}, len_2 = {len(max_list)}, max_list = {max_list}')
    print(f'max_element = {max_element}')
    return count


if __name__ == '__main__':
    # data = list(map(int, open('input.txt').readlines()))
    # data = random.sample(range(0, 10_000_000), 2_000_000)
    # print(f'len = {len(data)}, {data}')
    n = 1_000_000 # Количество элементов в массиве
    m = 1000 # Диапазон чисел
    data = [random.randint(0, m) for i in range(n)]
    start_time = time.time()
    target = main(data)
    print("--- %s seconds ---" % (time.time() - start_time))
    open('output.txt', 'w').write(str(target))
    print(f'ans = {target}')