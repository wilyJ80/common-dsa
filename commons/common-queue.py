"""
Easiest way is by using collections' deque
"""
from collections import deque

if __name__ == "__main__":
    """
    Use append and popleft for FIFO logic
    """
    queue = deque()
    deque.append(1)
    deque.append(2)
    print(deque)
    deque.popleft()
    print(deque)
