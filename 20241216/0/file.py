# напишем ручками
"""
def ite(n):
...     for i in range(n):
...             yield i
...     return n * 2
...
 I = ite(4)
 next(I)
"""

# list for catching stopIterration
"""
>>> def call(ite, n):
...     res = yield from ite(n)
...     yield res
...
>>> list(call(ite, 5))
[0, 1, 2, 3, 4, 10]
"""

# send next
"""
>>> def ite(n):
...     res = 0
...     for i in range(n):
...             param = yield i
...             res += param
...     return res
...
>>> I = ite(4)
>>> I.send(None)
0
>>> I.send(1)
1
>>> I.send(7)
2
>>> I.send(10)
3
>>> I.send(20)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration: 38

"""

# coroutine
"""
>>> asyns def helolo(name):
  File "<stdin>", line 1
    asyns def helolo(name):
          ^^^
SyntaxError: invalid syntax
>>> async def helolo(name):
...     print("Hello", name)
...     return 42
...
>>> helolo
<function helolo at 0x7fd7d3a31630>
>>> h = helolo("ME")
>>> h
<coroutine object helolo at 0x7fd7d3b4bd80>
>>>
"""

# асинхронность
"""
>>> import asyncio
>>> asyncio.run(helolo("Me"))
Hello Me
42
>>>

>>> async def twostep(a, b):
...     print("Start", a, b)
...     await asyncio.sleep(a)
...     print("Continue", a, b)
...     await asyncio.sleep(b)
...     print("End", a, b)
"""

# образующий цикл
"""
>>> async def main():
...     t1, t2 = asyncio.create_task(twostep(3, 4)), asyncio.create_task(twostep(1, 2))
...     await t1
...     await t2
...
>>> asyncio.run(main())
Start 3 4
Start 1 2
Continue 1 2
Continue 3 4
End 1 2
End 3 4

# same but different

>>> async def main():
...     await asyncio.gather(twostep(3, 4), twostep(1, 2))
...
>>> asyncio.run(main())
Start 3 4
Start 1 2
Continue 1 2
Continue 3 4
End 1 2
End 3 4

"""

import asyncio

# squarer * doubler
async def squarer(param):
    return param ** 2

async def doubler(param):
    return param * 2

"""
async def main(x, y):
    a, b = await asyncio.gather(squarer(x), squarer(y))
    return await asyncio.gather(doubler(a), doubler(b))

print(asyncio.run(main(9, 10)))
# [162, 200]
"""

# for security

"""
async def main(x, y):
    async with asyncio.TaskGroup() as tg:
        a, b = tg.create_task(squarer(x)), tg.create_task(squarer(y))
    async with asyncio.TaskGroup() as tg:
        e, f = tg.create_task(doubler(a.result())), tg.create_task(doubler(b.result()))
    return e.result(), f.result()

print(asyncio.run(main(9, 10)))
"""
# (162, 200)

# event

"""
evsnd, evmid = asyncio.Event(), [asyncio.Event(), asyncio.Event()]

async def send(ev, name, evname):
    ev.set()
    print(f"{name}: generated {evname}")


async def recv(ev, name, evname):
    await ev.wait()
    print(f"{name}: received {evname}")

async def snd():
    await send(evsnd, "snd", "evsnd")

async def mid(n):
    await recv(evsnd, f"min{n}", "evsnd")
    await send(evmid[n], f"mid{n}", f"enmid{n}")

async  def rcv():
    await recv(evmid[0], "rcv", f"evmid{0}")
    await recv(evmid[1], "rcv", f"evmid{1}")

async def main():
    await asyncio.gather(rcv(), mid(1), mid(0), snd())

print(asyncio.run(main()))
"""

# queue-------
import queue

q1 = asyncio.Queue()
q2 = asyncio.Queue()

# async  def put(name, value, wue)

async def prod(q1):
    for i in range(5):
        await q1.put(f"value_{i}")
        await asyncio.sleep(1)
        await asyncio.sleep(1)

async def mid(q1, q2, n):
    for i in range(n):
        val = await q1.get()
        await q2.put(val)

async def cons( q2, n):
    for i in range(n):
        val = await q2.get()
        print(val)

async def main():

    await asyncio.gather(cons(q2, 5), mid(q1, q2, 5), prod(q1))

print(asyncio.run(main()))