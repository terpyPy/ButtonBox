# Button box Game: by, Hunter Hannula & Cameron Kerley
•	A game played on a NeoTrellis Feather LED game board built with CircuitPython and model from a project by The Ruiz Brothers:
1.	Model from a project by The Ruiz Brothers: https://learn.adafruit.com/neotrellis-box-game
2.	NeoTrellis Feather LED game board: https://github.com/adafruit/Adafruit_Learning_System_Guides
3.	CircuitPython: https://learn.adafruit.com/welcome-to-circuitpython

•	Game Logic:

1.	generate a pattern at the start of the game

2.	if the pattern generated at the start of the game matches the a pressed button light it up green

3.	if wrong show visual flash or color that input is wrong.

4.	After a set amount guesses reset and gen a new pattern.

•	Sudo code for main project

-Programflow:

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
		checkButtonPress(pressedButton)   //check if board update event is correct
		timedFlash(time, color)
		getNextRightAnswer
		loseGame    //all squares blink red three times
		winGame   //all squares blink green three times
		drawBoard

# Demo of game start from pure software java version:
https://user-images.githubusercontent.com/66324329/118368067-3af40500-b56f-11eb-829f-6de83c493353.mp4


