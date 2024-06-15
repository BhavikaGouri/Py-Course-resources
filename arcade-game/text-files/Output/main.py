with open("./Input/Names/invited_names.txt") as name:
    names = name.readlines()

with open("./Input/Letters/starting_letter.txt") as letters:
    content = letters.read()
    for name in names:
        stripped_name = name.strip()
        new_name = content.replace("[name]", stripped_name)
        with open(f"{stripped_name}.txt", "w") as file:
            file.write(new_name)
            