import streamlit as st
import random

class RockPaperScissorsGame:
    def __init__(self):
        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_choice = None
        self.computer_choice = None
        self.result = ""
        if 'coins' not in st.session_state:
            st.session_state.coins = 0

    def run(self):
        st.markdown("<h1 style='text-align: center; color: #FF69B4;'>Rock, Paper, Scissors Game</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #FFD700;'>Choose Rock, Paper, or Scissors</h3>", unsafe_allow_html=True)

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

        # Display the total coins in the sidebar
        st.sidebar.markdown(f"<h2 style='color: #1E90FF;'>Subtotal Coins: {st.session_state.coins}</h2>", unsafe_allow_html=True)

    def play_game(self):
        self.computer_choice = random.choice(self.choices)
        st.markdown(f"<h3 style='text-align: center;'>Computer chose: {self.computer_choice}</h3>", unsafe_allow_html=True)

        if self.user_choice == self.computer_choice:
            self.result = "<span style='color: orange;'>It's a tie!</span>"
            st.image("https://www.pinterest.com/pin/295408056837557693", caption="It's a tie!", use_container_width=True)
            st.session_state.coins += 1
        elif (self.user_choice == "Rock" and self.computer_choice == "Scissors") or \
             (self.user_choice == "Paper" and self.computer_choice == "Rock") or \
             (self.user_choice == "Scissors" and self.computer_choice == "Paper"):
            self.result = "<span style='color: green;'>You win!</span>"
            st.image("https://via.placeholder.com/150/008000/FFFFFF?text=You+win!", caption="You win!", use_container_width=True)
            st.balloons()
            st.session_state.coins += 2
        else:
            self.result = "<span style='color: red;'>You lose!</span>"
            st.image("https://via.placeholder.com/150/FF0000/FFFFFF?text=You+lose!", caption="You lose!", use_container_width=True)
            st.session_state.coins -= 2

        # Reflect the updated coin total in the sidebar
        st.sidebar.markdown(f"<h2 style='color: #1E90FF;'>Subtotal Coins: {st.session_state.coins}</h2>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align: center;'>{self.result}</h2>", unsafe_allow_html=True)

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.run()
