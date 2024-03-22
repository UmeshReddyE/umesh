import math_functions
def main():
    print("1. Arithmetic_progression()")
    print("2. Geometric_progression()")
    print("3. Harmonic_progression()")
    print("4. Quadrant()")
    print("5. Unsorted()")
    print("6. Sorted()")
    print("7. Sqrt()")
    print("8. Power()")
    print("9. GCD()")
    print("10. Log()")
    print("11. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Arithmetic_progression()")
        arr = list(map(int, input("Enter the list: ").split()))
        if math_functions.Arithmetic_progression(arr):
            print("The series is in Arithmetic Progression")
        else:
            print("The series is not in Arithmetic Progression")
    elif choice == 2:
        print("Geometric_progression()")
        arr=list(map(int, input("Enter the list: ").split()))
        if math_functions.Geometric_progression(arr):
            print("The series is in Geometric Progression")
        else:
            print("The series is not in Geometric Progression")
    elif choice == 3:
        print("Harmonic_progression()")
        arr=list(map(int, input("Enter the list: ").split()))
        if math_functions.Harmonic_progression(arr):
            print("The series is in Harmonic Progression")
        else:
            print("The series is not in Harmonic Progression")
    elif choice == 4:
        print("Quadrant()")
        x = int(input("Enter the x co-ordinate: "))
        y = int(input("Enter the y co-ordinate: "))
        print("The quadrant is: ", math_functions.Quadrant(x, y))
    elif choice == 5:
        print("Unsorted()")
        l = list(map(int, input("Enter the list: ").split()))
        print("The list is: ", l)
        if math_functions.Unsorted(l):
            print("The list is unsorted")
        else:
            print("The list is sorted")
    elif choice == 6:
        print("Sorted()")
        l = list(map(int, input("Enter the list: ").split()))
        print("The list is: ", l)
        if math_functions.Sorted(l):
            print("The list is sorted")
        else:
            print("The list is unsorted")
    elif choice == 7:
        print("Sqrt()")
        n = int(input("Enter the number: "))
        print("The square root of {} is {}".format(n, math_functions.Sqrt(n)))
    elif choice == 8:
        print("Power()")
        x = int(input("Enter the number: "))
        y = int(input("Enter the power: "))
        print("{} to the power {} is {}".format(x, y, math_functions.Power(x, y)))
    elif choice == 9:
        print("GCD()")
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        print("The GCD of {} and {} is {}".format(x, y, math_functions.GCD(x, y)))
    elif choice == 10:
        print("Log()")
        x = int(input("Enter the number: "))
        print("The base-2 logarithm of {} is {}".format(x, math_functions.Log(x,2)))
    elif choice == 11:
        exit()
    else:
        print("Invalid choice")
    main()

if __name__ == "__main__":
    main()

