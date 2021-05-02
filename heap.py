from collections import deque
from typing import List


class MinHeap:
    def __init__(self):
        self.storage = []
        self.size = 0

    def push(self, element):
        self.storage.append(element)
        self.size += 1
        self.sift_up()

    def sift_up(self):
        index = len(self) - 1
        parent = (index - 1) // 2
        while self.storage[parent] > self.storage[index]:
            tmp = self.storage[parent]
            self.storage[parent] = self.storage[index]
            self.storage[index] = tmp
            index = parent
            parent = (index - 1) // 2
            if index == 0:
                break

    def sift_down(self):
        index = 0
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            if right >= len(self):
                right = left
            if left >= len(self):
                break
            if min(self.storage[left], self.storage[right]) == self.storage[left]:
                min_index = left
            else:
                min_index = right
            tmp = self.storage[index]
            self.storage[index] = self.storage[min_index]
            self.storage[min_index] = tmp
            index = min_index

    def pop(self):
        answer = self.peek()
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.sift_down()
        return answer

    def peek(self):
        return self.storage[0]

    def __len__(self):
        return self.size

    def __str__(self):
        q = deque()
        q.append((0, 1))
        answer = [[] for _ in range(len(self)+1)]
        while len(q) > 0:
            v, depth = q.popleft()
            answer[depth].append(self.storage[v])
            for to in (2 * v + 1, 2 * v + 2):
                if to < len(self):
                    q.append((to, depth + 1))
        return str(answer)


def main():
    heap = MinHeap()
    for i in range(10, 1, -1):
        heap.push(i)
    while len(heap) > 0:
        print(heap)
        heap.pop()


if __name__ == '__main__':
    main()
