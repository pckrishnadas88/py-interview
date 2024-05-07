# double ended queues
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)
queue.appendleft(100)
print(queue)

queue.pop()
print(queue)