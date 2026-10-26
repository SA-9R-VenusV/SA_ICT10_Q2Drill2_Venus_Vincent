from pyscript import display, document, when, HTML

grade7  = {"Ana Reyes", "Ben Cruz", "Carla Santos"}
grade8  = {"Diego Lim", "Elena Garcia", "Ben Cruz"}
grade9  = {"Felix Tan", "Gina Flores", "Hugo Ramos"}
grade10 = {"Iris Mendoza", "Jon Bautista", "Kara Aquino"}

master = grade7 | grade8 | grade9 | grade10


def render():
    display(
        HTML(f"""
        <h2>Total members: {len(master)}</h2>
        <ul><li>{'</li><li>'.join(sorted(master))}</li></ul>
        """),
        target="output",
        append=False,
    )


@when("click", "#add-btn")
def add_member(event):
    global master
    first = document.querySelector("#first-name")
    last = document.querySelector("#last-name")

    full_name = f"{first.value.strip()} {last.value.strip()}".strip()
    new_member = {full_name} - {""}

    master = master | new_member

    first.value = ""
    last.value = ""
    render()


render()