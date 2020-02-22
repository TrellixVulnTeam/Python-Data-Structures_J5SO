class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enque(self, x):
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()

        self.s1.append(x)

        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def dequeue(self):
        if len(self.s1) == 0:
            print("Queue is empty")

        x = self.s1[-1]
        self.s1.pop()
        return x

if __name__ == "__main__":

    q = Queue()
    q.enque(1)
    q.enque(2)
    q.enque(3)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())