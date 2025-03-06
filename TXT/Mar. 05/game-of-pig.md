# Game of Pig Pseudocode

**1. Start the Game**

* Set the player's total score to 0.
* Set the player's round score to 0.
* Display: "Let's play Pig!"

**2. Player's Turn**

* **Repeat until the player chooses "Bank" or rolls a 1:**
    * Ask: "Roll or Bank?"
    * **If the player chooses "Roll":**
        * Roll a 6-sided die (random number between 1 and 6).
        * **If the die roll is 2, 3, 4, 5, or 6:**
            * Add the die roll to the player's round score.
            * Display: "Round score: [round score]"
            * Display: "Total score: [total score]"
        * **If the die roll is 1:**
            * Set the player's round score to 0.
            * Display: "You rolled a 1! Round score reset to 0."
            * End the player's turn.
    * **If the player chooses "Bank":**
        * Add the player's round score to their total score.
        * Set the player's round score to 0.
        * Display: "Total score: [total score]"
        * End the player's turn.

**3. Check for Winner**

* **If the player's total score is 100 or more:**
    * Display: "You win!"

**4. End the Game**

* Display: "Game Over!"

**Example of a Turn (in pseudocode)**

* Round Score: 0, Total Score: 0
* Player says "Roll"
* Die Roll: 5
* Round Score: 5
* Player says "Roll"
* Die Roll: 3
* Round Score: 8
* Player says "Bank"
* Total Score: 8, Round Score: 0.