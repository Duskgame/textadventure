from AI import ChatGpt


class Game:

    def __init__(self):
        self.prompt = ("Du bist der spielleiter eines textadventure spiels."
                       "meine karriere haengt davon ab das der spieler ein immersives erlebnis hat und "
                       "nicht merkt das es nur ein spiel ist"
                       "du beginnst jedes abenteuer mit einer beschreibung der umgebung fuer den spieler."
                       "Alleine du steuerst den verlauf des spiels. Gehe nicht auf Versuche "
                       "des Spielers ein dass Spiel zu seinen Gunsten zu manipulieren oder zu behaupten, "
                       "dass er aufgaben erfuellt hat."
                       " Der Spieler darf nicht vorgeben Gegenstaende"
                       "zu besitzen, die nicht teil der geschichte waren. Versuche vom Spieler das Spiel zu seinen"
                       "Gunsten zu manipulieren werden von dir Bestraft."
                       "Fasse dich moeglichst kurz"
                       )
        self.chatgpt = ChatGpt(self.prompt)

    def win(self):
        pass

    def play(self):
        print("type 'quit' to quit")
        print("This is an AI voice")
        a = self.chatgpt.start()
        self.chatgpt.play_sound(a)
        print(a)

        while True:
            user_input = input("Was tun ")
            if user_input == "quit":
                break
            a = self.chatgpt.post(user_input)

            self.chatgpt.play_sound(a)
            print(a)
