def LongestValid(expr): 
    stack = [] 
    Validlengh = 0
    for char in expr: 
        if char == '(': 
            stack.append(char) 
        else: 
            if not stack: 
                continue
            stack.pop()
            Validlengh += 2

    return Validlengh

if __name__ == "__main__": 
    expr = "(((((((((((()(()))"
    print(LongestValid(expr))