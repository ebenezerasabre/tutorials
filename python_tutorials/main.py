#!/usr/bin/env python3

class ArrayVector:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.array = [None] * self.capacity

    def show_array(self):
        print("array -> ", self.array)

    def resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
        print("new capacity", new_capacity)


    def insert_at_rank_0(self, element):
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        for i in range(self.size, 0, -1):
            self.array[i] = self.array[i - 1]
        self.array[0] = element
        self.size += 1

    def remove_at_rank_0(self):
        if self.size > 0:
            removed_element = self.array[0]
            for i in range(1, self.size):
                self.array[i - 1] = self.array[i]
            self.size -= 1
            if self.size <= self.capacity // 4:
                self.resize(self.capacity // 2)
            return removed_element

    def insert_at_end(self, element):
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.size] = element
        self.size += 1

    def remove_at_end(self):
        if self.size > 0:
            removed_element = self.array[self.size - 1]
            self.size -= 1
            if self.size <= self.capacity // 4:
                self.resize(self.capacity // 2)
            return removed_element

    def elem_at_rank(self, rank):
        if 0 <= rank < self.size:
            return self.array[rank]
        else:
            return None





















#sample usage

vector = ArrayVector()


vector.insert_at_rank_0(1)
vector.insert_at_rank_0(43)
vector.insert_at_rank_0(6)
vector.insert_at_rank_0(7)

#vector.remove_at_rank_0()
vector.show_array()

print("element at rank", vector.elem_at_rank(2))



