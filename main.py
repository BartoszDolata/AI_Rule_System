from typing import List
import PySimpleGUI as sg
import clips
import cartoon_rule
import re

cid = 0
env = clips.Environment()
def polar_question(question: str, fact: str, *answers: List):
    """A simple Yes/No question."""
    layout = [
        [sg.Text(question)],
        [sg.Radio(x,"Answer", key = x) for x in answers],
        [sg.Button("NEXT")]]

    window = sg.Window("Cartoon finder", layout, size=(300, 100))
    event, values = window.read()
    
    if event == "NEXT":
        for i in answers:
            if values[i]:
                env.assert_string("("+fact+" "+ i +")")
                print_c()
    window.close()


def list_result(*results: List[str]):
    layout = [
        [sg.Text("Result of your choices:")],
        [sg.Listbox(results, enable_events=True, size=(50, 10), key="-FILE LIST-")],
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


def print_c():
    for i in env.facts():
        print(i)
    print("------")

def check():
    print("work")

def main():
    env.define_function(polar_question, name='polar-question')
    env.define_function(list_result, name='result')
    env.define_function(show, name="show")
    env.define_function(print_c, name="printc")
    env.define_function(check, name="check")


    env.load("cartoon_rule.clp")
    # RULES = cartoon_rule.get_rules()
    # for rule in RULES:
    #     env.build(rule)
    env.run()


if __name__ == '__main__':
    # print("Clips Version ", clips.__version__);
    main()
