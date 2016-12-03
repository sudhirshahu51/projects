# To implement Heap data structure using list


class Heap:
    def __init__(self):
        self.items = [None]
    
    def __len__(self):
        return self.size()
    
    def size(self):
        return len(self.items)-1    
    
    def insert(self, k):
        self.items.append(k)
        self.restore_up(self.size())
    
    def restore_up(self, i):
        if i <= 1:
            return
        k = self.items[i]
        par = i//2
        while self.items[par] <= k:
            self.items[i] = self.items[par]
            i = par
            if i <= 1:
                break
            par = i//2
        self.items[i] = k
    
    def delete(self):
        if self.size() < 2:
            return self.items.pop(-1)
        tmp = self.items[1]
        self.items[1] = self.items.pop(-1)
        self.restore_down()
        return tmp
    
    def restore_down(self):
        i = 1
        k = self.items[i]
        left_child, right_child = i * 2, i * 2 + 1
        while right_child <=  self.size():
            if k > self.items[left_child] and k > self.items[right_child]:
                return
            elif self.items[left_child] > self.items[right_child]:
                self.items[i] = self.items[left_child]
                i = left_child
            else:
                self.items[i] = self.items[right_child]
                i = right_child
            left_child, right_child = i * 2, i * 2 + 1
        if left_child == self.size() and k < self.items[left_child]:
            self.items[i] = self.items[left_child]
            i = left_child
        self.items[i] = k


def build_max_heap(arr):
    h = Heap()
    h.items = h.items + arr[:]
    for i in range(1, h.size()+1):
        h.restore_up(i)
    return h
    

if __name__ == '__main__':
    a = [25,35,18,9, 46, 70, 48, 23, 78, 12, 95]
    heap = build_max_heap(a)
    for i in range(12):
        print(heap.delete())