class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return None

def user_interaction():
    minStack = MinStack()
    
    while True:
        print("\nEnter a command:")
        print("1. push <value>")
        print("2. pop")
        print("3. top")
        print("4. getMin")
        print("5. exit")
        
        command = input().strip().split()
        
        if command[0] == "push":
            if len(command) == 2 and command[1].isdigit() or (command[1][0] == '-' and command[1][1:].isdigit()):
                minStack.push(int(command[1]))
                print(f"Pushed {command[1]}")
            else:
                print("Invalid value. Please enter a valid integer.")
        elif command[0] == "pop":
            minStack.pop()
            print("Popped the top element.")
        elif command[0] == "top":
            top_value = minStack.top()
            if top_value is not None:
                print(f"Top element is {top_value}")
            else:
                print("Stack is empty.")
        elif command[0] == "getMin":
            min_value = minStack.getMin()
            if min_value is not None:
                print(f"Minimum element is {min_value}")
            else:
                print("Stack is empty.")
        elif command[0] == "exit":
            print("Exiting.")
            break
        else:
            print("Invalid command. Please try again.")

user_interaction()
