import sys
import requests

print(sys.version)
print (sys.executable)


def greeting(person):
    greeting = "hi {}".format(person)
    return (greeting)



# print(greeting("avraham"))
# print(greeting("bob"))
r = requests.get("https://www.youtube.com/")
print(r.status_code)

