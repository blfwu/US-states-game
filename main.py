import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_guessed = []
num_guessed = 0

data = pandas.read_csv("50_states.csv")
states = data["state"]
# print(states)


while num_guessed != 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    if answer_state in data["state"].values:
        states_guessed.append(answer_state)
        num_guessed += 1

        # state = Turtle()
        # state.goto(50,50)
        
        # state.write(f"{answer_state}", True, "center")
        
    
    print(answer_state)
    print(states_guessed)
    print(num_guessed)









turtle.mainloop()
screen.exitonclick()