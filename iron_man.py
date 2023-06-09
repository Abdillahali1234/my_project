import turtle
face_one = [
  [(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10),(-40, -20), (0, -20)],

  [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260),(40, 120), (0, 120)]
]

face_two = [
  [(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210),(-80, -230), (-64, -210), (0, -210)],
  
  [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40),(100, -46), (50, -40), (40, -30), (0, -30)]
]

face_three = [
  [(-60, -220), (-80, -240), (-110, -220), (-120, -250), (-90, -280), (-60, -260), (-30, -260), (-20, -250),(0, -250)],
  
  [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250), (110, -220), (80, -240), (60, -220),(0,-220)]
]
for i in range(10):
    turtle.title("project to draw iron man by abdullah ali")
    turtle.hideturtle()
    turtle.setup(850.800)
    turtle.speed(2)
    turtle.bgcolor("#000000")
    start_point_for_face_one=(-40, 120)
    start_point_for_face_tow=(-40, -30)
    start_point_for_face_three=(-60, -220)
    def draw_face(face_one,start_point):

        turtle.penup()
        turtle.goto(start_point)
        turtle.pendown()
        turtle.color("#C0C0C0")   
        turtle.begin_fill()
        for i in range(len(face_one[0])):
            turtle.goto(face_one[0][i])

        for i in range(len(face_one[1])):
            turtle.goto(face_one[1][i])      

        turtle.end_fill()   


    draw_face(face_one,start_point_for_face_one)
    draw_face(face_two,start_point_for_face_tow)
    draw_face(face_three,start_point_for_face_three)
    turtle.clear()
