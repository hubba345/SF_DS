def random_predict(num):
    count = 0
    left_board = 1
    right_board = 101
    while True:
        count += 1
        center = (right_board + left_board) // 2
        if center > num:
            right_board = center
        elif center < num:
            left_board = center
        else: 
            return (center, count)
        
def count_attempt(looking_number):
    stat = []
    for num in looking_number:
        res = random_predict(num)
        stat.append(res[1])
    print(f"Минимальное значение: {min(stat)}")
    print(f"Среднее значение: {sum(stat) / len(stat)}")
    print(f"Максимальное значение: {max(stat)}")
    
import numpy as np
count_lst = []
np.random.seed(5)
random_array = np.random.randint(1, 101, size=(1000))
count_lst.extend(random_array)
count_attempt(count_lst)