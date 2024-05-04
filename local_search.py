import random
import copy

def calculate_target_function(schedule, u, t):
    target_function = 0
    total_jobs = 0

    for machine in schedule:
        time_accumulated = 0
        for pair in machine:
            for job in pair:
                time_accumulated += t[job]
                target_function += u[job] * time_accumulated
                total_jobs += 1

    return target_function / total_jobs

def greedy_algorithm(m, n, u, t):
    pairs = [(i, u[i], t[i]) for i in range(n)]
    pairs.sort(key=lambda x: (-x[1], x[2]))

    pairs_grouped = []
    for i in range(0, n - 1, 2):
        pairs_grouped.append((pairs[i][0], pairs[i + 1][0]))

    schedule = [[] for _ in range(m)]
    machine_index = 0

    for pair in pairs_grouped:
        schedule[machine_index].append(pair)
        machine_index = (machine_index + 1) % m

    return schedule

def print_schedule(schedule, msg="Розклад"):
    print(msg)
    for i, machine in enumerate(schedule):
        print(f"Машина {i + 1}: {[f'(робота {pair[0]}, робота {pair[1]})' for pair in machine]}")

def local_search(m, n, u, t, N):
    best_schedule = greedy_algorithm(m, n, u, t)
    best_target_function = calculate_target_function(best_schedule, u, t)
    print_schedule(best_schedule, "Початковий розклад:")
    print(f"Початкове значення цільової функції: {best_target_function}")

    for iteration in range(N):
        new_schedule = copy.deepcopy(best_schedule)

        machine1, machine2 = random.sample(range(m), 2)
        if new_schedule[machine1] and new_schedule[machine2]:
            pair1_index = random.randint(0, len(new_schedule[machine1]) - 1)
            pair2_index = random.randint(0, len(new_schedule[machine2]) - 1)

            new_schedule[machine1][pair1_index], new_schedule[machine2][pair2_index] = new_schedule[machine2][pair2_index], new_schedule[machine1][pair1_index]

        new_target_function = calculate_target_function(new_schedule, u, t)

        print(f"\nІтерація {iteration + 1}:")
        print_schedule(new_schedule, "Новий розклад після обміну:")
        print(f"Нове значення цільової функції: {new_target_function}")

        if new_target_function < best_target_function:
            best_target_function = new_target_function
            best_schedule = new_schedule
            print("Новий найкращий розклад знайдено!")

    print("\nНайкращий розклад після локального пошуку:")
    print_schedule(best_schedule)
    print("Найкраще значення цільової функції:", best_target_function)
    return best_schedule, best_target_function

# Вхідні дані
m = 2
n = 12
u = [4, 2, 1, 3, 2, 5, 1, 4, 3, 2, 5, 2]
t = [3, 2, 5, 1, 3, 2, 8, 5, 2, 1, 3, 1]

# Виклик алгоритму локального пошуку
N = 5  # Наприклад, показати 5 ітерацій
best_schedule, best_target_function = local_search(m, n, u, t, N)
