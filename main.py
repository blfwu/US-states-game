from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

map = Turtle()
map.shape(image)

states_guessed = []
missing_states = []
score = 0

data = pandas.read_csv("50_states.csv")



while score != 50:
    answer_state = screen.textinput(title="Guess the State", prompt=f"{score}/50 States Guessed")
    answer_state = answer_state.title() # guess works if lowercase, all uppercase, etc.

    if answer_state == "Exit":
        print("Check 'states_to_learn.csv' to learn the states you missed!")
        break

    elif answer_state in states_guessed: # check if state has already been guessed
        print(f"Already guessed {answer_state}!")
        
    elif answer_state in data["state"].values: # check if guess is among 50 states in csv
        x_coord = data[data["state"] == answer_state]["x"].values[0]
        y_coord = data[data["state"] == answer_state]["y"].values[0] # find x and y coords of the state

        states_guessed.append(answer_state)
        score += 1

        state = Turtle() # create new turtle object for each state correct
        state.hideturtle()
        state.penup()
        state.goto(x_coord, y_coord)
        state.write(f"{answer_state}", True, "center") # write correct guess onto map at respective x and y coords

        print(f"{answer_state} is a state!")

    else:
        print(f"{answer_state} is not a state!")
        


for index, row in data.iterrows(): # iterates through states_guessed and adds missing states to a missing_states to be written to states_to_learn.csv
    # print(row['state'])
    if not row['state'] in states_guessed:
        missing_states.append(row["state"])
        
        missing_states_df = pandas.DataFrame(
            {"state": missing_states}
        )
        missing_states_df.to_csv("states_to_learn.csv")
