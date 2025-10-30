

import re
import random
from datetime import datetime

class SimpleChatBot:
    def __init__(self, name="Buddy"):
        self.name = name
        self.greetings = ["hi", "hello", "hey", "hiya"]
        self.farewells = ["bye", "goodbye", "see ya", "see you"]
        self.smalltalk = {
            "how are you": ["I'm fine, thanks! How about you?", "Doing great — ready to help!"],
            "what is your name": [f"My name is {self.name}.", f"I'm {self.name}. Nice to meet you!"],
            "time": [lambda: f"The time is {datetime.now().strftime('%H:%M:%S')}"]
        }

    def respond(self, text):
        t = text.lower().strip()

        if any(t.startswith(g) for g in self.greetings):
            return random.choice(["Hello!", "Hey there!", "Hi — what can I do for you?"])


        if any(t.startswith(f) for f in self.farewells):
            return random.choice(["Goodbye!", "Take care!", "See you later!"])


        for key, replies in self.smalltalk.items():
            if key in t:
                r = random.choice(replies)
                return r() if callable(r) else r


        if "help" in t:
            return "I can answer simple questions (time, name) or chat. Try asking 'what is your name' or 'time'."
        if re.search(r"\bweather\b", t):
            return "I can't access live weather here, but I can show you how to fetch it with an API if you want."

        # fallback: echo + suggestion
        return ("I didn't understand that exactly — could you rephrase?\n"
                "Or try: 'what is your name', 'time', 'help'.")

def main():
    bot = SimpleChatBot("AnanyaBot")
    print("SimpleChatBot — type 'quit' or 'exit' to stop.")
    while True:
        user = input("You: ").strip()
        if user.lower() in ("quit", "exit"):
            print("Bot:", random.choice(["Bye!", "See you!"]))
            break
        print("Bot:", bot.respond(user))

if __name__ == "__main__":
    main()
