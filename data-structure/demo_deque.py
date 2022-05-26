from collections import deque

queue = deque(['aaa', 'bbb', 'ccc'])
queue.append('ddd')
queue.append('eee')
print(queue)

queue.popleft()
print(queue)