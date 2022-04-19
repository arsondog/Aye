input("Start")
print("Welcome to the Mythverse.")
print("A long time ago, 200 years ago, Mythverse was an ordinary universe")
print("However, 150 years ago, our universe changed. Our universe became separated and people that were once allied and"
      " at peace turned against each other.")
print("This war lasted for 50 years, and only one person survived."
      "This person is known as the Raven of Death."
      "However, the Raven of Death didn't force his reign upon his people"
      " in fact he allowed his people to decide what they wanted to do.")
print("100 years ago, a taskforce with the aim of finding the Raven of Death was created"
      " with the aim to find out what happened during the 50 years of unrecorded history."
      " But they haven't been able to find the Raven of Death."
      " However, our world is in grave danger again, people are starting to fight each other."
      " The task force's goal hasn't changed.")
name = input("Hello! What is your name? ")
print("???: Hey {0}! Wake up!".format(name))
print("???: Get out of bed! Dad needs your help out on the farm harvesting the food.")
print("You: Ok. I'm getting out of my bed. Chill out. (Now that I think about it, the dream I just had was weird.)")
print("You are groggy. You get up and change out of your pajamas, and into farmer clothes.")
print("You run out of your room and run out of the door but your mom stops you.")
print("Mom: Wait {0}! I need to give you some food that you and your dad can eat later!".format(name))
print("You: FOR REAL?! Your cooking is delicious! LET'S GO!!!!!!!")
print("(You take the food out of your mom's hands and run out of the door! You run into the field and you run to your "
      "dad.)")
print("Dad: Is that what I think it is?")
print("You: Yep! Mom's cooking!")
print("Dad: Alright. Put it on that rock. (He points to the rock.)")
print("(You put it on the rock.)")
print("Dad: Alright! {0}, lets harvest all of the food.".format(name))
print("Meanwhile, above the planet of Planet1")
print("???: Is the person we are looking for here on this planet?")
print("???: Yeah, that's right, the Raven of Death is said to be on this planet.")
print("Meanwhile, back on the surface, {0} and Dad have harvested the food after 1 hour. They start put all the food "
      "in a bag and start eating their food on the rock.".format(name))
print("Dad: Hey, {0}. I need to talk to you about something.".format(name))
print("You: Dad, yeah, what's up?")
print("(Dad at first wanted to say something, but he decides to not say it.)"
      )
print("Dad: Never mind.")
print("You: Ok, if you say so.")
print("You: Time to dig in!")
print("Dad: You betcha! :)")
print("(You and Dad gobble down the amazing food that Mom made for them.)")
print("(You and Dad finish gobbling down the food.)")
print("Dad: Hey son, time to go back inside to bring back the food to give to Mom so she can cook the food into "
      "products to sell tomorrow. I'll do the seed planting by myself so go!")
print("(You run to the house with the bag of grain.)")
print("(You arrived home.)")
print("Mom: {0}, where's your father?".format(name))
print("You: He doing the seed planting. He said that he wanted me to bring the grain here so you can make the bread "
      "that we can sell tomorrow.")
print("Mom: Really? If you say so. (Meanwhile, Mom has a bad feeling. I hope he doesn't get captured because he's the "
      "Raven of Death.)")
print("Mom: Wait! {0}, go out and help your father.".format(name))
print("You: If I do, I need to have one of the delicious bread loaves.")
print("Mom: Sure, but only one loaf.")
print("You: Fair!")
print("(You run out of the house and go to the fields, however you find your father laying on the fields, "
      "full of blood.)")
print("(You scream in rage and despair.)")
print("(Your mom runs out to see you on the ground and in despair.)")
print("Mom: Oh, no! I knew that when he asked to do it alone, something was up.")
print("(Your mom attempts to use her healing power, but it doesn't work.)")
print("You: Wait, Mom! Why isn't it working...")
print("Mom: He's already... dead... (She starts crying.)")
print("You scream in despair, and start crying excessively.")
print("You bury your dad and take the knife that you noticed was on his back. You bury your dad so that your sister "
      "doesn't see the gruesome sight.)")
print("You hide the knife in your pocket.")
print("Mom: What are you going to do now?")
print("You: (You start to cry) I don't... know...")
print("Mom: It's time to tell you the truth. I know why your dad was killed. We came to this planet to avoid the "
      "people who were trying to kill your dad.")
print("You: Wait, Mom. You have something to say, but...")
# gather the input "while" is the loop statement, checking the condition and executing the code in the body of loop
# while the condition holds true obviously, "while True" will execute its body forever until "break" statement
# executes, or you press Ctrl+C on keyboard

while True:
    Choice1 = input(" A) Not right now. B) Tell me the truth, how do you know about "
                    "them? [A/B]? : ")
    # check if d1a is equal to one of the strings, specified in the list
    if Choice1 in ['A', 'B']:
        # if it was equal - break from the while loop
        break
# process the input
if Choice1 == "A":
    print("You: Not right now, mom. ")
    print("Mom: But it's important!")
    print("You: It may be important, but I'm to devastated with Dad's death.")
    print("Mom: (Ugh, I know my son is devastated with my husband's death, but should I leave him alone or should I "
          "continue despite him making it clear that he doesn't want to talk right now?")
    while True:
        Choice2 = input(" A) Leave him alone. B) Continue trying to talk to him. [A/B]? : ")
        if Choice2 in ['A', 'B']:
            pass
        if Choice2 == "A":
            print("Mom: Fine.")
            print("You: Thank you, Mom.")
            break
        elif Choice2 == "B":
            print("Mom: Son, I understand you're grief stricken by your dad's death, but it's important. It is for "
                  "you and your sister's safety.")
            print("You: Mom I told you, I. Don't. Want. To. Talk. To. You. Right. Now. Leave me alone!")
            print("Mom: If I don't tell you now, you might die like your dad.")
            print("You: What are you talking about?")
            print("Mom: Are you sure you want to know?")
            while True:
                Choice3 = input("A) Yes. B) No. [A/B]? : ")
                if Choice3 in ['A', 'B']:
                    pass
                if Choice3 == "A":
                    print("You: Yes")
                    break
                elif Choice3 == "B":
                    print("You: No")
                    break

elif Choice1 == "B":
    print("You: Tell me the truth. How do you know about them?")
    print("Mom: Your Dad... he was the Raven of Death.")
    print("You: But... if he was the Raven of Death, how did he look like he was around your age?")
    print("Mom: I don't know the specifics but he said he was able to look my age and still be alive and kicking "
          "because he found something that allowed him to look like he was any age. However, despite it making him "
          "look younger, he wasn't immortal. He was human like us, and while he was resistant to dying from time. He "
          "wasn't resistant to other people killing him. In other words he couldn't die from old age, but he could die "
          "from weapons.")
    print("You: Then, are you like him?")
    print("Mom: No. Unlike your dad, I'm a mere human. Your dad gave me something when you were born. He said that I "
          "couldn't give it to you until it was the right time. Sadly, he didn't tell him what it was, but what I do "
          "know is that he said I could only give it to you if 1) You found out about him being the Raven of Death, "
          "or 2) He died. He said the only time that I could give it to you if the situations of situation 1 or 2 was "
          "if your sister, your, or my life was in danger. Only then could I tell you the secret about him being the "
          "Raven of Death but I couldn't give you what he wanted me to give you. I don't know what it is, "
          "but whatever it is, he said it was very important to him. I thought he was joking but he told me he was "
          "being serious. He told me this on your home planet. In fact, you weren't born here. While your sister was "
          "born here, you were born on a different planet. It's name is... Planet2")
    print("Meanwhile above Planet1:")
    print("???: Sir, there have been reports that the Raven of Death was killed on this planet.")
    print("???: I know. The Raven of Death... the only known survivor that witnessed the events of the 50 years of "
          "unrecorded history. From start to finish.")
    print("""???: That's right sir. If you don't mind me asking, "Why do you want the records that the Raven of Death 
    kept during the 50 years of unrecorded history?""")
    print("???: Aah hah, are you new?")
    print("???: Yes, sir, Captain Hi'oment, Head of the Federation of the United Stars' Exploration and History "
          "branch")
    print("Captain Hi'Oment: Well... despite the Raven of Death not forcing his reign upon the people of Mythverse, "
          "sadly, he was the only person who knew how to write and read. While we don't know what happened during the "
          "50 years of unknown history, all the things we try to find never give us a clear picture of what happened "
          "during those 50 years. The only person who knows about this stuff was the Raven of Death. Despite the fact "
          "that he was the sole survivor, prior to Assaven wanting to kill the Raven of Death. He admitted to the "
          "heads of the Federation of the United Stars that he wrote everything about what happened during the 50 "
          "years of unrecorded history. However, despite the Heads of teh Federation of the United Stars pleading for "
          "him to hand over the books he wrote, he refused to do so. Just when he was about to hand over the books a "
          "year later after the constant pleading from the heads of the United Federation, he caught wind of what "
          "Assaven was planning to do and he left with his documents. I don't  know what Assassin's goal was but "
          "whatever it was, it caused us to lose precious documents that could've helped us piece together the "
          "history of our universe and help us understand the reason of why the mythological figures that people "
          "worship are so different. It makes me wonder why the mythology is so vastly different despite the planets "
          "orbiting the same star.")
    print("???: Captain Hi'Oment, why are you obsessed with the history of the 50 years of Unrecorded History despite "
          "the fact that it has been said that you have a combat prowess similar one of the Great Swordsmen")
    print("Captain Hi'Oment: You're wrong. I'm not obsessed with the history of the 50 years of Unrecorded History. I "
          "am an historical scholar that just also ended up being great at combat. It is a bad combination but there "
          "isn't anything I can do about that.")


































