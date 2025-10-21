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
################################

total_logs = 0
def logger(prefix):
    count=0
    def log(msg):
        global total_logs
        nonlocal count
        total_logs+=1
        count +=1
        print(f"{prefix} [{count} / {total_logs}]: {msg}")
    return log

error = logger("ERROR")
 
error("File not found")
error("Access denied")
# TODO: use info logger with your own messages 

#############################################

def password_protector(pwd):
    def check(input_pwd):
        return pwd==input_pwd
    return check

temp=password_protector("123")
print(temp("23"))
print(temp("123"))
print(temp("23"))
########################################3
total_saves = 0
def remember():
    last=0
    def inner(new_value):
        global total_saves
        nonlocal last
        total_saves+= 1
        last=new_value
        return(f"Stored: {last} (Total saves: {total_saves})")
    return inner


save = remember()
memo = remember()

print(save("apple"))
print(save("banana"))
print(memo("carrot"))
print(save("banana"))
###################################

labels = ["Home", "Profile", "Settings"]
actions = []
for label in labels:
    def action():
        print(f"Opening {label}")
    actions.append(action)
for act in actions:
    act()