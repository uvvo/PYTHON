import turtle
from random import randint

# For screen
width = 700
height = 500
S = turtle.Screen()
S.setup(width,height)
S.bgcolor('black')


#T = turtle.Turtle
T = turtle.Pen()
T.speed(0)

# Start line
T.up()
T.setposition(-140,50)
T.color('white')
T.write('Start line',align='center')
T.right(90)
T.forward(10)
T.down()
T.forward(155)

# Finish line
T.up()
T.setposition(140,50)
T.write('Finish line',align='center')
T.color('white')
T.forward(10)
T.down()
T.forward(155)


T.up()
T.setposition(-175,20)
T.color('white')
T.down()
T.left(90)
T.forward(340)

T.up()
T.setposition(-175,-5)
T.down()
T.forward(340)

T.up()
T.setposition(-175,-35)
T.down()
T.forward(340)

T.up()
T.setposition(-175,-65)
T.down()
T.forward(340)

T.up()
T.setposition(-175,-95)
T.down()
T.forward(340)

T.up()
T.setposition(-175,-120)
T.down()
T.forward(340)

T.hideturtle()

# 1st turtle, red
T1 = turtle.Turtle()
T1.up()
T1.setposition(-160,10)
T1.shape('turtle')
T1.color('magenta')

# 2nd turtle, green
T2 = turtle.Turtle()
T2.up()
T2.setposition(-160,-20)
T2.shape('turtle')
T2.color('green')

# 3rd turtle, pink
T3 = turtle.Turtle()
T3.up()
T3.setposition(-160,-50)
T3.shape('turtle')
T3.color('pink')

# 4th turtle, yellow
T4 = turtle.Turtle()
T4.up()
T4.setposition(-160,-80)
T4.shape('turtle')
T4.color('yellow')

# 5th turtle, white
T5 = turtle.Turtle()
T5.up()
T5.setposition(-160,-110)
T5.shape('turtle')
T5.color('white')

# race
line = 140
while T1.xcor() < line or T2.xcor() < line or T3.xcor() < line or \
      T4.xcor() < line or \
      T5.xcor() < line:
    T1.forward(randint(1,5))
    T2.forward(randint(1,5))
    T3.forward(randint(1,5))
    T4.forward(randint(1,5))
    T5.forward(randint(1,5))


# Ranking Board
finals_list = [T1.xcor(),T2.xcor(),T3.xcor(),T4.xcor(),T5.xcor()]
finals_dict = {T1.xcor():'magenta', T2.xcor():'green', \
               T3.xcor():'pink',T4.xcor():'yellow', \
               T5.xcor():'white'} 

finals_list = sorted(finals_list,reverse=True) 

T.up() 
T.color('white')
T.setposition(-60,200)
T.write('Leader Board                                 Score:',align='left', font=(None,12))

# 1st
T.setposition(-60,180)
rank = finals_list[0]
T.write(f'1st place: {finals_dict[rank]} turtle                                                          5 points',align='left')

# 2nd
T.setposition(-60,160)
rank = finals_list[1]
T.write(f'2nd place: {finals_dict[rank]} turtle                                                          4 points',align='left')

# 3rd
T.setposition(-60,140)
rank = finals_list[2]
T.write(f'3rd place: {finals_dict[rank]} turtle                                                          3 points',align='left')

# 4th
T.setposition(-60,120)
rank = finals_list[3]
T.write(f'4th place: {finals_dict[rank]} turtle                                                          2 points',align='left')

# 5th
T.setposition(-60,100)
rank = finals_list[4]
T.write(f'5th place: {finals_dict[rank]} turtle                                                          1 point',align='left')
