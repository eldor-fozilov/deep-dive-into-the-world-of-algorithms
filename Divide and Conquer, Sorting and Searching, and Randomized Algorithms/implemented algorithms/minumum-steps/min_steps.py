# Problem definition:
# Think of a process moving from the integer 𝑥 to 𝑦 via multiple steps based on the following rules.
# A. The length of each step is nonnegative, and the length of the first and last step is one.
# B. The length of the next step is either one less than, equal to, or one greater than the length of the previous step.
# For example, moving from the integer 10 to 15 takes four steps (i.e., 1+2+1+1).
# Write an algorithm that finds the smallest number of steps when moving from the integer 𝑥 to 𝑦.

def min_steps(x, y):
    distance = y - x
    if distance == 0:
        return 0

    min_steps = 0
    step_size = 0
    steps_sum = 0
    l = []
    for i in range(distance):
        min_steps += 1

        check = False
        for j in [1, 0]:
            temp_step_size = step_size + j
            sum = temp_step_size * (temp_step_size + 1) / 2
            if sum <= (distance - steps_sum):
                check = True
                step_size += j
                break

        if check == False:
            step_size -= 1

        l.append(step_size)
        steps_sum += step_size
        if steps_sum == distance:
            print(l)
            return min_steps
