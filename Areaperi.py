def Area_of_Rectangle(length, breadth):
    return length * breadth

def perimeter_of_rectangle(length,breadth):
    return 2*(length+breadth)

def Area_of_Circle(radius):
    return 22/7*(radius**2)

def Area_of_square(sides):
    return sides ** 2

def Area_of_triangle(base,height):
    return 1/2*(base*height)

if __name__ == "__main__":
    while True:
        print("select an option")
        print("1. Area of Rectangle")
        print("2. Perimeter of Rectangle")
        print("3. Area of Circle")
        print("4. Area of Square")
        print("5. Area of Triangle")
        print("6. Exit")

        choice = int(input("enter the option: "))

        if choice == 1:
            length = int(input("enter the value og length: "))
            breadth = int(input("enter the value of breadth: "))
            areaofrectangle = Area_of_Rectangle(length, breadth)
            print(areaofrectangle)

        elif choice == 2:
            length = int(input("enter the value og length: "))
            breadth = int(input("enter the value of breadth: "))
            perimeterofrectangle = perimeter_of_rectangle(length, breadth)
            print(perimeterofrectangle)

        elif choice == 3:
            radius = int(input("enter the value of radius: "))
            areaofcircle = Area_of_Circle(radius)
            print(areaofcircle)

        elif choice == 4:
            sides = int(input("enter the value of side: "))
            areaofsquare = Area_of_square(sides)
            print(areaofsquare)

        elif choice == 5:
            base = int(input("enter the value of base: "))
            height = int(input("enter the value og height: "))
            areaoftriangle = Area_of_triangle(base, height)
            print(areaoftriangle)

        elif choice == 6:
            break

        else:
            print("invalid option")
