import turtle, pandas

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')

states = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
    prompt="What's another state's name?").title()

    if answer_state == 'Exit':
        missing_states = [state for state in states if state not in guessed_states]
        data = pandas.DataFrame(missing_states)
        data.to_csv('states_to_learn.csv')
        break

    if answer_state in states:
        guessed_states.append(answer_state)

        state_data = data[data.state == answer_state] #Pulls all data of the answered state
        x = state_data['x'].item() #Extracting only the pure value with item() to avoid passing labels 
        y = state_data['y'].item()

        mp = turtle.Turtle() #Creating answers on screen
        mp.hideturtle()
        mp.penup()
        mp.setposition(x, y)
        mp.write(arg=f"{answer_state}", align='center', font=("Courier", 8, "bold"))
