import PySimpleGUI as sg
import clips
import cartoon_rule
import re


def polar_question(text: str) -> str:
    """A simple Yes/No question."""
    layout = [[sg.Text(text)], [sg.Button("Yes"), sg.Button("No")]]
    window = sg.Window("Cartoon finder", layout)
    event, _ = window.read()
    window.close()

    # If the User closes the window, we interpret it as No
    if event == sg.WIN_CLOSED:
        return "No"
    else:
        return event

def list_result(text: list()):
    layout = [
        [sg.Text("Result of your choices:")],
        [sg.Listbox(values=re.split(r', ',text), enable_events=True, size=(50, 10), key="-FILE LIST-")]]
    window = sg.Window("Cartoon finder", layout)
    event, _ = window.read()
    window.close()


def main():
    env = clips.Environment()
    env.define_function(polar_question, name='polar-question')
    env.define_function(list_result, name='result')
    RULES = cartoon_rule.get_rules()
    for rule in RULES:
        env.build(rule)
    env.run()


if __name__ == '__main__':
    print("Clips Version ", clips.__version__);
    main()
