import PySimpleGUI as sg
import clips
import cartoon_rule
import re

env = clips.Environment()

def polar_question(text: str) -> str:
    """A simple Yes/No question."""
    layout = [[sg.Text(text)], [sg.Button("Yes"), sg.Button("No")], [sg.Button("PREV")]]
    window = sg.Window("Cartoon finder", layout, size=(300, 100))
    event, _ = window.read()
    # not working
    if event == "PREV":
        print("PREV")
        env.assert_string("(del)")
    for i in env.facts():
        print(i)
    window.close()

    # If the User closes the window, we interpret it as No
    if event == sg.WIN_CLOSED:
        return "No"
    else:
        return event


def list_result(text: str):
    layout = [
        [sg.Text("Result of your choices:")],
        [sg.Listbox(values=re.split(r', ', text), enable_events=True, size=(50, 10), key="-FILE LIST-")],
        [sg.Button("RESET")]]
    window = sg.Window("Cartoon finder", layout)
    event, _ = window.read()
    window.close()
    if event == "RESET":
        env.reset()


def show(text: str):
    layout = [
        [sg.Text(text)],
        [sg.Button("Start")]]
    window = sg.Window("Cartoon finder", layout)
    event, _ = window.read()
    window.close()

def print_c(text: str):
    print(text)

def main():

    env.define_function(polar_question, name='polar-question')
    env.define_function(list_result, name='result')
    env.define_function(show, name="show")
    env.define_function(print_c, name="printc")
    env.load("cartoon_rule.clp")
    # RULES = cartoon_rule.get_rules()
    # for rule in RULES:
    #     env.build(rule)
    env.run()


if __name__ == '__main__':
    print("Clips Version ", clips.__version__);
    main()
