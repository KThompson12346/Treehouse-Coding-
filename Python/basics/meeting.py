attendees = ["Ken", "Alena", "Treasure"]
attendees.append("Ashley")
attendees.extend(["James", "Guil"])
optional_invitees = ["Ben J", "Dave"]
Potential_attendees = attendees + optional_invitees
print("There are", len(Potential_attendees), "potential attendees currently")

to_line = ", ".join(attendees)
Cc_line = ", ".join(optional_invitees)
print("To: " + to_line)
print("Cc: " + Cc_line)

musical_groups = [
    ["Ad Rock", "MCA", "Mike D."],
    ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"],
    ["Salt", "Peppa", "Spinderella"],
    ["Rivers Cuomo", "Patrick Wilson", "Brian Bell", "Scott Shriner"],
    ["Chuck D.", "Flavor Flav", "Professor Griff", "Khari Winn", "DJ Lord"],
    ["Axl Rose", "Slash", "Duff McKagan", "Steven Adler"],
    ["Run", "DMC", "Jam Master Jay"],
]
# Your code here
for group in musical_groups:
    one_group = ', '.join(group)
    print("Members are: {}".format(one_group))
