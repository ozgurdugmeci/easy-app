import streamlit as st
import streamlit.components.v1 as components



st.subheader('1- Predictability Analysis')
 

htp6='https://raw.githubusercontent.com/ozgurdugmeci/easy-app/main/media/predict_resim2.jpg'
#image6 = Image.open(htp6)
st.image(htp6, caption= 'Predictability Analysis', width=800)

predicty= f'<p>When analyses part opens, this is the first analysis that appears on the screen. You can download this report in csv file \
 by clicking download link in "Analyses" part. Application assigns categories for each product. And for each category\
 model uses different calculation method to predict sales speed. This is an unsupervised machine learning model. </br>\
 <b>Predictable Sales : </b> Products in this category have consistent sales speed in every 20 days of 80 days. Predictability Analysis shows the quality of inventory \
 management. The higher percentage of the "Predictable Sales" ratio indicates the good quality of the inventory management. </br> <b>New Products :</b> \
 Application also detects "New Products". Since these products are in sales for less than 41 days, taking this information into consideration, model calculates  \
 sales speed for each product under this category. </br> <b>Unpredictable Sales :</b> Marketing activities, product availablity, stock-out situations, customer preference have effect on sales.\
 Because of these reasons some products have inconsistent sales trends in between sales ranges. Model obtains these kind of products and labels them as\
 "Unpredictable Sales".  Yet still model estimates a sales speed for the products in this group. </br> <b>Decreasing Sales :</b> Model detects sales decrease. And it groups \
 these products under "Decreasing Sales" category. It can be an early warning system to check the inventory quantities and to take the necessary actions. </p>'
 
st.markdown(predicty,unsafe_allow_html=True)

st.subheader('2- Sales Prediction & Calculate Stock-Cover Days') 



htp7='https://raw.githubusercontent.com/ozgurdugmeci/easy-app/main/media/planner_resim.jpg'

#htp7='gs://imajo/media/planner_resim.jpg'

#image7 = Image.open(htp7)


st.image(htp7, caption= 'Inventory Planner', width=800)
planner= f'<p>This analysis gives the core insights to plan inventory. You can check the <b>"Stock_Cover" </b> values.  In other words, it shows the number of days until a product will be out of stock. \
Thus necessary actions can be taken before a product quantity comes to a critical low level. <b>"Predicted_Sales_Speed"</b> is the estimated 30-day \
 sale values.  Analysing these values with the category information can help you in taking decisions.</p>'

st.markdown(planner,unsafe_allow_html=True)
st.subheader('3- Zero Sales') 
'The products have no sales in the last 80 days are listed here. If there are no such products, this analysis does not appear on the screen.' 

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
    
