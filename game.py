import streamlit as st
import random

class RockPaperScissorsGame:
    def __init__(self):
        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_choice = None
        self.computer_choice = None
        self.result = ""

    def run(self):
        st.markdown("<h1 style='text-align: center; color: pink;'>Rock, Paper, Scissors Game</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: yellow;'>Choose Rock, Paper, or Scissors</h3>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Rock"):
                self.user_choice = "Rock"
                self.play_game()
        with col2:
            if st.button("Paper"):
                self.user_choice = "Paper"
                self.play_game()
        with col3:
            if st.button("Scissors"):
                self.user_choice = "Scissors"
                self.play_game()



    def play_game(self):
        self.computer_choice = random.choice(self.choices)
        st.markdown(f"<h3 style='text-align: center;'>Computer chose: {self.computer_choice}</h3>", unsafe_allow_html=True)

        if self.user_choice == self.computer_choice:
            self.result = "<span style='color: orange;'>It's a tie!</span>"
            st.image("c:/Users/Waleed Abbasi/OneDrive/Desktop/python/images/tie.gif", use_container_width=True, width=500)
        elif (self.user_choice == "Rock" and self.computer_choice == "Scissors") or \
             (self.user_choice == "Paper" and self.computer_choice == "Rock") or \
             (self.user_choice == "Scissors" and self.computer_choice == "Paper"):
            self.result = "<span style='color: green;'>You win!</span>"
            st.image("c:/Users/Waleed Abbasi/OneDrive/Desktop/python/images/you_win.gif", use_container_width=True, width=500)
            st.balloons()
        else:
            self.result = "<span style='color: red;'>You lose!</span>"
            st.image("c:/Users/Waleed Abbasi/OneDrive/Desktop/python/images/you_lose.gif", use_container_width=True, width=500)

        st.markdown(f"<h2 style='text-align: center;'>{self.result}</h2>", unsafe_allow_html=True)

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.run()