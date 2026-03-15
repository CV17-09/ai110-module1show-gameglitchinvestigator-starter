# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- When I first ran the game, it looked playable, but I noticed the game logic was not working correctly. One bug I saw was with the attempt counter: it said I had 7 attempts, but after I missed once, the number did not go down right away. It only dropped after another miss, which made the attempt tracking feel delayed and inaccurate. Another bug was with the hints, because the game told me “higher” even when I had already entered the maximum number, 100, which did not make sense and showed that the hint logic was broken.

---

## 2. How did you use AI as a teammate?

- I used Claude and VS Code Copilot while working on this project. One example of a helpful suggestion was when AI explained why the hint logic might be wrong and suggested checking how the guess was being compared to the secret number. After reading the explanation, I looked at the code and tested different guesses in the game to confirm that the hint messages were not matching the input correctly. One misleading suggestion from AI was that the problem might be caused by the input field itself rather than the game logic. When I tested the game again and looked at the code, I realized the issue was actually coming from the comparison logic and not the input component.

---

## 3. Debugging and testing your fixes

- To decide whether a bug was fixed, I tested the game multiple times after making changes to see if the behavior improved. For example, I manually played the game and checked if the attempt counter decreased correctly after every wrong guess. I also ran the provided pytest tests to see whether the guessing logic returned the correct results. One test checked that if the secret number was 50 and the guess was also 50, the result should be “Win.” AI helped me understand what the tests were checking and how they related to the functions in the code.

---

## 4. What did you learn about Streamlit and state?

- The secret number kept changing because Streamlit reruns the script every time the user interacts with the app, such as when entering a guess. Each rerun created a new random secret number instead of keeping the same one. I would explain Streamlit reruns to a friend by saying that the app restarts the script every time something changes on the page, so variables reset unless you store them somewhere persistent. The solution was to store the secret number in Streamlit session state, which keeps the value saved between reruns. After that change, the secret number stayed the same throughout the game.

---

## 5. Looking ahead: your developer habits

- One habit I want to keep using is testing code after each change instead of waiting until the end, because it helped me quickly see if a bug was fixed. Next time I work with AI on a coding task, I would double-check its suggestions more carefully before assuming they are correct. This project showed me that AI can be helpful for explanations and ideas, but it can also make mistakes or misunderstand the problem. It changed the way I think about AI-generated code because I now see it as a tool that needs human verification rather than something that should be trusted automatically
