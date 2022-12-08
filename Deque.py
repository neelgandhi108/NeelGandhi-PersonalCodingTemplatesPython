#Deque

# Stack
s = deque()
s.append(1);  # 1
s.append(2);  # 1,2
s.append(3);  # 1,2,3
s.pop();      # 1,2
s.pop();      # 1

# Queue
q = deque()
q.append(1);  # 1
q.append(2);  # 1,2
q.append(3);  # 1,2,3
q.popleft();  # 2,3
q.popleft();  # 3

# LinkedList
ll = deque() 
ll.append(1);     # 1
ll.append(2);     # 1,2
ll.appendleft(0); # 0,1,2
ll.pop();         # 0,1
ll.popleft();     # 1

