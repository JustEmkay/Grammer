import streamlit as st
import spacy

nlp = spacy.load("en_core_web_sm")

def main():
    st.write("test")

if __name__ == '__main__':
    main()