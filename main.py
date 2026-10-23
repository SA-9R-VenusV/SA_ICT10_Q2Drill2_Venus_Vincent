from pyscript import display, document, when, HTML
import html

grade7  = {"Kenji Reyes", "Enzo Isidro"}
grade8  = {"Phoenix Lim", "Jonathan Macabebe"}
grade9  = {"Jonathan Macabebe", "Mack Ahti"}
grade10 = {"Dom Inik", "Al-Abang"}

master = grade7 | grade8 | grade9 | grade10


def fmt(s):
    return ", ".join(sorted(s)) or "none"


def render(status):
    both_7_8   = grade7 & grade8
    only_7     = grade7 - grade8
    one_of_7_8 = grade7 ^ grade8

    upper = set(grade9)
    upper |= grade10
    shared = set(grade7)
    shared &= grade8
    left_over = set(grade7)
    left_over -= grade8
    either = set(grade7)
    either ^= grade8

    is_subset        = grade7 <= master
    is_proper_subset = grade7 < master
    is_superset      = master >= grade7
    is_proper_super  = master > grade7
    same_as          = grade7 == grade8
    differs          = grade7 != grade8
    no_overlap       = (grade9 & grade10) == set()
    ana_in           = "Ana Reyes" in master
    zed_missing      = "Zed Nobody" not in master

    display(
        HTML(f"""
        <p class="status">{status}</p>

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

    full_name = html.escape(f"{first.value.strip()} {last.value.strip()}".strip())

    new_member = {full_name} - {""}

    key = (len(new_member), len(new_member & master))
    messages = {
        (0, 0): "Please enter a first and last name.",
        (1, 0): f"{full_name} was added to the club.",
        (1, 1): f"{full_name} is already a member (sets ignore duplicates).",
    }

    master |= new_member

    first.value = ""
    last.value = ""
    render(messages[key])


render("Club loaded from the four grade-level sets.")