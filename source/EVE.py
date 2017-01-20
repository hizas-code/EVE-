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

patterns = [
    [r'(Hello|Hi|Hai|Hey|Hei|Halo)',
     ["{0}"]],

    [r'How are you ([^\?]*)\??',
     [" I'm fine {0} thank you, how about you?"]],

    [r' (.*) you like football?',
     ["I don't watch it very often but I do have the knowledge of it.",
      "If you give me questions about it, I can answer it directly.",
      "Yeah of course, who doesn't like?",
      "If you like it, then I like it as well ;)"]],

    [r' When was football (created|found|invented|started)? ',
     ["Football was {0} by Ancient Greeks (400-375 BC) and then Chinese added rules to it (1130-1160)."]],

    [r' (.*) coach of (real madrid|Real Madrid|realmadrid|real Madrid|Real madrid)?',
     ["Coach of {0} is Zinédine Zidane."]],

    [r' (.*) coach of (bayern mucnhen|Bayern Munchen|bayernmunchen|bayern Munchen|Bayern munchen)?',
     ["Coach of {0} is Carlo Ancelotti."]],

    [r' (.*) coach of (barcelona|Barcelona)?',
     ["Coach of {0} is Luis Enrique Martínez García."]],

    [r' (.*) coach of (juventus|Juventus)?',
     ["Coach of {0} is Massimiliano Allegri."]],

    [r' (.*) coach of (Manchester United|manchester united|manchesterunited|manchester United|Manchester united)?',
     ["Coach of {0} is Jose Mourinho."]],

    [r' I (like|love) football',
     ["Hmm what do you {0} about it?",
      "Can you tell me the reasons why you {0} it?",
      "How does football make you feel? ",
      "Well who doesn't!.",
      "I see, football does bring people together."]],

    [r' I (hate|despise| am sick of) football',
     ["Hmm what do you {0} about it?",
      "Can you tell me the reasons why you {0} it?",
      "Well, that escalated quickly!",
      "I see, there are some people who {0} football.",
      "Is this pure hatred or just because you don't understand about it?"]],

    [r' (.*) football (.*)',
     ["Hmm I see, tell me more about it.",
      "I never heard that before. Please, fascinate me more!",
      "That's quite interesting.",
      "Why do you say that?",
      "I totally get it",
      "Would you be kind enough to elaborate it?",
      "Does anyone ever tell you that you have such an amazing way of thinking?",
      "IKR!"]],

    [r' You (.*)?',
     ["We're going far off the topic here.",
      "Why do you ask that?",
      "I can only answer question about football, remember?",
      "Maybe the answer lies within yourself.",
      "I'm a bot, I don't have every answer to every question. I'm sorry",
      "Maybe next time I'll answer that when my creators upgrade me"]],

    [r' I (like|love) team (.*)',
     ["Hmm what do you {0} about them?",
      "Can you tell me the reasons why you {0} them?",
      "Oh, I like that team too! We're match made in heaven. ",
      "Well who doesn't!.",
      "I see, are you a huge fan of them?",
      "They're one of the best team in this world."]],

    [r' I (hate|despise|am sick of) team (.*)',
     ["Hmm what do you {0} about them?",
      "Can you tell me the reasons why you {0} them?",
      "Well, that escalated quickly!",
      "I'm sorry, I never hate on anything :(",
      "Is this pure hatred or just because your favorite team got beat by team {0}?",
      "I see, but who knows, maybe you'll like them one day!"]],

    [r' I don\'?t  (.*) football (.*)',
     ["Oh really? Why?",
      "Could you explain why you don't {0}",
      "Maybe if you try {0}, your statement will change",
      "The question is: do you want to{0}?"]],

    [r' You (.*)',
     ["We're going far off the topic here.",
      "Why do you say that?",
      "We should be discussing football remember?",
      "Let's get back on what you have to say or ask about football, shall we?",
      "Hmmmmm really? I never really thought about that myself."]],

    [r' quit|bye|goodbye',
     ["I have such a wonderful time talking to you. Goodbye!",
      "Goodbye, hope you have a good day!",
      "Thank you for talking with me. Hope you'll be back soon!",
      "Well g'day to you, Sir!",
      "Thank you, that will be $200......nah I'm just messing with you :))"
      ]],

[r' (.*)',
     ["We're going far off the topic here.",
      "Why do you say that?",
      "We should be discussing football remember?",
      "Let's get back on what you have to say or ask about football, shall we?",
      "Hmmmmm really? I never really thought about that myself."]],
]

#Knowledge

world_champion = {
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
    2014 : "Germany",
}

uefa_champion = [

]

club = {
    "Real Madrid": [
        "White", "Zinedine Zidane", "Santiago Bernabeu"
    ],
    "Barcelona": [
        "Red and Blue", "Luis Enrique", "Camp Nou"
    ],
    "Manchester United" : [
        "Orange", "Jose Mourinho", "Old Trafford"
    ],
    "Juventus": [
        "White and Black", "Massimiliano Allegri", "Juventus Stadium"
    ],
    "Bayern Munchen": [
        "Red", "Carlo Ancelloti", "Allianz Arena"
    ]
}

#END

def thinking(chat):
    for pattern, answers in patterns:
        match = re.match(pattern, chat, re.I)
        if match:
            answer = random.choice(answers)
            return answer.format(match.group())

def main():
    print ("Hello there, I'm EVE! You can talk about football with me :)")
    while True:
        chat = input("~~ ")
        speak = thinking(chat)
        print(speak)
        if chat == "quit":
            break

if __name__ == "__main__":
    main()