import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.title('Contact')
mail_b= f'<p>Your feed back is very important for us. Write about your user experience. Give us kudos! Ask questions. Inform us\
about the errors you encountered. Tell about new ideas. You can contact me through <u>ozgur.dugmeci@gmail.com</u>  </p>'
 
#info_link= f'<a target="_blank" rel="noopener noreferrer" href="https://ozgur-dugmeci.medium.com/easy-inventory-planner-c1e5fc4aa0e">Click here to leave a comment.</a>'
st.markdown(mail_b,unsafe_allow_html=True)
#st.markdown(info_link,unsafe_allow_html=True)

df = pd.DataFrame({
    "Column1": [1, 2, 3],
    "Column2": ["A", "B", "C"]
})

log = pd.read_csv("Data/deneme.csv")
log.columns=['deneme']
log['haydi']=5
log['haydi4']=5

st.dataframe(log)

log.to_csv("Data/deneme2.csv")
#log.to_csv("deneme.csv")

