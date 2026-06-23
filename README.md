# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
Bugs found:
1. Reversed higher/go lower hint after guess (opposite to the actual)
2. New Game button does not reset the game after win or loss
3. Allows one attempt less than it supposed to (starts with 1 attempt taken)
4. Game uses incorrect ranges - all difficulty levels use 1..100 instead of ranges outlined in settings
- [ ] Explain what fixes you applied.
I've fixed the following issues:

Bug 1: Reversed higher/lower hints. A wrong guess pointed the player the wrong way - too-high guesses said "go higher" and too-low said "go lower." In check_guess, the right outcome label was paired with the wrong message. We flipped it so "Too High" says go LOWER and "Too Low" says go HIGHER, moved the logic into logic_utils.py, and added unit tests in tests/test_game_logic.py.

Bug 2: Game ignored the difficulty's range. Every difficulty effectively used 1–100. The guess prompt and New Game secret were hardcoded to 1–100, and the secret was only picked once so switching levels left an out-of-range number. Both now use the active (low, high) range, and the secret regenerates (resetting the game) when difficulty changes, tracked with a secret_difficulty key. We also moved get_range_for_difficulty into logic_utils.py and added tests for Easy, Normal, and Hard.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects the game difficulty
2. Game displays the correct number range and generates a secret (e.g., 50)
3. User enters a guess of 75 -> game gives a hint "Go Lower"
4. User enters a guess of 25 -> game gives a hint "Go Higher"
5. Game ends after the correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
