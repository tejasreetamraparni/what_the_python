nums = {1:'a', 2:'b'}

def get(k):
    return nums.get(k) is not None

print(get(4))