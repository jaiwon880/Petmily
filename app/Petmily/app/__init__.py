import streamlit as st
import widget

def app():
    widget.sidebar()
    widget.radar_chart()
    col1, col2 = st.columns(2)
    with col1 :
        widget.hospital_chart()
        widget.beauty_chart()
        widget.tf_chart()
    with col2 :
        widget.hotel_chart()
        widget.park_chart()
        widget.syn_chart()

if __name__ == '__main__':
    st.set_page_config(
        page_icon=":dog:",
        page_title="펫밀리",
        layout="wide")
    app()