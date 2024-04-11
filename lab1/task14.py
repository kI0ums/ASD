def hanoi_towers(n, source, auxiliary, target):
    if n > 0:
        hanoi_towers(n - 1, source, target, auxiliary)
        print(f"Переміщено диск {n} з {source} на {target}")
        calculate(source, target)
        hanoi_towers(n - 1, auxiliary, source, target)


def calculate(source, target):
    global state
    state[source] -= 1
    state[target] += 1
    state['moves'] += 1

    print(state, '\n')


n = 4
state = {'A': n, 'B': 0, 'C': 0, 'moves': 0}
hanoi_towers(n, 'A', 'B', 'C')
