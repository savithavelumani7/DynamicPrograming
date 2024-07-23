def daily_temperatures(T):
    n = len(T)
    result = [0] * n
    stack = []

    for i in range(n):
        while stack and T[i] > T[stack[-1]]:
            prev_day = stack.pop()
            result[prev_day] = i - prev_day
        stack.append(i)

    return result

def user_interaction():
    input_str = input("Enter the daily temperatures separated by spaces: ")
    T = list(map(int, input_str.strip().split()))
    
    result = daily_temperatures(T)
    print( result)

user_interaction()
