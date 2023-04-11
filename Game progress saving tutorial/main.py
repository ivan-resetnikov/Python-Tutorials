import json

playerHP = 100
playerName = 'LowRezCat'
playerINV = ['potato', 'cat', 'subscribe button']



def saveProgress():
	file = open('save.json', 'w')

	contentToSave = {
			'hp': playerHP,
			'name': playerName,
			'inv': playerINV
		}

	json.dump(contentToSave, file)

	file.close()


def loadProgress():
	global playerHP, playerName, playerINV

	file = open('save.json', 'r')

	fileContent = json.load(file)

	playerHP = fileContent['hp']
	playerName = fileContent['name']
	playerINV = fileContent['inv']

	file.close()



saveProgress()

loadProgress()