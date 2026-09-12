# **Group 8_Memory Matching Game CS2C** 

**Test table 1.1** 

# **Test Test Procedure Case** 

- Start the game without 

- TC-01 entering a name 

- Enter a name and start the 

- TC-02 game 

- TC-03 Select one card 

|TC-04|Select two matching cards|
|---|---|
|TC-05|Select two different cards|
|TC-06|Click the same card twice|
|TC-07|Complete a round|
|TC-08|Run out of turns|
|TC-09|Complete all rounds|
|TC-10|Click Restart Game|



|**Expected Result**|**Actual Result**|**Status**|
|---|---|---|
|Warning message should appear|Warning message appeared|Passed|
|Game should start normally|Game started|Passed|
|Card should be revealed|Card was revealed|Passed|
|Score should increase and cards should<br>remain visible|Score increased and cards<br>remained visible|Passed|
|Cards should be hidden again|Cards were hidden|Passed|
|Second selection should not be accepted|Second selection was ignored|Passed|
|Next round should load|Next round loaded|Passed|
|Game Over message should appear|Game Over appeared|Passed|
|Winning message should appear|Winning message appeared|Passed|
|Game should reset|Game reset correctly|Passed|



# **Bug 1.2** 

Bug 1: Empty player name 

**Problem:** The game could be started without entering a name. **Fix:** Added validation to check if the name field is empty. **Status:** Fixed 

Bug 2: Same card selected twice 

**Problem:** The same card could be selected as both cards. **Fix:** Added a condition to ignore the second click if it is the same card. **Status:** Fixed 

Bug 3: Matched cards could be selected again 

**Problem:** Already matched cards could still be clicked. **Fix:** Used the `matched` list and disabled the buttons after a match. **Status:** Fixed 

