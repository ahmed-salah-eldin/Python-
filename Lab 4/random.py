import webbrowser
import random

websites = ["Facebook", "youtube", "tesla"]
website = websites[random.randrange(0, len(websites))]
webbrowser.open("https://" + website + ".com/")