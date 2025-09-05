marks = {
    "Shariar" : 100,
    "Oni" : 99,
    "Sadiq" : 90 ,
    0 : "Hellal"
}
print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Oni": 44 , "Shakib":67})
print(marks)

print(marks.get("Dulal"))

print(marks.get("Sadiq2")) #gives you a none value
# print(marks["Sadiq2"]) Gives you a error