import random
categories = ["Shakespeare", "Movies", "History", "Sports", "Computer Science"]

Shakespeare = ["Shakespeare heavily relied on this theatre company to produce his plays.", "It wasn't true love that killed Romeo, it was this.", "This character is famously known as a foil to Macbeth.", "In King Lear, Gloucester loses one of his senses when this is cut off.", "This character delivered Shakespeare's famous To Be or Not to Be Speech."]

Movies = ["This actor plays Batman in 2008s The Dark Knight", "In this 1980 horror movie, a family is isolated in an eerie hotel with a sinister past.","This 1999 film features a group of misfits who band together to fight against a corrupt system in a dystopian future.","In this animated film, a young lion named Simba learns to embrace his identity and take his place in the circle of life.","This popular film franchise follows a hobbit named Frodo as he embarks on a quest to destroy a powerful ring."]

History =["This U.S. president is famous for delivering the Gettysburg Address and abolishing slavery.","In 1776, this document was signed, declaring the thirteen American colonies independence from British rule.","This conflict, known for its trench warfare and the introduction of tanks, lasted from 1914 to 1918.","This famous speech by Martin Luther King Jr. was delivered during the March on Washington in 1963.","This empire, which spanned three continents at its height, was ruled by Suleiman the Magnificent in the 16th century."]

Sports = ["This sport is known as 'the beautiful game' and is played by two teams of eleven players.","This is the name of the event where in 1980, U.S. hockey team achieved a stunning upset over the Soviet Union in the Winter Olympics.","This athlete holds the record for the most home runs in a single MLB season, hitting 73 in 2001.","This tennis tournament, held annually in London, is the oldest Grand Slam event and features a grass court.","This basketball player, known as 'His Airness,' won six NBA championships with the Chicago Bulls in the 1990s."]

Computer_Science = ["This programming language, known for its use in web development, was created by Brendan Eich in 1995.","This data structure follows the Last In, First Out (LIFO) principle.","In computer networking, this protocol is commonly used to transfer files over the internet.","This algorithm, often associated with sorting, has an average time complexity of O(n log n).","This type of machine learning involves training a model on labeled data to make predictions."]

def start_game():
    score = 0
    w = str(input("Welcome to Jeopardy! Would you like to play? Yes or no?: "))
    while w.upper() != "YES" and w.upper() != "NO":
        print("Invalid response. Please enter 'Yes' or 'No'.")     
        w = str(input("Welcome to Jeopardy! Would you like to play? Yes or no?: "))
    if w.upper() == "YES":
        for i in range(25):  
            score = one_turn(score) 
        score=bonus_round(score)
    else:
        print("Too bad, maybe next time!")
        exit()
    print(f"Game Over! Your final score is: {score}")

def bonus_round(score):
    word = 'MINUTEMEN'
    s_word = ''.join(random.sample(word, len(word)))
    if score < 3000:
        print("Sorry, you do not have enough points for the bonus round.")
    else:
        print("Congratulations! You have qualified for the bonus round!")
        print(f"Unscramble this: {s_word}")
        print("You have 5 attemps to solve this. Good luck!")
        for attempt in range(1,6):
            g = input(f"Attempt {attempt}: Your guess: ").upper()
            if g == word:
                print("Correct! You're awesome!")
                score += 1000
                return score
            else:
                print("Incorrect. Try again.")
    print("Better luck next time!")
    return score

def one_turn(score):
    while True:
        print(categories)
        select = str(input("Select a category: "))
        if select.upper() == "SHAKESPEARE":
            score = Shakespeare_questions(score)
            break
        elif select.upper() == "MOVIES":
            score = Movies_questions(score)
            break
        elif select.upper() == "HISTORY":
            score = History_questions(score)
            break
        elif select.upper() == "SPORTS":
            score = Sports_questions(score)
            break
        elif select.upper() == "COMPUTER SCIENCE":
            score = Computer_questions(score)
            break
        else:
            print("Invalid Category Name")
    return score

def daily_double(score):
    print('DAILY DOUBLE!!')
    wager = int(input(f"How many points do you want to wager? Your current score: {score}\n"))
    if wager < 0 or wager > score:
        print('Invalid wager amount, please try again.')
        wager = int(input(f"How many points do you want to wager? Your current score: {score}\n"))
    print(Computer_Science[1])
    a2 = str(input("Answer: "))
    if a2.upper() == "STACK":
            score += wager
            print("Correct! Total score =", score)
    else:
            score -= wager
            print("Wrong! Total score =",score,"Correct Answer is Stack.")
    return score

def Shakespeare_questions(score):
    valid_points = ["100", "200", "300", "400", "500"]
    pvs = str(input("Select your point value. 100, 200, 300, 400, 500: "))
    while pvs not in valid_points:
        print("Invalid input! Please select a valid point value (100, 200, 300, 400, 500).")
        pvs = str(input("Select your point value. 100, 200, 300, 400, 500: "))
    if pvs == "500":
        print(Shakespeare[0])
        a1 = str(input("Answer: "))
        if a1.upper() == "THE GLOBE":
            score += 500
            print("Correct! Total score =", score)
        else:
            score -= 500
            print("Wrong! Total score =", score, "Correct answer was The Globe.")
    elif pvs == "400":
        print(Shakespeare[3])
        a2 = str(input("Answer: "))
        if a2.upper() == "EYES" or a2.upper() == "HIS EYES":
            score += 400
            print("Correct! Total score =", score)
        else:
            score -= 400
            print("Wrong! Total score =", score, "Correct answer is Eyes.")
    elif pvs == "300":
        print(Shakespeare[4])
        a3 = str(input("Answer: "))
        if a3.upper() == "HAMLET":
            score += 300
            print("Correct! Total score =", score)
        else:
            score -= 300
            print("Wrong! Total score =", score, "Correct answer is Hamlet.")
    elif pvs == "200":
        print(Shakespeare[2])
        a4 = str(input("Answer: "))
        if a4.upper() == "MACDUFF":
            score += 200
            print("Correct! Total score =", score)
        else:
            score -= 200
            print("Wrong! Total score =", score, "Correct answer is Macduff.")
    elif pvs == "100":
        print(Shakespeare[1])
        a5 = str(input("Answer: "))
        if a5.upper() == "POISON":
            score += 100
            print("Correct! Total score =", score)
        else:
            score -= 100
            print("Wrong! Total score =", score, "Correct answer is Poison.")
    return score

def Movies_questions(score):
    valid_points = ["100", "200", "300", "400", "500"]
    pvs = str(input("Select your point value. 100, 200, 300, 400, 500: "))
    while pvs not in valid_points:
        print("Invalid input! Please select a valid point value (100, 200, 300, 400, 500).")
        pvs = str(input("Select your point value. 100, 200, 300, 400, 500: "))
    if pvs == "500":
        print(Movies[0])
        a1 = str(input("Answer: "))
        if a1.upper() == "CHRISTIAN BALE":
            score += 500
            print("Correct! Total score =", score)
        else:
            score -= 500
            print("Wrong! Total score =", score, "Correct answer was Christian Bale.")
    elif pvs == "400":
        print(Movies[2])
        a2 = str(input("Answer: "))
        if a2.upper() == "MATRIX" or a2.upper() == "THE MATRIX":
            score += 400
            print("Correct! Total score =", score)
        else:
            score -= 400
            print("Wrong! Total score =", score, "Correct answer is The Matrix.")
    elif pvs == "300":
        print(Movies[1])
        a3 = str(input("Answer: "))
        if a3.upper() == "THE SHINING" or a3.upper() == "SHINING":
            score += 300
            print("Correct! Total score =", score)
        else:
            score -= 300
            print("Wrong! Total score =", score, "Correct answer is The Shining.")
    elif pvs == "200":
        print(Movies[3])
        a4 = str(input("Answer: "))
        if a4.upper() == "THE LION KING" or a4.upper() == "LION KING":
            score += 200
            print("Correct! Total score =", score)
        else:
            score -= 200
            print("Wrong! Total score =", score, "Correct answer is The Lion King.")
    elif pvs == "100":
        print(Movies[4])
        a5 = str(input("Answer: "))
        if a5.upper() == "LORD OF THE RINGS" or a5.upper() == "THE LORD OF THE RINGS":
            score += 100
            print("Correct! Total score =", score)
        else:
            score -= 100
            print("Wrong! Total score =", score, "Correct answer is The Lord of The Rings.")
    return score

        
def History_questions(score):
    valid_points = ["100", "200", "300", "400", "500"]
    pvs = str(input("Select your point value. 100, 200, 300, 400, 500: "))
    while pvs not in valid_points:
        print("Invalid input. Please select a valid point value (100, 200, 300, 400, or 500).")
        pvs = str(input("Select your point value. 100, 200, 300, 400, 500: "))
    if pvs == "500":
        print(History[4])
        a1 = str(input("Answer: "))
        if a1.upper() == "OTTOMAN" or a1.upper() == "THE OTTOMAN EMPIRE" or a1.upper() == "OTTOMAN EMPIRE":
            score += 500
            print("Correct! Total score =", score)
        else:
            score -= 500
            print("Wrong! Total score =", score, "Correct answer was The Ottoman Empire.")
    elif pvs == "400":
        print(History[3])
        a2 = str(input("Answer: "))
        if a2.upper() == "I HAVE A DREAM" or a2.upper() == "THE I HAVE A DREAM SPEECH" or a2.upper() == "THE DREAM SPEECH":
            score += 400
            print("Correct! Total score =", score)
        else:
            score -= 400
            print("Wrong! Total score =", score, "Correct Answer is The I Have a Dream Speech.")
    elif pvs == "300":
        print(History[1])
        a3 = str(input("Answer: "))
        if a3.upper() == "DECLARATION OF INDEPENDENCE" or a3.upper() == "THE DECLARATION OF INDEPENDENCE":
            score += 300
            print("Correct! Total score =", score)
        else:
            score -= 300
            print("Wrong! Total score =", score, "Correct answer is The Declaration of Independence.")
    elif pvs == "200":
        print(History[2])
        a4 = str(input("Answer: "))
        if a4.upper() == "WORLD WAR ONE" or a4.upper() == "WORLD WAR 1":
            score += 200
            print("Correct! Total score =", score)
        else:
            score -= 200
            print("Wrong! Total score =", score, "Correct answer is World War 1.")
    elif pvs == "100":
        print(History[0])
        a5 = str(input("Answer: "))
        if a5.upper() == "ABRAHAM LINCOLN" or a5.upper() == "PRESIDENT LINCOLN" or a5.upper() == "ABE LINCOLN":
            score += 100
            print("Correct! Total score =", score)
        else:
            score -= 100
            print("Wrong! Total score =", score, "Correct answer is Abraham Lincoln.")
    return score


def Sports_questions(score):
    valid_points = ["100", "200", "300", "400", "500"]
    pvs = str(input("Select your point value. 100, 200, 300, 400, 500: "))
    while pvs not in valid_points:
        print("Invalid input. Please select a valid point value (100, 200, 300, 400, or 500).")
        pvs = str(input("Select your point value. 100, 200, 300, 400, 500: "))
    if pvs == "500":
        print(Sports[2])
        a1 = str(input("Answer: "))
        if a1.upper() == "BARRY BONDS":
            score += 500
            print("Correct! Total score =", score)
        else:
            score -= 500
            print("Wrong! Total score =", score, "Correct answer was Barry Bonds.")
    elif pvs == "400":
        print(Sports[0])
        a2 = str(input("Answer: "))
        if a2.upper() == "SOCCER" or a2.upper() == "FUTBOL":
            score += 400
            print("Correct! Total score =", score)
        else:
            score -= 400
            print("Wrong! Total score =", score, "Correct Answer is Soccer/Futbol.")
    elif pvs == "300":
        print(Sports[1])
        a3 = str(input("Answer: "))
        if a3.upper() == "MIRACLE ON ICE" or a3.upper() == "THE MIRACLE ON ICE":
            score += 300
            print("Correct! Total score =", score)
        else:
            score -= 300
            print("Wrong! Total score =", score, "Correct answer is The Miracle On Ice.")
    elif pvs == "200":
        print(Sports[4])
        a4 = str(input("Answer: "))
        if a4.upper() == "MICHAEL JORDAN" or a4.upper() == "MICHEAL JORDAN":
            score += 200
            print("Correct! Total score =", score)
        else:
            score -= 200
            print("Wrong! Total score =", score, "Correct answer is Michael Jordan.")
    elif pvs == "100":
        print(Sports[3])
        a5 = str(input("Answer: "))
        if a5.upper() == "WIMBLEDON" or a5.upper() == "WIMBLEDON TOURNAMENT" or a5.upper() == "WIMBLEDON CHAMPIONSHIPS":
            score += 100
            print("Correct! Total score =", score)
        else:
            score -= 100
            print("Wrong! Total score =", score, "Correct answer is Wimbledon.")
    return score


        
def Computer_questions(score):
    valid_points = ["100", "200", "300", "400", "500"]
    pvs = str(input("Select your point value. 100, 200, 300, 400, 500: "))
    while pvs not in valid_points:
        print("Invalid input. Please select a valid point value (100, 200, 300, 400, or 500).")
        pvs = str(input("Select your point value. 100, 200, 300, 400, 500: "))
    if pvs == "500":
        print(Computer_Science[2])
        a1 = str(input("Answer: "))
        if a1.upper() == "FTP" or a1.upper() == "FILE TRANSFER PROTOCOL":
            score += 500
            print("Correct! Total score =", score)
        else:
            score -= 500
            print("Wrong! Total score =", score, "Correct answer was File Transfer Protocol.")
    elif pvs == "400":
        print(Computer_Science[4])
        a2 = str(input("Answer: "))
        if a2.upper() == "SUPERVISED LEARNING":
            score += 400
            print("Correct! Total score =", score)
        else:
            score -= 400
            print("Wrong! Total score =", score, "Correct Answer is Supervised Learning.")
    elif pvs == "300":
        print(Computer_Science[3])
        a3 = str(input("Answer: "))
        if a3.upper() == "MERGE SORT" or a3.upper() == "QUICK SORT":
            score += 300
            print("Correct! Total score =", score)
        else:
            score -= 300
            print("Wrong! Total score =", score, "Correct answer is Merge Sort.")
    elif pvs == "200":
        daily_double(score)
    elif pvs == "100":
        print(Computer_Science[0])
        a5 = str(input("Answer: "))
        if a5.upper() == "JAVA SCRIPT" or a5.upper() == "JAVA":
            score += 100
            print("Correct! Total score =", score)
        else:
            score -= 100
            print("Wrong! Total score =", score, "Correct answer is Java Script.")
    return score


start_game()
            
  



