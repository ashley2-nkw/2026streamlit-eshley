# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:32:56 2026

@author: BBarsch
"""

import streamlit as st

st.write("ashley's first streamlit ")

st.write("Hello2")

st.title("Title heading")

st.write("Hello, Streamlit!")

st.header("Number selection")

number = st.slider("Pick a number", 1, 100)
st.write(f"You picked: {number}")
st.markdown("some text you could write ")