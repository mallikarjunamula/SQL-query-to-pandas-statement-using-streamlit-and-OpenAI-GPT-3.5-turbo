import streamlit as st
from openai import OpenAI

st.subheader("SQL Query to Pandas Statement:",divider='rainbow')
client = OpenAI(api_key="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")
def Sql2db(query, client):
  response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
      {"role": "system", "content": "You are an expert in SQL and Pandas, Who converts sql query to pandas statements"},
      {"role": "user", "content": query}
    ]
  )
  return response.choices[0].message.content

input_text  = st.text_area("Write SQL Query here!")
button = st.button("Generate Response")
if button and input_text:
    with st.spinner("Generating Pandas Statement!!"):
        resp = Sql2db(input_text, client)
    st.write(resp)
