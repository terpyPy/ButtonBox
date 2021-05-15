# Button box Game: by, Hunter Hannula & Cameron Kerley
A game played on a NeoTrellis Feather LED game board built with CircuitPython and model from a project by The Ruiz Brothers:
	Model from a project by The Ruiz Brothers - https://learn.adafruit.com/neotrellis-box-game
	NeoTrellis Feather LED game board - https://github.com/adafruit/Adafruit_Learning_System_Guides
	CircuitPython - https://learn.adafruit.com/welcome-to-circuitpython
- game logic:
	1. genrate a pattern at the start of the game
	2. if the pattern genrated at the start of the game matches the a pressed button light it up green
	3. if wrong show visual flash or color that input is wrong.
	4. After a set amount guesses reset and gen a new pattern.
# sudo code for main project
	Programflow:

		Load pattern
		Display pattern start
		Open user input
		User button press -> 
		   If wrong increase wrongAnswers by one and flash button red
		   If wrongAnswers is too high show lose game visual sequence and reset game

		   If right flash button green
		   If not last answer then advance nextRightAnswer
		      Else show win visual sequence and load new pattern
		methods:
		loadPattern
		checkButtonPress(pressedButton)   //check if pressed button from board update event is correct
		timedFlash(time, color)
		getNextRightAnswer
		loseGame    //all squares blink red three times
		winGame   //all squares blink green three times
		drawBoard

