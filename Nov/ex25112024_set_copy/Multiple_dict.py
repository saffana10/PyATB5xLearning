
student_info_1 ={
    "name" : "saffana",
    "age" : 20,
    "address":{
        "home address" : "MAH",
        "office address" : "MUM"
    }
}

student_info_2={
    "name" : "John",
    "age" : 25,
    "address":{
        "home address" : "KA",
        "office address" : "GOA"
    }
}

student_info = [student_info_1,student_info_2]
print(student_info)
print(student_info[0])
print(student_info[0]["name"])
print(student_info[0]["age"])
print(student_info[0]["address"])
print(student_info[0]["address"]["office address"])

# alternate way
print(student_info_2["address"]["office address"])


