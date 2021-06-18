import math
from sympy import symbols, Eq, solve
import turtle
import sys
print('''
     NOTE: Please enter the angle in degrees only
      '''
      )
start = 0
while (start == 0):
    fx = 0
    fy = 0
    Forces = []
    Quads = []
    Angles = []
    no_forces = 0
    print('''
    1. Find Resultant forces
    2. Find Unknown forces[Maximum 2]
    ''')
    ch = int(input("ENTER YOUR CHOICE(1-2): "))
    if ch == 1:
        print('''
              Please enter the angle in degrees
              '''
              )
        no_forces = int(input("Enter the total number of forces: "))
        for i in range(0, no_forces):
            force = float(input("Enter force {}: ".format(i + 1)))
            print('''
                  Choose force unit
              Enter 1 for Newton
              Enter 2 for kilonewton
              Enetr 3 for Dyne
              '''
                  )
            unit = int(input("Choose the unit: "))
            if unit == 1:
                force = force
            elif unit == 2:
                force = force * 1000
            elif unit == 3:
                force = round(force * (10**-5),2)
            else:
                print("Pls Enter valid option..... ")
                for i, x in enumerate(list(range(10000000))):
                    pass
                print("Program exiting...")
                for i, x in enumerate(list(range(10000000))):
                    pass
                sys.exit(0)
               
                
            quad = int(input("Enter quadrant(1-4): "))
            if quad > 4:
                print("\nPls Enter valid quarant..... ")
                for i, x in enumerate(list(range(10000000))):
                    pass
                print("Program exiting...")
                for i, x in enumerate(list(range(10000000))):
                    pass
                sys.exit(0)
                    
            ang_rad = float(input("Enter angle made with x axis: "))
            ang_deg = ang_rad * math.pi / 180
            Forces.append(force)
            Quads.append(quad)
            Angles.append(ang_rad)
            if quad == 1:
                fx = fx + (force * math.cos(ang_deg))
                fy = fy + (force * math.sin(ang_deg))

            elif quad == 2:
                fx = fx - (force * math.cos(ang_deg))
                fy = fy + (force * math.sin(ang_deg))

            elif quad == 3:
                fx = fx - (force * math.cos(ang_deg))
                fy = fy - (force * math.sin(ang_deg))

            else:
                fx = fx + (force * math.cos(ang_deg))
                fy = fy - (force * math.sin(ang_deg))
            
                
        print("\n\t\tEntered Forces in Newton are:")
        print("\n%-15s %-15s %s" %('Force', 'Quadrant', 'Angle'))
        
        for x in range(0, no_forces):
            f = Forces[x]
            q = Quads[x]
            a = Angles[x]
            print ("%-15s %-15s %s" %(f,q,a))
        
        print('''
            TO CONFIRM PRESS 1 
            TO RESET PRESS 2
            ''')
        confirm = int(input())
        if confirm == 1:
            print('''
                      \t\t\t     ____________________
                          \t\t\t|____CALCULATING_...|

            ''')
            for i, x in enumerate(list(range(10000000))):
                pass
            print("\tThe sum of all forces along x axis is: ", round(fx, 2)," N")
            print("\tThe sum of all forces along y axis is: ", round(fy, 2)," N")
            resultant = math.sqrt((fx ** 2) + (fy ** 2))
            if resultant == 0:
                print("\n\tThe forces are in equilibrium: ")
            else:
                resultant_ang_rad = math.atan(fy / fx)
                resultant_ang_deg = abs(resultant_ang_rad * (180 / math.pi))
                print("\n\tThe magnitude of the resultant force is: ", round(resultant, 2)," N")
                print("\n\tThe angle of the resultant force with respect to x axis is:", round(resultant_ang_deg, 2),"degrees")

                if fx > 0 and fy > 0:
                    print("\n\tThe resultant is acting in FIRST QUADRANT")

                    sc = turtle.Screen()
                    sc.bgcolor("Lightblue")
                    x_axis = turtle.Turtle()
                    y_axis = turtle.Turtle()
                    res = turtle.Turtle()
                    cir = turtle.Turtle()
                    res.color("Red")
                    cir.color("Blue")
                    x_axis.forward(200)
                    y_axis.left(90)
                    y_axis.forward(200)
                    res.left(45)
                    res.forward(150)
                    res.write(round(resultant, 2))
                    cir.left(45)
                    cir.forward(30)
                    cir.circle(-20, 180)
                    cir.write(round(resultant_ang_deg, 2))
                    sc.exitonclick()

                elif fx < 0 and fy > 0:
                    print("\n\tThe resultant is acting in SECOND QUADRANT")

                    sc = turtle.Screen()
                    sc.bgcolor("Lightblue")
                    x_axis = turtle.Turtle()
                    y_axis = turtle.Turtle()
                    res = turtle.Turtle()
                    cir = turtle.Turtle()
                    res.color("Red")
                    cir.color("Blue")
                    x_axis.left(180)
                    x_axis.forward(200)
                    y_axis.left(90)
                    y_axis.forward(200)
                    res.left(135)
                    res.forward(150)
                    res.write(round(resultant, 2))
                    cir.left(135)
                    cir.forward(30)
                    cir.circle(20, 180)
                    cir.write(round(resultant_ang_deg, 2))
                    sc.exitonclick()

                elif fx < 0 and fy < 0:
                    print("\n\tThe resultant is acting in THIRD QUADRANT")
                    sc = turtle.Screen()
                    sc.bgcolor("Lightblue")
                    x_axis = turtle.Turtle()
                    y_axis = turtle.Turtle()
                    res = turtle.Turtle()
                    cir = turtle.Turtle()
                    res.color("Red")
                    cir.color("Blue")
                    x_axis.left(180)
                    x_axis.forward(200)
                    y_axis.right(90)
                    y_axis.forward(200)
                    res.right(135)
                    res.forward(150)
                    res.write(round(resultant, 2))
                    cir.right(135)
                    cir.forward(30)
                    cir.circle(-20, 180)
                    cir.write(round(resultant_ang_deg, 2))
                    sc.exitonclick()

                elif fx > 0 and fy < 0:
                    print("\n\tThe resultant is acting in FORTH QUADRANT")

                    sc = turtle.Screen()
                    sc.bgcolor("Lightblue")
                    x_axis = turtle.Turtle()
                    y_axis = turtle.Turtle()
                    res = turtle.Turtle()
                    cir = turtle.Turtle()
                    res.color("Red")
                    cir.color("Blue")
                    x_axis.forward(200)
                    y_axis.right(90)
                    y_axis.forward(200)
                    res.right(45)
                    res.forward(150)
                    res.write(round(resultant, 2))
                    cir.right(45)
                    cir.forward(30)
                    cir.circle(20, 180)
                    cir.write(round(resultant_ang_deg, 2))
                    sc.exitonclick()
                else:
                    pass

        
        if confirm == 2:
            continue
    elif ch == 2:
        unknownforce_quad = []
        unknownforce_ang = []
        fx = 0
        fy = 0
        F1c = 1 #To detect correct sense of unknown forces
        F2c = 1 #To detect correct sense of unknown forces
        F1s = 1 #To detect correct sense of unknown forces
        F2s = 1 #To detect correct sense of unknown forces
        known_forces = int(input("Enter the number of known forces: "))
        unknown_forces = int(input("Enter the number of unknown forces(Maximun 2): "))
        
        print("\n\t\tENTER THE KNOWN FORCES")

        for i in range(0, known_forces):
            force = float(input("Enter force {}: ".format(i + 1)))
            print('''
                 Choose force unit
              Enter 1 for Newton
              Enter 2 for kilonewton
              Enetr 3 for Dyne
              '''
                  )
            unit = int(input("Choose the unit: "))
            if unit == 1:
                force = force
            elif unit == 2:
                force = force * 1000
            elif unit == 3:
                force = round(force * (10**-5),2)
            else:
                print("Pls Enter valid option..... ")
                for i, x in enumerate(list(range(10000000))):
                    pass
                print("Program exiting...")
                for i, x in enumerate(list(range(10000000))):
                    pass
                sys.exit(0)
            quad = int(input("Enter quadrant(1-4): "))
            if quad > 4:
                print("\nPls Enter valid quarant..... ")
                for i, x in enumerate(list(range(10000000))):
                    pass
                print("Program exiting...")
                for i, x in enumerate(list(range(10000000))):
                    pass
                sys.exit(0)
            
            ang_rad = float(input("Enter angle made with x axis: "))
            ang_deg = ang_rad * math.pi / 180
            
            if quad == 1:
                
                fx = fx + (force * math.cos(ang_deg))
                fy = fy + (force * math.sin(ang_deg))
                


            elif quad == 2:
                fx = fx - (force * math.cos(ang_deg))
                fy = fy + (force * math.sin(ang_deg))
                

          
            elif quad == 3:
                fx = fx - (force * math.cos(ang_deg))
                fy = fy - (force * math.sin(ang_deg))
                
            
            else:
                fx = fx + (force * math.cos(ang_deg))
                fy = fy - (force * math.sin(ang_deg))
        
       
        for a in range(0, unknown_forces):
            print("\t\tENTER THE DETAILS OF UNKNOWN FORCE",a+1,": ")
            quad = int(input("Enter quadrant(1-4): "))
            ang_rad = float(input("Enter angle made with x axis: "))
            ang_deg = ang_rad * math.pi / 180
            unknownforce_ang.append(ang_deg)
            unknownforce_quad.append(quad)


        if unknown_forces == 1:
            if unknownforce_quad[0] == 1 or unknownforce_quad[0] == 4:
                F1c = F1c
            else:
                F1c == -F1c
            F1c = F1c * (fx / math.cos(ang_deg))
            print("The unknown Force F1 is",F1c," N")
        elif unknown_forces == 2:
            if unknownforce_quad[0] == 1:
                F1c = F1c
                F1s = F1s
            elif unknownforce_quad[0] == 2:
                F1c = -F1c
                F1s = F1s
            elif unknownforce_quad[0] == 3:
                F1c = -F1c
                F1s = -F1s
            elif unknownforce_quad[0] == 4:
                F1c = F1c
                F1s = -F1s
            else:
                print("Enter Valid quadrant")
                break
            if unknownforce_quad[1] == 1:
                F2c = F2c
                F2s = F2s
            if unknownforce_quad[1] == 2:
                F2c = -F2c
                F2s = F2s
            if unknownforce_quad[1] == 3:
                F2c = -F2c
                F2s = -F2s
            if unknownforce_quad[1] == 4:
                F2c = F2c
                F2s = -F2s
            x, y = symbols('x y')
            eq1 = Eq(F1c*x*math.cos(unknownforce_ang[0]) + F2c*y*math.cos(unknownforce_ang[1]) + fx,0)
            eq2 = Eq(F1s*x*math.sin(unknownforce_ang[0]) + F2s*y*math.sin(unknownforce_ang[1]) + fy,0)
            result = solve([eq1,eq2],(x,y))
            
            print("\n\n\t\tThe unknown forces are:")
            sol_dict = solve((eq1,eq2), (x, y))
            print("F1 = ", round(sol_dict[x],2)," N")
            print("F2 = ", round(sol_dict[y],2)," N")
            
    print("\nTo Continue press 1")
    print("To exit press 0 : ")
    cont=int(input())
    if cont == 1:
        continue
    else:
        sys.exit(0)
    
