# A priority queue is a container data structure that manages a set of records with 
# totally-ordered keys (for example, a numeric weight value) to provide quick 
# access to the record with the smallest or largest key in the set.
#instead of retrieving the next element by insertion time, it retrieves the 
# highest-priority element

import heapq
from Queue import PriorityQueue

n_list=[]

heapq.heappush(n_list,2)
heapq.heappush(n_list,1)
heapq.heappush(n_list,3)

while n_list:
    print(heapq.heappop(n_list))


q = PriorityQueue()

q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))

while not q.empty():
    next_item = q.get()
    print(next_item)
