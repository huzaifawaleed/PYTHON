# Set Methods.

# Union() & Update()
# In union() it returns the values of two sets in a new third set like set3 = set1.union(set2).
# In update() it returns the values of both sets in first set there is no need to create third variable like car1.update(car2)


# car1 = {"Honda", "Toyota", "Suzuki","Hyundai"}
# car2 = {"Honda", "Changan", "Peugeot","Hyundai"}
# car3 = car1.union(car2)
# print(car3)

# car1 = {"Honda", "Toyota", "Suzuki","Hyundai"}
# car2 = {"Honda", "Changan", "Peugeot","Hyundai"}
# car1.update(car2)
# print(car1)


# intersection() & intersection_update().
# In intersection() it returns the common values of both sets in a new set like set3 = set1.intersection(set2).
# In intersection_update() it returns the values of both sets in first set there is no need to create third variable like car1.intersection_update(car2).


# car1 = {"Honda", "Toyota", "Suzuki","Hyundai"}
# car2 = {"Honda", "Changan", "Peugeot","Hyundai"}
# car3 = car1.intersection(car2)
# print(car3)

# car1 = {"Honda", "Toyota", "Suzuki","Hyundai"}
# car2 = {"Honda", "Changan", "Peugeot","Hyundai"}
# car1.intersection_update(car2)
# print(car1)


# symmetric_difference() & symmetric_difference_update().
# In symmetric_difference() it returns the values which are not common in both sets in a new set like set3 = set1.symmetric_difference(set2).
# In intersection_update() it returns the values which are not common in both sets in first set there is no need to create third variable like car1.symmetric_difference_update(car2).


# car1 = {"Honda", "Toyota", "Suzuki","Hyundai"}
# car2 = {"Honda", "Changan", "Peugeot","Hyundai"}
# car3 = car1.symmetric_difference(car2)
# print(car3)

# car1 = {"Honda", "Toyota", "Suzuki","Hyundai"}
# car2 = {"Honda", "Changan", "Peugeot","Hyundai"}
# car1.symmetric_difference_update(car2)
# print(car1)


# Difference() & Difference_Update().
# In difference() it returns the values which are only present in orignal set means set1 in a new variable like set3 = set1.difference(set2).
#In difference_update() it returns the values which are only present in orignal set means set1 there is no need of new variable it updates existing variable like set1.difference_update(set2).

# car1 = {"Honda", "Toyota", "Suzuki","Cultus"}
# car2 = {"Honda", "Changan", "Peugeot","Hyundai"}
# car3 = car1.difference(car2)
# print(car3)

car1 = {"Honda", "Toyota", "Suzuki","Cultus"}
car2 = {"Honda", "Changan", "Peugeot","Hyundai"}
car1.difference_update(car2)
print(car1)