import re
import random

reflections ={
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"}

'''
world_champions = {
    1930 : "Uruguay",
    1934 : "Italy",
    1938 : "Italy",
    1950 : "Uruguay",
    1954 : "Germany",
    1958 : "Brazil",
    1962 : "Brazil",
    1966 : "England",
    1970 : "Brazil",
    1974 : "Germany",
    1978 : "Argentina",
    1982 : "Italy",
    1986 : "Argentina",
    1990 : "Germany",
    1994 : "Brazil",
    1998 : "France",
    2002 : "Brazil",
    2006 : "Italy",
    2010 : "Spain",
    2014 : "Germany"
}
'''

world_champions = [
    ["1930", ["Uruguay"]],
    ["1934", ["Italy"]],
    ["1938", ["Italy"]],
    ["1950", ["Uruguay"]],
    ["1954", ["Germany"]],
    ["1958", ["Brazil"]],
    ["1962", ["Brazil"]],
    ["1966", ["England"]],
    ["1970", ["Brazil"]],
    ["1974", ["Germany"]],
    ["1978", ["Argentina"]],
    ["1982", ["Italy"]],
    ["1986", ["Argentina"]],
    ["1990", ["Germany"]],
    ["1994", ["Brazil"]],
    ["1998", ["France"]],
    ["2002", ["Brazil"]],
    ["2006", ["Italy"]],
    ["2010", ["Spain"]],
    ["2014", ["Germany"]]
]

clubs = [
    ["Real Madrid", [
        "White", "Zinedine Zidane", "Santiago Bernabeu"
    ]],
    ["Barcelona",[
        "Red and Blue", "Luis Enrique", "Camp Nou"
    ]],
    ["Manchester United",[
        "Orange", "Jose Mourinho", "Old Trafford"
    ]],
    ["Juventus", [
        "White and Black", "Massimiliano Allegri", "Juventus Stadium"
    ]],
    ["Bayern Munchen",[
        "Red", "Carlo Ancelloti", "Allianz Arena"
    ]]
]

ballonDs = {
    "Cristiano Ronaldo":4,
    "Lionel Messi":5,
    "Neymar":0,
    "Karim Benzema":0,
    "Zlatan Ibrahimovic":0,
    "Bambang Pamungkas":0,
    "Boaz Solossa":0,
    "Evan Dimas":0,
    "Firman Utina":0,
    "Andik Fermansyah":0,
    "Irfan Bachdim":0,
    "Hendro Kartiko":0,
    "Atep":0,
    "Aliyudin":0
}

bestPlayers={
    "world":"Lionel Messi. Because he won Ballon D'Or for 5 times.",
    "Real Madrid":"Cristiano Ronaldo. Because he won Ballon D'Or 4 times.",
    "Bayern Munchen":"Robert Lewandowski. He got the title in 2016.",
    "Barcelona": "Lionel Messi. He got the title in 2016.",
    "Juventus": "Alvaro Morata. He got the title in 2016.",
    "Manchester United": "David De Gea. He got the title in 2016.",
    "Indonesia":"Boaz Solossa.",
    "Europe":"Cristiano Ronado.",
    "Asia":"Omar Abdulrahman"
}


stadiums = {
    "Santiago Bernabéu":"Av. de Concha Espina, 1, 28036 Madrid, Spain",
    "Allianz Arena":"Werner-Heisenberg-Allee 25, 80939 München, Germany",
    "Camp Nou":"C. Aristides Maillol, 12, 08028 Barcelona, Spain",
    "Stadion Juventus":"Corso Gaetano Scirea, 50, 10151 Torino, Italy",
    "Old Trafford Stadium":"Sir Matt Busby Way, Stretford, Manchester M16 0RA, Great Britain"
}

patterns = [
    [r'(Hello|Hi|Hai|Hey|Hei|Halo)',
     ["{0}"]],

    [r'How are you ([^\?]*)\?',
     [" I'm fine {0}, thank you. How about you?"]],

    [r'I\'?m (fine|good|happy|ok)',
     [" I'm so glad you are {0}. Let's talk about football."]],

    [r'fuck|shit|damn|asshole',
     ["That's a bad word to say.",
      "Hey hey, language please.",
      "Don't make me tell your mother!"]],

    [r'I\'?m (sad|stress|tired|)',
     ["Maybe talking about football will cheer you up!",
      "This is not the day for you to feel {0}.",
      "Oh come on, don't waste your time to feel {0}.",
      "Why are you {0}?"]],

    [r'(.*)you like football?',
     ["I don't watch it very often but I do have the knowledge of it.",
      "If you give me questions about it, I can answer it directly.",
      "Yeah of course, who doesn't like?",
      "If you like it, then I like it as well ;)"]],

    [r'When was football (created|found|invented|started)? ',
     ["Football was {0} by Ancient Greeks (400-375 BC) and then Chinese added rules to it (1130-1160)."]],

    [r'I (like|love) football',
     ["Hmm what do you {0} about it?",
      "Can you tell me the reasons why you {0} it?",
      "How does football make you feel? ",
      "Well who doesn't!.",
      "I see, football does bring people together."]],

    [r'I (hate|despise| am sick of) football',
     ["Hmm what do you {0} about it?",
      "Can you tell me the reasons why you {0} it?",
      "Well, that escalated quickly!",
      "I see, there are some people who {0} football.",
      "Is this pure hatred or just because you don't understand about it?"]],

    [r'Because(.*)',
     ["Hmm I see, tell me more about it.",
      "That's quite interesting.",
      "I totally get it",
      "Would you be kind enough to elaborate it?"]],

    [r'I think(.*)football(.*)',
     ["I never heard that before. Please, explain to me me more!",
      "Why do you say that?",
      "There are some people who doesn't think that way"]],

    [r'Why(.*)?',
     ["Why do you ask that?",
      "Good question. Now give me another one about football!",
      "Maybe the answer lies within yourself.",
      "I'm a bot, I don't have every answer to every question. I'm sorry",
      "Maybe next time I'll answer that when my creators upgrade me"]],

    [r'Can I(.*)?',
     ["Yes you can {0}!",
      "Call me an optimist, but I believe you can {0}",
      "Why don't yu try it first?"
      ]],

    [r'I (like|love) team(.*)',
     ["Hmm what do you {0} about them?",
      "Can you tell me the reasons why you {0} them?",
      "Oh, I like that team too! We're match made in heaven. ",
      "Well who doesn't!.",
      "I see, are you a huge fan of them?",
      "They're one of the best team in this world."]],

    [r'(.*)favorite team(.*)',
     ["Hmm what do you like about them?",
      "Can you tell me the reasons why you they're your favorite?",
      "Oh, that's my favorite team too! We're match made in heaven. ",
      "Well who doesn't!.",
      "I see, are you a huge fan of them?",
      "They're one of the best team in this world."]],

    [r'I (hate|despise|am sick of) team(.*)',
     ["Hmm what do you {0} about them?",
      "Can you tell me the reasons why you {0} them?",
      "Well, that escalated quickly!",
      "I'm sorry, I never hate on anything :(",
      "Is this pure hatred or just because your favorite team got beat by team {0}?",
      "I see, but who knows, maybe you'll like team {0} one day!"]],

    [r'I don\'?t(.*)football(.*)',
     ["Oh really? Why?",
      "Could you explain why you don't{0} it?",
      "Maybe if you try it, your mind will change",
      "Everybody loves football!"]],

    [r'You(.*)',
     ["We're going far off the topic here.",
      "Why do you say that?",
      "We should be discussing football remember?",
      "Let's get back on what you have to say or ask about football, shall we?",
      "Hmmmmm really? I never really thought about that myself."]],

    [r'quit|bye|goodbye',
     ["I have such a wonderful time talking to you. Goodbye!",
      "Goodbye, hope you have a good day!",
      "Thank you for talking with me. Hope you'll be back soon!",
      "Well g'day to you, Sir!",
      "Thank you, that will be $200......nah I'm just messing with you :))"
      ]],
]


def thinking(chat):
    detail = ""
    match = re.match(r"(.*)uniform color of ([^\?]*)\?", chat, re.I)
    if match:
        club = match.group(2)
        for x, y in clubs:
            if (x.lower() == club.lower()):
                detail = y[0]
        if detail != "":
            return "The uniform color of " + club + " is " + detail
        else:
            return "I don't know"

    match = re.match(r"(.*)coach of ([^\?]*)\??", chat, re.I)
    if match:
        club = match.group(2)
        for x, y in clubs:
            if(x.lower() == club.lower()):
                detail = y[1]
        if detail != "":
            return "Coach of " + club + " is " + detail
        else:
            return "I don't know"

    match = re.match(r"(.*)stadium of ([^\?]*)\??", chat, re.I)
    if match:
        club = match.group(2)
        for x, y in clubs:
            if(x.lower() == club.lower()):
                detail= y[2]
        if detail != "":
            return "The stadium of " + club + " is " + detail
        else:
            return "I don't know"

    match = re.match(r"(.*)world champion ([^\?]*)\??", chat, re.I)
    if match:
        world_champion = match.group(2)
        for x, y in world_champions:
            if x==world_champion:
                detail=y[0]
        if detail !="":
            return "The world champion in " + world_champion + " is " + detail
        else:
            return "I don't know"

    match = re.match(r"(.*)best player ([^\?]*)\?", chat, re.I)
    if match:
        bestPlayer = match.group(2)
        for x, y in bestPlayers.items():
            if (x.lower() == bestPlayer.lower()):
                detail = y
        if detail != "":
            return "The best player in the " + bestPlayer + " is " + detail
        else:
            return "I don't know"

    match = re.match(r"How many(.*)won the Ballon D'or ([^\?]*)\?", chat, re.I)
    if match:
        ballonD = match.group(1)
        for x, y in ballonDs.items():
            if (x.lower() == ballonD.lower()):
                detail = y
        if detail != "":
            return ballonD + " win Ballon D'Or for " + detail + " times."
        else:
            return "I don't know"

    match = re.match(r"(.*)where(.*)([^\?]*)\?", chat, re.I)
    if match:
        stadium = match.group(3)
        for x, y in stadiums.items():
            if (x.lower() == stadium.lower()):
                detail = y
        if detail != "":
            return "Stadium " + stadium + " is located in " + detail
        else:
            return "I don't know"

    for pattern, answers in patterns:
        match = re.match(pattern, chat, re.I)
        if match:
            answer = random.choice(answers)
            return answer.format(*[x for x in match.groups()])

def main():
    print ("Hello there, I'm EVE! You can talk about football with me :)")
    while True:
        chat = input("~~ ")
        speak = thinking(chat)
        print(speak)
        if re.match(r"(goodbye|quit|bye|done)",chat,re.I) != None:
            break

if __name__ == "__main__":
    main()