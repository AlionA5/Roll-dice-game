import random
import streamlit as st
import pandas as pd
import os
import base64 
import numpy as np
import altair as alt
import streamlit.components.v1 as com
import streamlit as st
import base64

import streamlit as st
import base64

st.markdown("""
    <style>
    body {
        background-color: #white;
    }
    </style>
""", unsafe_allow_html=True)

file_ = open(os.path.join(os.getcwd(),"dice.gif"), "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)

class Dice:
    def roll(self):
        return (random.randint(1,6), random.randint(1,6))
roll_dice = Dice()
print(roll_dice.roll())

dice_images = {
    i: os.path.join(os.getcwd(), f"Dice-{i}-b.png") for i in range(1, 7)
}

st.header("Roll the Dice")

if st.button("Roll Dice"):
    dice1, dice2 = Dice().roll()

    st.write(f"You rolled {dice1} and {dice2}. Total: {dice1 + dice2}")

    col1, col2 = st.columns(2)
    with col1:
        st.image(dice_images[dice1], width=200)
    with col2:
        st.image(dice_images[dice2], width=200)