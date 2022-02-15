import turtle

# klasa reprezentujaca system Lindenmayera wraz z metodami reguł produkcji ciągów znaków przetwarzanych do stworzenia
# fraktali z wykorzystaniem grafiki żółwia
class Lsystem:
    def __init__(self, axiom_string: str = 'F++F++F', regule_string: str = 'F-F++F-F', iterations: int = 4,
                 angle: float = 60.0, length: int = 5):
        self.axiom = axiom_string
        self.regule = regule_string
        self.iter = iterations
        self.angle = angle
        self.length = length
        # self.create_l_system(number_of_iterations=iterations,axiom=axiom_string,rule_string=regule_string)

    def apply_rules(self, original_string: str, rule_string: str):
        return ''.join([rule_string if chr == 'F' else chr for chr in original_string])

    def create_l_system(self, number_of_iterations: int, axiom: str, rule_string: str):
        for gen in range(number_of_iterations):
            axiom = self.apply_rules(axiom, rule_string)
        return axiom

# Rysowanie l -systemu z wykorzystaniem grafiki żółwia
def draw_l_system(my_turtle: turtle.Turtle, instructions: str, angle: float, distance: int):
    #deklaracja i inicjalizacja koloru w postaci listy formatu RGB, w turtle przedział formatu koloru wynosi od 0 do 1.0
    color: list = [0.3, 0.35, 0.36]
    #deklaracja stosu
    stack: list = []

    for task in instructions:
        my_turtle.color(color)
        if task == 'F':
            my_turtle.forward(distance)
        elif task == 'B':
            my_turtle.backward(distance)
        elif task == '+':
            my_turtle.right(angle)
        elif task == '-':
            my_turtle.left(angle)
        #
        elif task == 'f':
            my_turtle.penup()
            my_turtle.forward(distance)
            my_turtle.pendown()
        elif task == '[':
            pos = [my_turtle.xcor(), my_turtle.ycor()]
            stack.append((angle, pos))
        elif task == ']':
            angle, pos = stack.pop()
            my_turtle.setheading(angle)
            my_turtle.penup()
            my_turtle.goto(pos[0], pos[1])
            my_turtle.pendown()
        #rysuj kropke
        elif task == '*':
            my_turtle.dot()
        # manipulacja kolorem
        elif task == '@':
            if color[1] >= 1.0:
                color[1] -= 0.5
            elif color[1] < 0:
                color[1] += 0.02
            else:
                color[1] += 0.01

#inicjalizacja okna aplikacji wraz z markerem rysujacym - wartości zwracane w postaci tuple
def initialize_screen():
    window = turtle.Screen()
    window.bgcolor('black')
    my_turtle = turtle.Turtle()

    my_turtle.speed(1000)

    my_turtle.up()
    my_turtle.back(200)
    my_turtle.down()
    return my_turtle, window

#main
if __name__ == "__main__":

    print('1 - Koch \n')
    print('2 - Sierpinski \n')
    print('3 - Petadendrith \n')
    print('4 - Tree \n')

    user: int = int(input('Select a method from range 1 to 4 : \n'))

    my_turtle, window = initialize_screen()

    if user == 1:
        koch = Lsystem()
        string = koch.create_l_system(koch.iter, koch.axiom, koch.regule)
        draw_l_system(my_turtle, string, koch.angle, koch.length)
    elif user == 2:
        sierpinski = Lsystem(axiom_string='F+F+F', regule_string='F+F-F-F+F', angle=120.0, iterations=4, length=6)
        string = sierpinski.create_l_system(sierpinski.iter, sierpinski.axiom, sierpinski.regule)
        draw_l_system(my_turtle, string, sierpinski.angle, sierpinski.length)
    elif user == 3:
        tree_structure = Lsystem(axiom_string='F', regule_string='F+F-F--F+F+F', angle=72, iterations=5,
                                 length=2)
        tree_string = tree_structure.create_l_system(tree_structure.iter, tree_structure.axiom, tree_structure.regule)
        draw_l_system(my_turtle, tree_string, tree_structure.angle, tree_structure.length)

    elif user == 4:
        #rysowanie kolorowego drzewa wraz z kropkami jak korzeń gałęzi 
        tree_structure = Lsystem(axiom_string='----F', regule_string='FF+[*+@F-@F-@F]-[*-@F+@F+@F]', angle=22.5,
                                 iterations=3,
                                 length=10)
        tree_string = tree_structure.create_l_system(tree_structure.iter, tree_structure.axiom, tree_structure.regule)
        draw_l_system(my_turtle, tree_string, tree_structure.angle, tree_structure.length)
    else:
        print('Black Screen')
        window.bye()

    window.exitonclick()
