import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Demand Planning")
st.title('Demand Planning Application Guide')
   
htp0='https://raw.githubusercontent.com/ozgurdugmeci/easy-app/main/media/model4.jpg'
#image0 = Image.open(htp6)
st.image(htp0, caption= 'Model', width=600)


biry= f'<p>It is an easy-to-use and smart way to manage your inventory. <br> \
 This app uses an unsupervised machine learning model to analyze your sales and stock data, calculating the sales speed for each product. <br> This helps you estimate \
 how long your stock will last. With application, you can easily keep track of your inventory levels, predict future needs, and avoid running out or having \
 too much stock. The app is simple and intuitive design makes it easy to use, helping you make better decisions and keep your business running smoothly.  <p>'

st.markdown(biry,unsafe_allow_html=True)
   


urly= f'<a target="_blank" rel="noopener noreferrer" href="https://www.youtube.com/watch?v=kzYUHItdyOQ">Click to watch csv upload.</a>'
#st.markdown(urly,unsafe_allow_html=True)
urly_download_new= f'<a target="_blank" rel="noopener noreferrer" href="https://www.youtube.com/watch?v=wahIMj-G3sE">Click to watch how to upload excel file.</a>'
st.markdown(urly_download_new,unsafe_allow_html=True)



st.subheader('Excel Upload & Analyses')
metin_excel= f" <p> - Prepare excel file with the correct order of the columns.<br> - Upload excel file or simply click <b>Upload Test Data</b> button. </p>"
st.markdown(metin_excel,unsafe_allow_html=True)



  
takip= """ 
<!-- Default Statcounter code for easy2
https://share.streamlit.io/ozgurdugmeci/easy-app/main/app.py
-->
<script type="text/javascript">
var sc_project=12528966; 
var sc_invisible=0; 
var sc_security="5fb071da"; 
var scJsHost = "https://";
document.write("<sc"+"ript type='text/javascript' src='" +
scJsHost+
"statcounter.com/counter/counter.js'></"+"script>");
</script>
<noscript><div class="statcounter"><a title="Web Analytics"
href="https://statcounter.com/" target="_blank"><img
class="statcounter"
src="https://c.statcounter.com/12528966/0/5fb071da/0/"
alt="Web Analytics"></a></div></noscript>
<!-- End of Statcounter Code -->

"""
#st.markdown(takip, unsafe_allow_html=True)  
components.html(takip,width=200, height=200)
    
    
    
