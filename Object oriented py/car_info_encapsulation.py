# Class to represent the introduction of a car, including its name and manufacturer

class Intro:
    def __init__(self, car_name: str, manufacturer: str):
        self.car_name = car_name
        self.manufacturer = manufacturer

    def intro(self) -> str:
        return f"I am {self.car_name}, manufactured by {self.manufacturer}"

# Class to represent details about the car, such as speed and specifications
class Details():
    def __init__(self, speed, specification):
        self.speed = speed
        self.specification = specification

    def detail(self) -> str:
        return f"I can reach a speed of {self.speed} my specifications are: {self.specification}"


print("Top 10 fastest car in the world")

# List containing car models with their introductory and detailed data
models = [
    (Intro("Bugatti Chiron Supersport 300+", "Bugatti"),
     Details("304 mph", "Quad-turbo 8.0-liter W-16 engine with 1,600 horsepower")),
    (Intro("Koenigsegg Jesko Absolut", "Koenigsegg"),
     Details("300+ mph", "Twin turbocharged V8 engine with 1280 horsepower")),
    (Intro("SSC Tuatara", "SSC North America "),
     Details("316 mph", "Twin turbo V8 engine with 1,750 horsepower")),
    (Intro("Pagani Huayra", "Pagani"),
     Details("238 mph", "AMG derived twin-turbocharged V12 engine with 730 horsepower")),
    (Intro("Rimac Nevera", "Rimac Automobili"),
     Details("258 mph", "1,914 horsepower")),
    (Intro("McLaren Speedtail", "McLaren"),
     Details("250 mph", "4.0 litre twin-turbo V8 engine with 1050 horsepower")),
    (Intro("Koenigsegg Gemera", "Koenigsegg"),
     Details("250 mph", "2.0 litre three-cylinder engine with 600 horsepower")),
    (Intro("Aston Martin Valkyrie", "Aston Martin"),
     Details("250 mph", "6.5-litre hybrid V12 engine with 1,160 horsepower")),
    (Intro("Koenigsegg Agera RS", "Koenigsegg"),
     Details("277 mph", "5.0-liter twin-turbo V8 engine with 1,341 horsepower")),
    (Intro("Hennessey Venom F5", "Hennessey Performance"),
     Details("272 mph", "6.6-litre twin-turbo V8 engine with 1,800 horsepower"))
]

try:
    stop = False
    while not stop:
        # Prompt user to select a car by number
        choose_car_num = int(input("Enter the number of the car you want to view (1-10): "))
        if 1 <= choose_car_num <= 10:
            # Retrieve and display selected car information
            car_intro, car_detail = models[choose_car_num - 1]
            print(f"\nYou selected car #{choose_car_num}\n")
            print(car_intro.intro() + "\n" + car_detail.detail())
            # Ask if the user wants to choose another car
            reload = input("Do you want to select another car among the top 10, (y/n)?: ").lower()
            if reload == "y":
                stop = False
            elif reload == "n":
                stop = True
            else:
                # Handle invalid responses
                print("Invalid selection, please restart the program !")
                stop = True
        else:
            print("Invalid selection!\n")
except Exception as e:
    print("An error has occurred")
