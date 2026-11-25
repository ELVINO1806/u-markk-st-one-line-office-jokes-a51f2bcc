import os

ENTRY_SETUP = "The office thermostat has two settings: Arctic and meeting room."
ENTRY_PUNCH = "We vote daily. Arctic always wins."

OUTPUT_PATH = "/output/entry.txt"


def build_entry():
    return ENTRY_SETUP + " " + ENTRY_PUNCH


def main():
    text = build_entry()
    directory = os.path.dirname(OUTPUT_PATH)
    os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
