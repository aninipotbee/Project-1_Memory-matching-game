# **Group 8_Memory Matching Game CS2C**

## **Test Table 1.1**

| **Test Case** | **Test Procedure** | **Expected Result** | **Actual Result** | **Status** |
|---|---|---|---|---|
| TC-01 | Start the game without entering a name | Warning message should appear | Warning message appeared | Passed |
| TC-02 | Enter a name and start the game | Game should start normally | Game started | Passed |
| TC-03 | Select one card | Card should be revealed | Card was revealed | Passed |
| TC-04 | Select two matching cards | Score should increase and cards should remain visible | Score increased and cards remained visible | Passed |
| TC-05 | Select two different cards | Cards should be hidden again | Cards were hidden | Passed |
| TC-06 | Click the same card twice | Second selection should not be accepted | Second selection was ignored | Passed |
| TC-07 | Complete a round | Next round should load | Next round loaded | Passed |
| TC-08 | Run out of turns | Game Over message should appear | Game Over appeared | Passed |
| TC-09 | Complete all rounds | Winning message should appear | Winning message appeared | Passed |
| TC-10 | Click Restart Game | Game should reset | Game reset correctly | Passed |

# **Bug 1.2**

### **Bug 1: Empty Player Name**

**Problem:** The game could be started without entering a name.

**Fix:** Added validation to check if the name field is empty.

**Status:** Fixed

### **Bug 2: Same Card Selected Twice**

**Problem:** The same card could be selected as both cards.

**Fix:** Added a condition to ignore the second click if it is the same card.

**Status:** Fixed

### **Bug 3: Matched Cards Could Be Selected Again**

**Problem:** Already matched cards could still be clicked.

**Fix:** Used the `matched` list and disabled the buttons after a match.

**Status:** Fixed
