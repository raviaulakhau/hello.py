from cmath import sqrt
def quradratic_solver(cofficient_of_x2, cofficient_of_x, quradratic_constant):
    
    root_1 = (-cofficient_of_x + sqrt(cofficient_of_x * cofficient_of_x - 4 * cofficient_of_x2 * quradratic_constant)) / (2*cofficient_of_x2)
    root_2 = (-cofficient_of_x + sqrt((cofficient_of_x * cofficient_of_x - 4 * cofficient_of_x2 * quradratic_constant))) / (2*cofficient_of_x2)
    print(root_1, root_2)


x = int(input(("enter x^2 cofficient: ")))
y = int(input(("enter x cofficient: ")))
c = int(input(("enter quradratic_constant: ")))
quradratic_solver(x, y, c)