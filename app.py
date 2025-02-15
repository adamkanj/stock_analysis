import streamlit as st


def main():
    """Main App start for home page"""
    st.set_page_config(page_title="Streamlit App", page_icon=":shark:", layout="wide")

    st.title("Stock Analysis", anchor=False)


if __name__ == "__main__":
    main()
