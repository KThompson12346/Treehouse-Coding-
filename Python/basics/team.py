# TODO Create an empty list to maintain the player names
team_list = []

# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'

add_player = input("Would you like to add a player to the team, (yes or no)?")
while add_player.lower() == 'yes':
    player_name = input("\nEnter the name of your player: ")
    team_list.append(player_name)
    add_player = input("Would you like to add a player to the team, (yes or no)?")

# TODO print the number of players on the team
print("\nThe number of players on your team is {}.".format(len(team_list)))

# TODO Print the player number and the player name
# The player number should start at the number one
player_num = 1
for player in team_list:
    print("Player {} is {}".format(player_num, player))
    player_num += 1


# TODO Select a goalkeeper from the above roster
goal_keeper = input("Select a goal keeper using numbers 1-{}: ".format(len(team_list)))
goal_keeper = int(goal_keeper)
# TODO Print the goal keeper's name
# Remember that lists use a zero based index
print("\nYou have selected {} as your goal keeper".format(team_list[goal_keeper - 1]))
