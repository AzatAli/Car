class Car:
        def __init__(self, model, size, color, doors, mileage, made_year):
                self.model = model
                self.size = size
                self.color = color
                self.doors = doors
                self.mileage = mileage
        def characteristics(self):
                print("\nХарактеристики вашего автомобиля:\nМарка: ", self.model, "\nРазмер: ", self.size, "\nЦвет: ", self.color, "\nКол-во дверей: ", self.doors, "\nПробег: ", self. mileage, "\nГод создания:", self.made_year, "\n")

models = [" ","Nissan", "Toyota", "BMW", "Lamborgini", "Ford", "Ferrari"]
sizes = [" ", "Big", "Medium", "Small", "Family size"]
colors = [" ", "Red", "Yellow", "Blue", ]
doorss = [" ", "2", "4", "6"]
mileages = [" ", "НОВАЯ", "До 1000 км", ">1000 км"]
made_years = [" ", "<1990г", "1990 - 2000гг", ">2000г"]

car_user_choice = Car
print("Здравствуйте, позвольте нашему сервису подобрать вам машину.\nМы дадим вам выбор из характеристик, подобрав которые вы сможете получить готовую машину\n")

def chce(x, options, liste):
        print("\nВыберите ", x)
        global choice
        choice = int(input(options))

chce("модель вашей машины", "\n1. Nissan\n2. Toyota\n3. BMW\n4. Lamborgini\n5. Ford\n6. Ferrari\n", models)
car_user_choice.model = models[choice]
print("Ваш выбор: ", car_user_choice.model)

chce("размер вашей машины", "1. Big\n2. Medium\n3. Small\n4. Family size\n", sizes)
car_user_choice.size = sizes[choice]
print("Ваш выбор: ", car_user_choice.size)

chce("кол-во дверей:", "\n1. 2\n2. 4\n3. 6\n", doorss)
car_user_choice.doors = doorss[choice]
print("Ваш выбор: ", car_user_choice.doors)

chce("цвет:", "\n1. Red\n2. Yellow\n3. Blue\n", colors)
car_user_choice.color = colors[choice]
print("Ваш выбор: ", car_user_choice.color)

chce("пробег", "\n1. НОВАЯ\n2. До 1000км\n3. >1000км\n", mileages)
car_user_choice.mileage = mileages[choice]
print("Ваш выбор: ", car_user_choice.mileage)

chce("год создания", "\n1. <1990г\n2. 1990 - 2000гг\n3. >2000г\n", made_years)
car_user_choice.made_year = made_years[choice]
print("Ваш выбор: ", car_user_choice.made_year)

car_user_choice.characteristics(car_user_choice)
input()
