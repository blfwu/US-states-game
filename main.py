from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

map = Turtle()
map.shape(image)

states_guessed = []
score = 0

data = pandas.read_csv("50_states.csv")

# states = data["state"]
# print(states)


while score != 50:
    answer_state = screen.textinput(title="Guess the State", prompt=f"{score}/50 States Guessed")
    answer_state = answer_state.title() # guess works if lowercase, all uppercase, etc.

    if answer_state == "Exit":
        break

    if answer_state in data["state"].values: # check if guess is among 50 states in csv
        x_coord = data[data["state"] == answer_state]["x"].values[0]
        y_coord = data[data["state"] == answer_state]["y"].values[0]
        # print(x_coord)
        # print(y_coord)

        states_guessed.append(answer_state)
        score += 1

        state = Turtle()
        state.hideturtle()
        state.pu()
        state.goto(x_coord, y_coord) # write correct guess onto map at respective x and y coords
        
        state.write(f"{answer_state}", True, "center")
        
    
    print(answer_state)
    print(states_guessed)
    print(score)