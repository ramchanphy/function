def greet(person,first_time=False):
    if first_time:
        return"first time for everything, right? welcome," +person
    return "hello " +person
def greet_all(people):
    for person in people:
        print(greet(person))
friends=["bob","josh","john"]
greet_all(friends)