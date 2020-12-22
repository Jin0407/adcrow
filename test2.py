class MaxStack():

    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, data):
        self.stack.append(data)
        self.size += 1

    def pop(self):
        if self.size==0:
            print("There's no data.")
        else:
            return self.stack.pop()
            self.size -= 1
    
    def top(self):
        if self.size==0:
            print("There's no data.")
            return 0
        else:
            return self.stack[-1]
    
    def peekMax(self):
        return max(self.stack)

def main():
    s = MaxStack()
    s.push('8')
    s.push('5')
    s.push('0')
    s.push('4')
    s.push('0')
    s.push('7')
    print(s.stack)
    s.pop()
    print(s)
    print(s.top())
    print(s.peekMax())


if __name__ == "__main__":
    main()