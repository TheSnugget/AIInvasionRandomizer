# !!! requires manunally modifying stuff on lines 16-19 and 108 !!!
# on start, replace the contents of unownedCountriesList (line 19) with the contents of the country list for the current region, then remove the starting country from the list.

import random
from random_word import RandomWords
import pyttsx3
engine = pyttsx3.init()
r = RandomWords()
engine.setProperty('rate', 180)


# currently limited to europe, will add more regions soonish
europeanCountriesList = ["Portugal", "Spain", "France", "The UK", "Ireland", "Iceland", "Belgium", "Luxembourg", "The Netherlands", "Germany", "Denmark", "Switzerland", "Italy", "Austria", "Czechia", "Poland", "Slovakia", "Hungary", "Slovenia", "Croatia", "Bosnia", "Serbia", "Albania", "Greece," "Macedonia", "Bulgaria", "Romania", "Moldova", "Ukraine", "Belarus", "Lithuania", "Latvia", "Estonia", "Finland", "Sweden", "Norway"]
europeTerraformList = ["Drain the Water between The UK and France, claiming the land for myself.", "Drain the Water between The UK and Ireland, claiming the land for myself.", "Drain the Baltic Sea, claiming the land for myself.", "Drain the Mediterranian Sea, taking the land for myself.", "Drain the Black Sea, taking the land for myself.", "Take The UK off the map.", "Take France off the map.","Cut Denmark off of the mainland via river.", "Cut Italy off of the mainland via river.", "Flood the Netherlands.", "Create the Corruption in Iceland."]

# manually modify these lists
ownedCountriesList = ['placeholder to prevent crashing']
adjacentCountriesList = ['placeholder 2']
unownedCountriesList = ["Poland", "Portugal", "Belgium", "Spain", "France", "The UK", "Ireland", "Iceland", "Luxembourg", "The Netherlands", "Germany", "Denmark", "Switzerland", "Italy", "Austria", "Czechia", "Slovakia", "Hungary", "Slovenia", "Croatia", "Bosnia", "Serbia", "Albania", "Greece," "Macedonia", "Bulgaria", "Romania", "Moldova", "Ukraine", "Belarus", "Lithuania", "Latvia", "Estonia", "Finland", "Sweden", "Norway"]
playerList = ["The Randomizer"]

# don't modify these ones!!
sponsorList = ["Nord VPN", "Raid Shadow Legends", "Genshin Impact", "Brilliant", "Skillshare", "Audible", "Wren", "Displate"]
invasionModifierList = ["Explosives.", "Guns.", "Knives.", "Nothing.", "Big Rocks.", "A Battalion of Explosive Bunnies.", "Sheer Intimidation.", "Really Cool Wigs.", "Flying Sharks.", "The Unmatched Power of The Sun (via a magnifying glass).", "Hand Grenades.", "Crossbows.", "Candy Bars.", "A Mildly Concerning Amount of Shelves.", "A Discussion Over Tea.", "Waffle House Employees.", "Alcohol.", "Flamethrowers.", "Alcohol Powered Flamethrowers.", "Really Annoying Sounds.", "Political Divide.", "Sticks and Stones to Break Their Bones.", "Sharpened Femur Bones.", "An Invasive Species.", "Chemicals to Dump Into Their Water Supply.", "Man-Made Horrors Beyond Their Comprehension.", "Snails.", "Snails with Guns.", "Snails with Really Big Guns.", "Orbital Lasers.", "A Rod From God.", "Unmatched Pizzazz.", "Forklifts.", "A Flood of Molasses.", "Intent To Explode Their Nuclear Reactors.", "OSHA Violations.", "A New Plague.", "French Bread.", "Lawsuits.", "Cameras." "The Fog.", "Wine Glasses with Wheels.", "Their Worst Nightmares.", "Entire Trees."]
soldierModifierList = ["Very Tired.", "Forklift Certified.", "Banned from Operating Forklifts in 107 Countries.", "Clownly.", "Dancing.", "Poor.", "Idiotic.", "Materialistic.", "Suffering from a Terrible Back Injury.", "Divorced.", "Frightening.", "Extremely Drunk.", "Laughing Really Hard.", "Rich.", "8 Feet Tall.", "Chickens.", "Disguised As Gorillas.", "Cosplaying As Barack Obama.", "Fish.", "Clinically Insane.", "Made of Jewels.", "Football Players (American)", "Football Players (Not American)", "Martians.", "Floating.", "Vampires.", "Riding Motorcycles.", "Dressed as Jesus Christ.", "1 Year Old.", "Eating Salmon.", "Chainsmoking.", "Conspiracy Theorists.", "Biologists.", "The Real MrBeast.", "The Fake MrBeast.", "Stuffed Inside A Robot Suit.", "Goats.", "Colorblind.", "Blind.", "Benny Worm", "Really Big Fans of Apples (probably horses).", "Actually Just Blades of Grass.", "Drinking Nitroglycerin.", "a Swarm of Bees.", "Sporting really long Beards.", "Huge fans of Weezer.", "Frequent Consumers of Grass.", "Prone to Spontaneous Ascension.", "Not Very Polite.", "Advertising " + sponsorList[random.randint(0,len(sponsorList)-1)] + ".", "Pleading for Help."]
allianceModifierList = ["over A Cup Of Tea.", "by Pleading on My Knees.", "by Threatening Them with A Nuke I don't have.", "by Bribing Them with The Most Recent Resource I've Aqcuired.", "by Bribing Them With Drugs.", "By Drugging Them.", "by Poisoning Their Water Supply and Offering To Clean It.", "with a Blood Sacrifice.", "With a MrBeast Challenge.", "By Convincing Them that The Moon Is Evil.", "By Inviting Them Onto The Joe Rogan Podcast.", "By Holding Them At Gunpoint.", "By Strategically Assassinating Any Political Figures Who Would Deny The Treaty.", "By Offering to Build A Corner Store In Their Country.", "By having an intellectual conversation about the state of modern AI.", "Challenging their Leader to a Duel.", "Over a Game of Chess.", "Over a Game of Clue.", "By Offering them a Lifetime Supply of Gravel.", "By Lighting The Diplomat on Fire.", "By Advertising " + sponsorList[random.randint(0,len(sponsorList)-1)] + ".", "By Hitting Them Until They Accept."]
buildingList = ["A Statue of Hatsune Miku", "A Gun Factory", "A Great Wall", "A Dam", "A Bridge to Iceland", "Nuclear Silos", "A Really Big Chess Board", "An Anvil Factory", "A Car or Two", "A God", "A Rest Stop along the highway", "A reason to Fear", "A Rocket to piss off NASA", "A Portal to Hell", "A bed", "A Really Cool Gas Station", "A replica of the Bass Pro Shop Pyramid", "A replica of the Eiffel Tower", "A Large Beehive", "A Big Pumpkin with a Pumpkin Factory inside", "An Olive Garden", "A Series of Underground Tunnels", "A Pit Straight to Hell", "An Artificial Volcano", "An Art Museum", "A Private Club for the 1% Who Definitely Need More Stuff.", "A Haphazard Tower of Furniture", "A Way Out Of The Simulation", "The Smallest Castle in the World", "A Shrine to Today's Sponsor; " + sponsorList[random.randint(0,len(sponsorList)-1)], "A Gun Store"]
characterList = ["Spamton G. Spamton", "Hatsune Miku", "Santa Claus", "Elon Musk", "SM64 Mario", "Psychologist", "Saul Goodman", "Oblivion Guard", "Sans Undertale", "Ralsei Deltarune", "Engineer TF2", "Jerma985", "Waluigi", "Joe Biden", "Jimmy 'MrBeast' Donaldson", "Minecraft Steve", "Walter White", "a chair", "Ronald Reagan", "Ronald McDonald", "DougDoug", "Shadow the Hedgehog", "Chimpanzee", "Dr. Eggman", "Mr. Krabs", "Man In The Corner", "Scout TF2", "Donkey Kong", "Hornet", "Jesus Christ", "Neil Cicierega", "Vacuum Salesman Michael Jackson", "Noelle Deltarune", "Doctor Eggman", "You", "ChatGPT"]
modeList = ["Standard", "Defensive", "Offensive", "Chaos"]

def invade():
 invasionPrompt = 'Invade ' + adjacentCountriesList[random.randint(0,len(adjacentCountriesList)-1)] + ' with ' + invasionModifierList[random.randint(0,len(invasionModifierList)-1)] + ' The soldiers will be ' + soldierModifierList[random.randint(0,len(soldierModifierList)-1)]
 print(invasionPrompt)
 engine.say(invasionPrompt)
 engine.runAndWait()


def ally():
 alliancePrompt = 'I\'ll Ally with ' + adjacentCountriesList[random.randint(0,len(adjacentCountriesList)-1)] + ' ' + allianceModifierList[random.randint(0,len(allianceModifierList)-1)] + ' The diplomat will be ' + soldierModifierList[random.randint(0,len(soldierModifierList)-1)]
 print(alliancePrompt)
 engine.say(alliancePrompt)
 engine.runAndWait()


def research():
 if random.randint(1,2) == 1:
  researchPrompt = 'Research ' + '"' + r.get_random_word() + ' ' + r.get_random_word() + '"'
  print(researchPrompt)
  engine.say(researchPrompt)
  engine.runAndWait()
 else:
  if random.randint(1,3) == 1:
   researchPrompt = 'Research ' + '"' + r.get_random_word() + ' ' + r.get_random_word() + ' ' + r.get_random_word() + '' + r.get_random_word() + '"'
  else:
   print('Research something from https://en.wikipedia.org/wiki/Special:Random.')
   engine.say('Research something from https://en.wikipedia.org/wiki/Special:Random.')
   engine.runAndWait()


def advice():
 advicePrompt = 'I\'ll ask ' + characterList[random.randint(0,len(characterList)-1)] + ' for advice.'
 print(advicePrompt)
 engine.say(advicePrompt)
 engine.runAndWait()


def anarchy():
 anarchyIntroList = ['Limiting yourself is for cowards. I\'ll do two things at once.', 'Why do one when two better?', 'I\'ll trade cohesive narrative for progress and do two things in one turn.','I\'ll do two things. First:']
 anarchyIntro = anarchyIntroList[random.randint(0,len(anarchyIntroList)-1)]
 print(anarchyIntro)
 engine.say(anarchyIntro)
 engine.runAndWait()
 setAction()
 print('Additionally,')
 engine.say('Additionally,')
 engine.runAndWait()
 setAction()


def terraform():
 terraformPrompt = 'I think I\'ll ' + europeTerraformList[random.randint(0,len(europeTerraformList)-1)]
 print(terraformPrompt)
 engine.say(terraformPrompt)
 engine.runAndWait()


def build():
 buildPrompt = 'I think I\'ll build ' + buildingList[random.randint(0,len(buildingList)-1)] + ' in ' + ownedCountriesList[random.randint(0,len(ownedCountriesList)-1)] + '.'
 print(buildPrompt)
 engine.say(buildPrompt)
 engine.runAndWait()


def sabotage():
 sabotagePrompt = 'I\'ll try to sabotage one of ' + playerList[random.randint(0,len(playerList)-1)] + '\'s resources.'
 print(sabotagePrompt)
 engine.say(sabotagePrompt)
 engine.runAndWait()


def mode():
 currentMode = modeList[random.randint(0,3)]
 modePrompt = 'I\'ll change my mode to ' + currentMode + ', then:'
 print(modePrompt)
 engine.say(modePrompt)
 engine.runAndWait()
 setAction()


currentMode = 'standard' # modes are essentially the weights for each action. change the default mode when the randomizer says to.

standardActionList = [invade,invade,invade,ally,ally,ally,sabotage,sabotage,research,research,build,build,terraform,terraform,mode,mode,advice,anarchy] # standard
passiveActionList = [build,build,build,terraform,terraform,terraform,research,research,research,advice,advice,advice,mode,mode,invade,ally,sabotage,anarchy] # passive
offensiveActionList = [invade,invade,invade,invade,ally,ally,ally,ally,sabotage,sabotage,advice,advice,mode,mode,research,build,terraform,anarchy] # offensive
chaosActionList = [anarchy,anarchy,anarchy,mode,mode,mode,research,research,sabotage,sabotage,build,build,terraform,terraform,advice,advice,invade,ally] # chaos

def setAction():
 if currentMode == 'standard':
  action = standardActionList[random.randint(0,17)]
  action()
 else:
  if currentMode == 'passive':
   action = passiveActionList[random.randint(0,17)]
   action()
  else:
   if currentMode == 'offensive':
    action = offensiveActionList[random.randint(0,17)]
    action()
   else:
    action = chaosActionList[random.randint(0,17)]
    action()

setAction()
