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

pattern = [
    [r'(Hello|Hi|Hey)',
     ["{0}"]],

    [r'How are you ([^\?]*)\??',
     [" I'm fine {0} thank you, how about you?"]],

    [r'I\'?m (fine|good|happy|ok)',
     [" I'm so glad you are {0}. Let's talk about football"]],

    [r'(.*)fuck|shit|damn|asshole(.*)?',
     ["That's a bad word to say",
      "Hey hey, language please",
      "Don't make me tell your mother!"]],

    [r'I\'?m (sad|stress|tired|)',
     ["Maybe talking about football will cheer you up!",
      "This is not the day for you to feel {0}",
      "Oh come on, don't waste your time to feel {0}",
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
      "Could you explain why you don't {0}",
      "Maybe if you try it, your mind will change",
      "The question is: do you want to{0}?"]],

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


def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in reflections:
            tokens[i] = reflections[token]
    return ' '.join(tokens)


def analyze(statement):
    for patterns, responses in pattern:
        match = re.match(patterns, statement.rstrip(".!"), re.I)
        if match:
            response = random.choice(responses)
            return response.format(*[reflect(g) for g in match.groups()])


def main():
    print ("Hello there, I'm EVE! You can talk about football with me :)")

    while True:
        statement = input("> ")
        print (analyze(statement))

        if statement == "quit":
            break


if __name__ == "__main__":
    main()