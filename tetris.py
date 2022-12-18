def ways_to_give_tasks(n: int) -> int:
    # Initialize the result to 1, because there is always at least one way to give
    # the tasks in such a way that at least one programmer is happy: by giving no tasks
    # to any programmer.
    result = 1

    # Iterate over the number of tasks that each programmer can receive, starting from 1
    for i in range(1, n + 1):
        # For each number of tasks, calculate the number of ways to give tasks to the
        # programmers such that at least one programmer is happy.
        result = (result * (n - i + 1)) % 1000000007

    return result


print(ways_to_give_tasks(1))
print(ways_to_give_tasks(2))