letter_file = open("Mail Merge Project Start\Input\Letters\starting_letter.txt")

names_file = open("Mail Merge Project Start\\Input\\Names\\invited_names.txt", "r")

new_letter_file = letter_file.read()
new_file_name = "invite_for_[name].txt"

for i in names_file:
    f = i.strip()
    b = new_letter_file
    a = b.replace("[name]", f)
    c = new_file_name.replace("[name]",f)
    e = c.strip()
    d = open(e, "w")
    d.write(a)
    d.close()
    


letter_file.close()
names_file.close()