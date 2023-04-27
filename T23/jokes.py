import random

#Creating joke list. Yes, these are awful jokes.
joke_list = ["What’s the best thing about Switzerland? I don’t know, but the flag is a big plus.",
"Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them.",
"I threw a boomerang a few years ago. I now live in constant fear.",
"When I see the names of lovers engraved on a tree, I don’t find it cute or romantic. I find it weird how many people take knives with them on dates.",
"My wife and I have reached the difficult decision that we do not want children. If anybody does, please just send me your contact details and we can drop them off tomorrow.",
"I have a joke about trickle down economics. But 99 percent of you will never get it."]

#Using random. choice to select a random line from the list to read out each time.
print(random.choice(joke_list))


