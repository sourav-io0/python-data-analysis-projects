from collections import deque
graph={
'A':['B','C'],
'B':['D','E'],
'C':['F'],
'D':[],
'E':[],
'F':[]
}
queue=deque()
visited=set()
traversal_order=[]
start='A'
queue.append(start)
visited.add(start)
while queue:
    current=queue.popleft()
    traversal_order.append(current)
    for neighbor in graph[current]:
        if neighbor not in visited:
            queue.append(neighbor)
            visited.add(neighbor)
print('Final traversal Order:')
print('-->'.join(traversal_order))
