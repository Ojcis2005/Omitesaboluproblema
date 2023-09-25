

class Auglis
  def __init__(self, number, age, name);
    self.age = age
    self.number = number
    self.name = name
user = Auglis(2,3,"Ābols")
print(Auglis.number)             // Dārza augļu klase

class Dārzenis
  def __init__(self, number, age, name)
    self.number = number
    self.age = age
    self.name = name

user = Auglis(3,3,"Burkāns")
print(Auglis.number)        // Dārza dārzeņu klase
// ka veikt datu ievadi no malas

 Fruit = []
Vegitable = []


while True:
    print("Enter 'v' for vegetable, 'f' for fruit, or 'q' to quit:")
    choice = input()

    if choice == 'q':
        break
    elif choice == 'v':
        vegetable = input("Enter a vegetable: ")
        vegetables.append(vegetable)
    elif choice == 'f':
        fruit = input("Enter a fruit: ")
        fruits.append(fruit)
    else:
        print("Invalid choice. Please enter 'v', 'f', or 'q'.")

print("Entered vegetables:", vegetables)
print("Entered fruits:", fruits)