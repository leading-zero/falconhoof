import sys
import random

def main():

    # I've created Boolean variables to define the different scenes contained
    # throughout the game. When each variable is set to 'True' the player
    # is located within that particular scene. Most scenes have been given a short
    # name which give an idea about the game's current state  and characters or
    # challenges that appear in the scene.

    intro = True
    start_game = False
    fork = False
    witch = False
    troll = False
    boulder = False
    labyrinth = False
    chasm = False

    # The misunderstood variable advises the player that their inpu does not
    # match the options given by the narration.

    misunderstood = "\nFalconhoof does not understand this instruction."
    misunderstood += "\n"
    misunderstood += "\nRespond according to the narrator's instruction"
    misunderstood += "\nto continue your quest."
    misunderstood += "\n"

    while intro:
        # BBC Two - Limmy’s Show n.d., BBC, viewed 4 July 2021,
        # <https://www.bbc.co.uk/programmes/b00yy8pz>.

        # The variable named narration is used throughout the game to provide
        # story details and request the player for input. The variable is a
        # string as that type is suited for displaying text.
        #
        # This variable could also have names such as "message" or "storyline"
        # but I've gone with "narration" which is somewhat synonomous with
        # the aforementioned terms.

        narration = "\nGreetings, traveller!"
        narration += "\nWelcome to \'Falconhoof: The Call of Adventure!\'!"
        narration += "\nAre you ready to begin your quest?"
        narration += "\n"
        narration += "\nPress 'Enter' to start the game."

        sys.stdout.write(narration)

        sys.stdin.readline()

        # The following lines set boolean values for the scenes to progress.
        # This structure is used throughout the rest of the game.

        intro = False
        start_game = True

    while start_game:

        narration = "\nYou find yourself walking down a path that leads"
        narration += "\ninto a dark forest."
        narration += "\n"
        narration += "\nWhat do you want to do?"
        narration += "\n"
        narration += "\n1. Turn around and go home."
        narration += "\n2. Keep walking into the forest."
        narration += "\n"

        sys.stdout.write(narration)

        # The user_input variable takes input from the player in the form of a
        # string. This variable appears in almost all of the places where the user
        # is prompted for input.
        #
        # I've chosen to use a string type for this variable as I
        # can provide better feedback to the user when the expected response is
        # not received. I did try setting this variable type to int but was
        # unable to figure out a way to provide feedback to the user when a
        # string is entered.

        user_input = sys.stdin.readline().strip()

        # I've used an if-elif-else code block here as the user has two options
        # to progress the story. The else block allows for feedback to be provided
        # to the user when they input an invalid instruction.

        if user_input == "1":

            sys.stdout.write("\nWhere's your sense of adventure, Falconhoof?!")
            sys.stdout.write("\nGame Over.")

            start_game = False

        elif user_input == 2:

            sys.stdout.write("\nYou muster all of your courage and start walking")
            sys.stdout.write("\ndown the dark path into the forest.")
            sys.stdout.write("\n")

            start_game = False
            fork = True

        else:

            sys.stdout.write(misunderstood)

    while fork:

        narration = "\nYou come to a fork in the road."
        narration += "\nTo your left you can see a house in the distance."
        narration += "\nTo your right, the path continues..."
        narration += "\n"
        narration += "\n1. Turn left and walk towards the house."
        narration += "\n2. Turn right and walk further into the forest."
        narration += "\n"

        sys.stdout.write(narration)

        user_input = sys.stdin.readline().strip()

        if user_input == "1":

            narration = "\nYou turn left and walk towards the house."
            narration += "\n"
            sys.stdout.write(narration)

            fork = False
            witch = True

        elif user_input == "2":

            narration = "\nYou turn right and head further into the forest."
            narration += "\n"
            sys.stdout.write(narration)

            fork = False
            troll = True

        else:

            sys.stdout.write(misunderstood)

    while witch:

        # reference: Baum, LF 1900, The Wonderful Wizard of Oz | Children’s Classics |
        # Bedtime Stories, Storyberries, viewed 4 July 2021,
        # <https://www.storyberries.com/bedtime-stories-the-wonderful-wizard-of-oz-by-l-frank-baum/>.

        narration = "\nAs you approach the house, a witch stirring a couldron."
        narration += "\ncomes into view."
        narration += "\n"
        narration += "\nThe witch spots you."
        narration += "\nShe cackles and says \"I recently acquired some"
        narration += "\nflying monkeys from my sister who lives East of here."
        narration += "\n"
        narration += "\nTell you what, guess how many she gave me"
        narration += "\nand you can continue on your merry way, Falconhoof\""
        narration += "\n"
        narration += "\nHow many flying monkeys does the witch"
        narration += "\nhave locked up in her house?!"
        narration += "\n"

        sys.stdout.write(narration)

        guessing_game = True

        # This while block is used to keep track of how many guesses
        # have been made by the player. After three incorrect guesses
        # the game is ended.

        while guessing_game:

            # To keep the game interesting and less predictable, I've created a
            # code block that will change the correct number to be guessed by
            # the player each time the game is started.
            #
            # The flying_monkeys variable is passed the value of the random_number
            # variable. This will determine which of the two numbers in the
            # flying_monkeys_list variable will be the correct number to be
            # guessed by the player.
            #
            # The variable names here have been chosen to easily describe what is
            # happening with the values that are being created. I think if I used
            # shorter names such as "rn" for the random number that the code would
            # be less readable for other programmers reading the code.

            flying_monkeys_list = [random.randint(10, 15), random.randint(16,20)]
            random_number = random.randint(0, 1)
            flying_monkeys = flying_monkeys_list[random_number]


            # I had to use an int type variable for the user input here as the
            # following code blocks rely on evaluating wheter the guessed number
            # is either the correct guess and/or higher or lower than the correct
            # number. The downside of this is that if a string is entered then
            # ValueError is thrown as the program expects an integer to be entered.
            # The variable name has been adjusted so that the user_input variable
            # is not reused with a different data type.

            user_input_int = int(sys.stdin.readline().strip())

            guesses_remaining = 3

            # The following code block checks to see if the number entered by
            # the player is higher or lower than the correct number of flying
            # monkeys. I had to add the 'and guesses_remaining' conditions to the
            # if and elif sections so that when guesses_remaining is zero, or the
            # correct number has been guessed, the program escapes the loop. If
            # these conditions are not checked for the loop runs one too many
            # times. After the loop has been escaped, the program checks to see
            # if the correct number has been guessed and if not, the game ends.

            while guesses_remaining > 0:

                guesses_remaining -= 1

                if user_input_int < flying_monkeys and guesses_remaining > 0:

                    narration = "\n\"That's not right!"
                    narration = "\nI have more flying monkeys than that!!!\""
                    narration += "\nsays the witch."
                    narration += "\n"
                    narration += "\nGuess again, Falconhoof... "
                    narration += "\nYou have " + str(guesses_remaining) + " guesses remaining..."
                    narration += "\n"

                    sys.stdout.write(narration)

                    user_input_int = int(sys.stdin.readline().strip())

                elif user_input_int > flying_monkeys and guesses_remaining > 0:

                    narration = "\n\"Don't be silly, Falconhoof."
                    narration += "\nNobody needs that many flying monkeys.\""
                    narration += "\nsays the witch."
                    narration += "\n"
                    narration += "\nGuess again, Falconhoof... "
                    narration += "\nYou have " + str(guesses_remaining) + " guesses remaining..."
                    narration += "\n"

                    sys.stdout.write(narration)

                    user_input_int = int(sys.stdin.readline().strip())

            if user_input_int == flying_monkeys:

                narration = "\nWell done, Falconhoof! You have correctly"
                narration += "\nguessed the number of my flying monkeys."
                narration += "\n"
                narration += "\nGood luck on your journey."
                narration += "\n"

                sys.stdout.write(narration)

                guessing_game = False
                witch = False
                boulder = True

            else:

                narration = "\nThe witch turns you into a mouse and adds"
                narration += "\nyou to the bubbling brew in the cauldron."
                narration += "\n"
                narration += "\nGame Over."

                sys.stdout.write(narration)

                witch = False

    while troll:
        # The Three Billy Goats Gruff n.d., Storyberries, viewed 4 July 2021,
        # <https://www.storyberries.com/fairy-tales-the-three-billy-goats-gruff-by-Katharine-Pyle/>.

        narration = "\nAfter a short walk you come to a bridge."
        narration += "\n"
        narration += "\nAs you step onto the bridge a troll jumps out from"
        narration += "\nunder the bridge."
        narration += "\n"
        narration += "\nThe troll speaks. \"None shall pass, without a fight"
        narration += "\nor... correctly guessing my name!\""
        narration += "\n"
        narration += "\nA strange proposition indeed..."
        narration += "\n"
        narration += "\nWhat do you want to do?"
        narration += "\n"
        narration += "\n1. Fight"
        narration += "\n2. Guess the troll's name"
        narration += "\n"

        sys.stdout.write(narration)

        # The user_input variable is used again here with a string data type.
        # Again, this provides better feedback to the player when the expected input
        # is not provided.

        user_input = sys.stdin.readline().strip()

        fight = False
        guess_name = False

        if user_input == "1":

            fight = True

        elif user_input == "2":

            guess_name = True

        elif user_input != "1" or "2":

            sys.stdout.write(misunderstood)

        # In the following while loop, the 'and user_input...' conditions are added
        # so that the loop can be escaped when the corresponding number is entered.
        # This allows the guess_name state to be activated correctly after the
        # fight sequence has been initiated.

        while fight:

            repeats = 3

            while repeats > 0 and user_input == "1":

                repeats -= 1

                narration = "\nYou're a lover not a fighter, Falconhoof."
                narration += "\n"
                narration += "\nWhat do you want to do?"
                narration += "\n"
                narration += "\n1. Fight"
                narration += "\n2. Guess the troll's name"
                narration += "\n"

                sys.stdout.write(narration)

                user_input = sys.stdin.readline().strip()

            if repeats > 0 and user_input == "2":

                guess_name = True
                fight = False

            elif user_input != "1" or "2":

                sys.stdout.write(misunderstood)
                user_input = sys.stdin.readline().strip()

            else:

                narration = "\nViolence won't solve anything, Falconhoof."
                narration += "\n"
                narration += "\nGame over."

                sys.stdout.write(narration)

                fight = False
                guess_name = False
                troll = False

        # In this while loop the player is given 2 attempts to guess the troll's
        # name. Once again, I've implemented the 'and' condition to ensure that
        # the loop behaves as expected. I've also repeated a similar pattern
        # which as the witch's guessing game to make the correct response different
        # on each successive play through.

        while guess_name:

            names = ["Tim", "Greg", "Stuart", "Hubert"]
            random_name = random.randint(0, 3)
            troll_name = names[random_name].lower()

            narration = "\n\"I love a guessing game!\" says the troll."
            narration += "\n"
            narration += "\n\"I'll give you two attempts at guessing my name"
            narration += "\nand you can choose from the following names:"
            narration += "\n"
            narration += ", ".join(names) + "\""
            narration += "\n"

            sys.stdout.write(narration)

            user_input = sys.stdin.readline().strip().lower()

            attempts = 2

            # This while loop keeps track of the number of attempts the player
            # has made at guessing the troll's name. Using the 'and' condition
            # in the elif statement ensures the loop to progress correctly.

            while attempts > 0:

                attempts -= 1

                if user_input == troll_name:

                    narration = "\nWell done little man, you may cross the bridge."
                    narration += "\n"
                    narration += "\nGood luck on your journey."
                    narration += "\n"

                    sys.stdout.write(narration)

                    guess_name = False
                    boulder = True

                elif attempts > 0 and user_input != troll_name:

                    narration = "\nYou silly little man, that's not my name."
                    narration += "\n"
                    narration += "\nTry again."
                    narration += "\n"

                    sys.stdout.write(narration)

                    user_input = sys.stdin.readline().strip().lower()

                else:

                    narration = "\nYou have failed to guess my name little man."
                    narration += "\n"
                    narration += "\nThe troll gobbles you up."
                    narration += "\n"
                    narration += "\nGame Over."

                    sys.stdout.write(narration)

            guess_name = False
            troll = False

    while boulder:

        # BBC Two - Limmy’s Show n.d., BBC, viewed 4 July 2021,
        # <https://www.bbc.co.uk/programmes/b00yy8pz>.

        # As with previous challenges, I've added some randomness to keep the
        # game interesting and less repetitive. The 'force' list creates two
        # float numbers, which are then rounded to two decimal places. One of the
        # 'force' list's numbers is then selected randomly in the required_force
        # variable.

        force = [random.uniform(150.8, 160.1), random.uniform(200.2, 210.5)]
        rounded = round(force[0], 2), round(force[1], 2)
        random_force = random.randint(0, 1)
        required_force = rounded[random_force]

        narration = "\nYou continue through the forest and find yourself"
        narration += "\nin a moonlight meadow..."
        narration += "\n"
        narration += "\nA huge boulder sits in the middle of the meadow."
        narration += "\n"
        narration += "\nBeing the well travelled traveller that you are,"
        narration += "\nyou suspect that the boulder may be covering the"
        narration += "\nentrance to a hidden passage."
        narration += "\n"
        narration += "\nYou decide to roll the boulder out of the way."
        narration += "\n"
        narration += "\nHow much force will you use to push the boulder?"
        narration += "\n"
        narration += "\nEnter a number as it appears below to apply"
        narration += "\nthat many kilonewtons of force"
        narration += "\n"
        narration += "\n" + str(rounded[0])
        narration += "\n" + str(rounded[1])
        narration += "\n"

        sys.stdout.write(narration)

        # The user_input_float variable has been created here to compare the
        # player's input with the randomly generated number that is required to
        # be entered to progress in the game. Like the witch's guessing game,
        # an error will be thrown if a string is entered.

        user_input_float = float(sys.stdin.readline().strip())

        if user_input_float == required_force:

            narration = "\nYou push the boulder with " + str(required_force) + " kN of force."
            narration += "\n"
            narration += "\nThe boulder rolls in to a conveniently placed nook."
            narration += "\n"
            narration += "\nYou are now standing at the entrance of"
            narration += "\nVoldesad's Labyrinth!"
            narration += "\n"

            sys.stdout.write(narration)

        elif user_input_float != required_force:

            narration = "\nYou push the boulder with " + str(rounded[1]) + "kN"
            narration += "\nof force"
            narration += "\nThe boulder rolls back on you and crushes you..."
            narration += "\nGame Over."
            narration += "\n"

            sys.stdout.write(narration)

        boulder = False
        labyrinth = True

    while labyrinth:

        # BBC Two - Limmy’s Show n.d., BBC, viewed 4 July 2021,
        # <https://www.bbc.co.uk/programmes/b00yy8pz>.

        narration = "\nAfter walking for what seems like a short eternity"
        narration += "\nYou find yourself in the central chamber of Voldesad's"
        narration += "\nLabyrinth"
        narration += "\n"
        narration += "\nTo your left is the tunnel of no return, leading to"
        narration += "\nthe Chasm of Fire"
        narration += "\n"
        narration += "\nWithin the chamber is a statue of the Greek god, Hermes"
        narration += "\n"
        narration += "\nWhat do you want to do?"
        narration += "\n"
        narration += "\n1. Enter the tunnel of no return."
        narration += "\n2. Examine the statue"
        narration += "\n"

        sys.stdout.write(narration)

        user_input = int(sys.stdin.readline().strip())

        # The winged sandals are required to jump the Chasm of Fire, I've
        # created them as a Boolean value which is updated after the player examines
        # the Statue of Hermes. If the player progresses to the next room without
        # them, they are unable to cross the chasm which ends the game.

        winged_sandals = False

        if user_input == 1:

            narration = "\nYou enter the tunnel..."

            sys.stdout.write(narration)

            labyrinth = False
            chasm = True

        elif user_input == 2:

            narration = "\nYou examine the statue. There's a small plaque"
            narration += "\nat the base of the statue. It reads:"
            narration += "\n"
            narration += "\n\"Kiss my feet and I'll give you a treat!\""
            narration += "\n"
            narration += "\nYou've come too far not to heed the advice of"
            narration += "\nan inanimate object."
            narration += "\n"
            narration += "\nYou kiss the feet of Hermes."
            narration += "\n"
            narration += "\nLo and behold!!!"
            narration += "\n"
            narration += "\nA pair of winged sandals appears"
            narration += "\nnext to the statue!"
            narration += "\n"
            narration += "\nYou put the sandals on and head into"
            narration += "\nthe tunnel of no return..."

            sys.stdout.write(narration)

            winged_sandals = True
            labyrinth = False
            chasm = True

    while chasm:

        # BBC Two - Limmy’s Show n.d., BBC, viewed 4 July 2021,
        # <https://www.bbc.co.uk/programmes/b00yy8pz>.

        # In the final scene of the game, the player is only given the option
        # to attempt to jump the chasm of fire. As described earlier, the jump can
        # only be successful if the player has examined the Statue of Hermes.
        
        narration ="\nThe tunnel of no return closes behind you."
        narration +="\nYou stand at the edge of the chasm of fire."
        narration += "\n"
        narration +="\nOn the other side of chasm you see the Black Ruby"
        narration +="\nof Voldesad. Next to it is $2000 prize money"
        narration += "\n"
        narration += "\nThere's only one thing left to do, Falconhoof..."
        narration += "\n"
        narration += "Press 'Enter' to jump the chasm"

        sys.stdout.write(narration)

        sys.stdin.readline().strip()

        if winged_sandals:
            narration = "\nYou leap across the chasm of fire."
            narration += "\n"
            narration += "\nYou claim your cash prize and the Black Ruby of "
            narration += "\nVoldesad."
            narration += "\n"
            narration += "\nYour quest ends here, traveller."
            narration += "\n"
            narration += "\nThanks for playing!"

            sys.stdout.write(narration)

        else:
            narration = "\nYou make a pitiful jump into the flames."
            narration += "\n"
            narration += "\nGame Over."

            sys.stdout.write(narration)

        chasm = False

main()
