def min_operations(target):
    steps = 0

    while target != 0:
        while target/2 == target//2:
            target = target // 2
            steps += 1
        target -= 1
        steps += 1

    return steps

print(min_operations(18))
