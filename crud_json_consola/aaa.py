import funcion
import json

idr = int(input("id: "))
name = str(input("name: "))
age = str(input("age: "))
city = str(input("city: "))

todo = {}

todo["campo"] = {
    "0" : "id",
    "1" : "name",
    "2" : "age",
    "3" : "city"
}

todo["datos"] = {
    idr : {
        "1" : name,
        "2" : age,
        "3" : city
    }
}
