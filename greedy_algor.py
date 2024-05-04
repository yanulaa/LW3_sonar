def greedy_algorithm(m, n, u, t):
    # Створення списку пар (індекс, вага, тривалість)
    pairs = [(i, u[i], t[i]) for i in range(n)]

    # Сортування робіт за неспаданням часу
    pairs.sort(key=lambda x: (-x[1], x[2]))
    formatted_output = "[" + ",".join([f"(i:{x[0]}, u:{x[1]}, t:{x[2]})" for x in pairs]) + "]"
    print("Відсортовані роботи:", formatted_output)

    # Формування пар робіт
    pairs_grouped = []
    for i in range(0, n - 1, 2):
        pair = (pairs[i][0], pairs[i + 1][0])
        pair_u_avg = (pairs[i][1] + pairs[i + 1][1]) / 2
        pairs_grouped.append((pair, pair_u_avg))
    print("Сформовані пари робіт:",
          [f"(pair:{pair[0]}, u_avg:{pair[1]})" for pair in pairs_grouped])

    # Формування розкладу
    schedule = [[] for _ in range(m)]  # Розклад для кожної машини
    machine_times = [0] * m  # Час виконання для кожної машини
    machine_index = 0

    for pair in pairs_grouped:
        # Додаємо пару до машини по черзі
        schedule[machine_index].append(pair)
        machine_index = (machine_index + 1) % m

        print("Розклад:")
        for i, machine in enumerate(schedule):
            print(f"Машина {i + 1}:", machine)

    # Розрахунок значення цільової функції
    target_function = 0
    total_jobs = 0

    for i, machine in enumerate(schedule):
        time_accumulated = 0
        for pair in machine:
            for job in pair[0]:
                time_accumulated += t[job]
                target_function += u[job] * time_accumulated
                total_jobs += 1

    target_function /= total_jobs
    print("Значення цільової функції:", target_function)
    return schedule, target_function

# Вхідні дані
m = 2
n = 12
u = [4, 2, 1, 3, 2, 5, 1, 4, 3, 2, 5, 2]
t = [3, 2, 5, 1, 3, 2, 8, 5, 2, 1, 3, 1]

# Виклик функції
schedule, target_function = greedy_algorithm(m, n, u, t)