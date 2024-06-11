import hashlib

def find_collision(zero_count):
    target = '0' * zero_count
    i = 0
    while True:
        data = str(i)+'bJpZ2tABnoSFk8Q7qQgKPfyvmy8jwpZKd4Qgy0cGep9KU6IvFBlxb+BEN9y4srp5YygpKIaGuQ608Bhv5NJ0CwtMZXRzTW92ZUNURgMAAAAAAAAAAAAAAAAAAAA='
        hash_value = hashlib.sha3_256(data.encode()).hexdigest()
        if hash_value[:zero_count] == target:
            print(f"找到碰撞：{data} 对应的哈希值为 {hash_value}")
            break
        i += 1

find_collision(3)