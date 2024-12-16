import sys


def write_output(N, sorted_chunks):
    result = bytearray([N]) + b"".join(sorted_chunks)
    sys.stdout.buffer.write(result)


data = sys.stdin.buffer.read()

N = data[0]
tail = data[1:]
L = len(tail)
chunks = sorted( [tail[round(i * L / N): round((i + 1) * L / N)] for i in range(N)] )
sorted_chunks = sorted(chunks)
write_output(N, sorted_chunks)


import sys
exec(sys.stdin.read())