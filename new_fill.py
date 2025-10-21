total_score = 0
def player(name):
    score=0
    def add_points(points):
        global total_score
        nonlocal score
        score+=points
        total_score+=points
        print(f"{name}: {score} points (Total: {total_score})")
    return add_points
 
alice = player("Alice")
print(alice(3))
print(alice(2))
print(alice(1))
print(alice(4))

bob = player("Bob")
print(bob(4))
print(bob(4))
print(bob(4))
print(bob(4))
