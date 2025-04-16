student_info = {
    "Name" : "Saffana",
    "age" : 25
}
print(student_info["Name"])
print(student_info["age"])

student_info["address"] = "AB"
print(student_info)

student_info2 = dict(Name = "Saffana", age  =  25)
print(student_info2)

student_info_1 = {
    "Name" : "Saffana",
    "age" : 25,
    "address": {
    "home_address" : "AB",
    "office_address" : "KC"
    }
}
print(student_info_1)