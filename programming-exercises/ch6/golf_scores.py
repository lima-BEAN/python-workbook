# The Springfork Amateur Golf Club has a tournament every weekend.
# The club president has asked you to write two programs:
#
#   1. A program that will read each player's name and golf score
#      as keyboard input, and then save these records in a file
#      named golf.txt. (Each record will have a field for the player's name
#                       and a field for the player's score.)
#   2. A program that reads the records from the golf.txt file and then
#      displays them.


def main():
    names =   []
    scores =    []
    
    add = Add()
    while add == True:
        player_name = PlayerName()
        player_score = PlayerScore()
        names.append(player_name)
        scores.append(player_score)
        add = Add()
        
    Write(names, scores)
    Read()

def Add():
    add = input('Do you have a player\'s name and score to add? (y/n): ')
    if add.title() == 'Y':
        return True
    else:
        return False

def PlayerName():
    name = input('Player\'s name: ')
    return name

def PlayerScore():
    score = input('Player\'s score: ')
    return score

def Write(names, scores):
    count = 0
    file = open('golf.txt', 'w')
    for name in names:
        count += 1
        file.write(str(count) + ': ' + name + '\t\tScore: ' + scores[count-1])
    file.close()

def Read():
    golf_scores = open('golf.txt', 'r')
    for record in golf_scores:
        print(record)
    golf_scores.close()
    
main()
