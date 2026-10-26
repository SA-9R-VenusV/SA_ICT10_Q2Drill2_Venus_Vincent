from pyscript import display, document, when, HTML

grade7  = {"Kenji Reyes", "Enzo Isidro"}
grade8  = {"Ezekiel Lim", "Ben Anben"}
grade9  = {"Lebron James", "John Pork"}
grade10 = {"Ben Stiller", "Tyler James Williams"}

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