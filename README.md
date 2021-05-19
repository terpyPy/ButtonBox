
# Button box Game: by, Hunter Hannula & Cameron Kerley: 
1. A game played on a NeoTrellis Feather LED game board built with CircuitPython and model from a project by The Ruiz Brothers:

	•Model from a project by The Ruiz Brothers: https://learn.adafruit.com/neotrellis-box-game
	
	•NeoTrellis Feather LED game board: https://github.com/adafruit/Adafruit_Learning_System_Guides
	
	•CircuitPython: https://learn.adafruit.com/welcome-to-circuitpython
	
- Test package Abstraction chart:
![DraftPackegeStructer](https://user-images.githubusercontent.com/66324329/118437126-0b98e180-b6b0-11eb-86d3-393a04a4331a.png)

- gamestate visual Demo digram:
![boardDrawing](https://user-images.githubusercontent.com/66324329/118375883-98e61400-b592-11eb-891f-f6c603d98c80.png)
	
2. Game Logic:

	•generate a pattern at the start of the game

	•if the pattern generated at the start of the game matches the a pressed button light it up green

	•if wrong show visual flash or color that input is wrong.

	•After a set amount guesses reset and gen a new pattern.
	


3. Sudo code for main project

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



