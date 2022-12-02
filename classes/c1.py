class Cat:
    name = ""
    age = 0
    fur_color = ""
    breed = ""
    def eat(self):
        print("Cat is eating!")

    def sleep(self):
        print("Cat is sleeping!")

#creating objects
tom = Cat()
snow = Cat()
tom.name = "Tom"
tom.age = 3
tom.fur_color = "white"
tom.breed = "City cat"
snow.name = "Snowbell"
snow.age = 5
snow.fur_color = "gray"
snow.breed = "persian"

# calling method
tom.eat()
tom.sleep()
snow.sleep()
print (tom.name, tom.age, tom.fur_color, tom.breed)
print (snow.name, snow.age, snow.fur_color, snow.breed)
