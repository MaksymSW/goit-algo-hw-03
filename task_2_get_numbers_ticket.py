import random
def get_numbers_ticket(min, max, quantity):
    small = min
    large = max
    try:
        if small >= 1 and large <= 1000 and 0 < (large - small + 1):
           lottery_numbers = set()

        while len(lottery_numbers) < quantity <= large - small + 1:            
            lottery_numbers.add(random.randint(small, large))
        return sorted(list(lottery_numbers))
    
    except Exception:
        return []
                  
                  
print("Ваші лотерейні числа: ", get_numbers_ticket(1, 49, 6))
print("Ваші лотерейні числа: ", get_numbers_ticket(1, 36, 5))
print("Ваші лотерейні числа: ", get_numbers_ticket(1, 500, 10))
print("Ваші лотерейні числа: ", get_numbers_ticket(700, 500, 10))

