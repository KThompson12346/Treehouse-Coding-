attendees = ["Ken", "Alena", "Treasure"]
attendees.append("Ashley")
attendees.extend(["James", "Guil"])
optional_invitees = ["Ben J", "Dave"]
Potential_attendees = attendees + optional_invitees
print("There are", len(Potential_attendees), "potential attendees currently")
