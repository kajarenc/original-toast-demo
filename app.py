import streamlit as st

st.set_page_config(
    page_icon=":flag:",
)


st.subheader("Demo app for original toast behaviour")

with st.chat_message("ai"):
    st.write("Hello from AI default👋")

with st.chat_message("user"):
    st.write("Hello from User default👋")

with st.chat_message("ai", avatar="🛑"):
    st.write("Hello from AI 👋")

with st.chat_message("user", avatar="💚"):
    st.write("Hello from USER 👋")

st.info("This is a purely informational message", icon="ℹ️")


my_button = st.button("Show toast with custom icon")
if my_button:
    st.toast("Your edited image was saved!" * 10, icon="😍")
    st.toast("Your edited image was saved!" * 10, icon="🦄")
