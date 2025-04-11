from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

map = Turtle()
map.shape(image)

states_guessed = []
num_guessed = 0

data = pandas.read_csv("50_states.csv")

# states = data["state"]
# print(states)


while num_guessed != 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    if answer_state in data["state"].values:
        x_coord = data[data["state"] == answer_state]["x"].values[0]
        y_coord = data[data["state"] == answer_state]["y"].values[0]
        # print(x_coord)
        # print(y_coord)

        states_guessed.append(answer_state)
        num_guessed += 1

        state = Turtle()
        state.hideturtle()
        state.pu()
        state.goto(x_coord, y_coord)
        
        state.write(f"{answer_state}", True, "center")
        
    
    print(answer_state)
    print(states_guessed)
    print(num_guessed)









map.mainloop()
screen.exitonclick()