# 78. Write a program to swap two recipe ingredients values using unpacking.
recipe1 = ["Oill", "onions", "tomatoes", "Salt", "papper"]
recipe2 = [ "onions", "tomatoes", "Salt",]
print("Before")
print("recipe ingredients:",recipe1)
print("recipe ingredients:",recipe2)

recipe1, recipe2 = recipe2, recipe1

print("After")
print("recipe ingredients:",recipe1)
print("recipe ingredients:",recipe2)
