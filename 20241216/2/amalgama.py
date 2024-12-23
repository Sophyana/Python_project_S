import asyncio
import random

async def merge(A, B, start, middle, finish, event_in1, event_in2, event_out):
    await asyncio.gather(event_in1.wait(), event_in2.wait())
    i, j, k = start, middle, start

    while i < middle and j < finish:
        if A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1

    while i < middle:
        B[k] = A[i]
        i += 1
        k += 1

    while j < finish:
        B[k] = A[j]
        j += 1
        k += 1

    event_out.set()

async def mtasks(A):
    a = A.copy()
    N = len(A)
    B = [0] * N
    tasks = []
    current_array = a
    next_array = B

    events = [[asyncio.Event() for _ in range((N + (1 << level) - 1) // (1 << level))]
              for level in range((N - 1).bit_length() + 1)]

    step = 1
    level = 0
    while step < N:
        for start in range(0, N, 2 * step):
            middle = min(start + step, N)
            finish = min(start + 2 * step, N)

            event_in1 = events[level][start // step]
            event_in2 = events[level][middle // step if middle < N else (start // step)]
            event_out = events[level + 1][start // (2 * step)]

            task = merge(current_array, next_array, start, middle, finish, event_in1, event_in2, event_out)
            tasks.append(task)

        current_array, next_array = next_array, current_array
        step *= 2
        level += 1

    if current_array is not a:
        a[:] = current_array[:]

    for i in range(len(events[0])):
        events[0][i].set()

    return tasks, current_array

import sys
exec(sys.stdin.read())
