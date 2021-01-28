
from functools import lru_cache
solution = []
#short = []

@lru_cache(maxsize=10000)
def best_sum(target, nums):
   # global short
    if target == 0:
        return []
    if target < 0:
        return None
    for element in nums:
        reminder = target-element
        reminder_combination = best_sum(reminder, nums)
        if reminder_combination != None:
            solution.append(element)
            print(f"solution {solution} & element is {element}")
            return solution
            # if len(short)==0:
            #     print("short")
    
              
    


#print(best_sum(7, tuple([5, 3, 4, 7])))
print(best_sum(300, tuple([7,14])))
