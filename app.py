import streamlit as st
import streamlit.components.v1 as components
import logging
import openpyxl
import pandas as pd 
import numpy as np
from random import randint
import base64
from io import BytesIO
from datetime import datetime
from PIL import Image

a = 0
a2 = 0
a3 = 0
a4 = 0 
a5 = 0
kilit1 = 0
kilit2 = 0
kilit3 = 0
kilit4 = 0
kilit5 = 0
takip2='xx'

st.sidebar.title('Easy Inventory Planner')
st.sidebar.header('Content')
yan_sayfa_secenek = st.sidebar.radio(
    '',
    ('Application Guide', 'About Analyses', 'Getting CSV Files Ready','Direct Excel Upload & Analyses', 'Uploading CSV Files & Analyses','Contact')
)

if yan_sayfa_secenek == 'Uploading Files & Analyses' :
  
    
    
 st.title("1- UPLOADING FILES")
 st.header('A- Upload Inventory File')
   
 
 urly_upload= f'<a target="_blank" rel="noopener noreferrer" href="https://www.youtube.com/watch?v=kzYUHItdyOQ">Click to watch partial upload.</a>'
 st.markdown(urly_upload,unsafe_allow_html=True)
 st.info('Characters on upload files other than Unicode Standard can cause error. ')   


 st.set_option('deprecation.showfileUploaderEncoding', False)
 uploaded_file = st.file_uploader("Select Inventory File", type=['csv'])
 
 if uploaded_file :
  
  df_inv = pd.read_csv(uploaded_file, delimiter= ';')
  df_inv=df_inv.fillna(0)
  
  if len(df_inv.columns) != 2:
   st.warning('There must be only two columns. Please upload data again.') 
  
  df_inv.columns=['Product_Number','Inventory_Quantity']
  df_inv['Inventory_Quantity']=df_inv['Inventory_Quantity'].replace(regex=[','], value='.')
  try:
   df_inv['Inventory_Quantity']=df_inv['Inventory_Quantity'].astype(float)
   
   st.dataframe(df_inv.head(3))
   uploaded= str(len(df_inv)) + " rows uploaded."
   uploaded
   
   #st.markdown(sd, unsafe_allow_html=True) 
   a=df_inv['Inventory_Quantity'].sum()
   'Total Inventory_Quantity'
   a
  
  
   if a == 0 :
    st.warning('Uploaded file is empty. Upload file again.')
    
  except:
   st.warning('Check the data you uploaded. There might be string value on Column B.')  
 else :
  warning1= f'<p style="color:red;">Inventory file has not been uploaded.</p>'
  st.markdown(warning1, unsafe_allow_html=True)  

 
 st.header('B- Upload Sales20 File')
 
 st.set_option('deprecation.showfileUploaderEncoding', False)
 uploaded_file2 = st.file_uploader("Select Sales20 File", type=['csv'])
 
 if uploaded_file2 :
  
  df_sales20 = pd.read_csv(uploaded_file2, delimiter= ';')
  df_sales20=df_sales20.fillna(0)
  if len(df_sales20.columns) != 2:
   st.warning('There must be only two columns. Please upload data again.') 
  
  df_sales20.columns=['Product_Number','Sales20']
  
  
  df_sales20['Sales20']=df_sales20['Sales20'].replace(regex=[','], value='.')
  try:
   df_sales20['Sales20']=df_sales20['Sales20'].astype(float)
   
   st.dataframe(df_sales20.head(3))
   uploaded= str(len(df_sales20)) + " rows uploaded."
   uploaded
   
   #st.markdown(sd, unsafe_allow_html=True) 
   a2=df_sales20['Sales20'].sum()
   'Total Sales20'
   a2
  
  
   if a2 == 0 :
    st.warning('Uploaded file is empty. Upload file again.')
   
  except:
    st.warning('Check the data you uploaded. There might be string value on Column B.')  
  
 else :
  warning2= f'<p style="color:red;">Sales20 file has not been uploaded.</p>'
  st.markdown(warning2, unsafe_allow_html=True)    

 
 st.header('C- Upload Sales40 File')
 
 st.set_option('deprecation.showfileUploaderEncoding', False)
 uploaded_file3 = st.file_uploader("Select Sales40 File", type=['csv'])
 
 if uploaded_file3 :
  
  df_sales40 = pd.read_csv(uploaded_file3, delimiter= ';')
  df_sales40=df_sales40.fillna(0)
  if len(df_sales40.columns) != 2:
   st.warning('There must be only two columns. Please upload data again.') 
  
  df_sales40.columns=['Product_Number','Sales40']
  df_sales40['Sales40']=df_sales40['Sales40'].replace(regex=[','], value='.')
  try:
   df_sales40['Sales40']=df_sales40['Sales40'].astype(float)
   
   st.dataframe(df_sales40.head(3))
   uploaded= str(len(df_sales40)) + " rows uploaded."
   uploaded
   
   #st.markdown(sd, unsafe_allow_html=True) 
   a3=df_sales40['Sales40'].sum()
   'Total Sales40'
   a3
  
  
   if a3 == 0 :
    st.warning('Uploaded file is empty. Upload file again.')
   
  except:
    st.warning('Check the data you uploaded. There might be string value on Column B.')  
  
 else :
  warning3= f'<p style="color:red;">Sales40 file has not been uploaded.</p>'
  st.markdown(warning3, unsafe_allow_html=True)

 st.header('D- Upload Sales60 File')
 
 st.set_option('deprecation.showfileUploaderEncoding', False)
 uploaded_file4 = st.file_uploader("Select Sales60 File", type=['csv'])
 
 if uploaded_file4 :
  
  df_sales60 = pd.read_csv(uploaded_file4, delimiter= ';')
  df_sales60=df_sales60.fillna(0)
  if len(df_sales60.columns) != 2:
   st.warning('There must be only two columns. Please upload data again.') 
  
  df_sales60.columns=['Product_Number','Sales60']
  df_sales60['Sales60']=df_sales60['Sales60'].replace(regex=[','], value='.')
  try:
   df_sales60['Sales60']=df_sales60['Sales60'].astype(float)
   
   st.dataframe(df_sales60.head(3))
   uploaded= str(len(df_sales60)) + " rows uploaded."
   uploaded
   
   #st.markdown(sd, unsafe_allow_html=True) 
   a4=df_sales60['Sales60'].sum()
   'Total Sales60'
   a4
  
  
   if a4 == 0 :
    st.warning('Uploaded file is empty. Upload file again.')
   
  except:
    st.warning('Check the data you uploaded. There might be string value on Column B.')  
 else :
  warning4= f'<p style="color:red;">Sales60 file has not been uploaded.</p>'
  st.markdown(warning4, unsafe_allow_html=True)
 
 
 st.header('E- Upload Sales80 File')
 
 st.set_option('deprecation.showfileUploaderEncoding', False)
 uploaded_file5 = st.file_uploader("Select Sales80 File", type=['csv'])
 
 if uploaded_file5 :
          
  
  df_sales80 = pd.read_csv(uploaded_file5, delimiter= ';')
  df_sales80=df_sales80.fillna(0)
  if len(df_sales80.columns) != 2:
   st.warning('There must be only two columns. Please upload data again.') 
  
  df_sales80.columns=['Product_Number','Sales80']
  df_sales80['Sales80']=df_sales80['Sales80'].replace(regex=[','], value='.')
  try:
   df_sales80['Sales80']=df_sales80['Sales80'].astype(float)
   
   st.dataframe(df_sales80.head(3))
   uploaded= str(len(df_sales80)) + " rows uploaded."
   uploaded
   
   #st.markdown(sd, unsafe_allow_html=True) 
   a5=df_sales80['Sales80'].sum()
   'Total Sales80'
   a5
  
  
   if a5 == 0 :
    st.warning('Uploaded file is empty. Upload file again.')
   
  except:
   st.warning('Check the data you uploaded. There might be string value on Column B.')  

 else :
  warning5= f'<p style="color:red;">Sales80 file has not been uploaded.</p>'
  st.markdown(warning5, unsafe_allow_html=True)
 if (a != 0 and a2 !=0 and  a3!=0  and a4 != 0  and a5!=0) :
  st.title('2- ANALYSES')
  
  df_inv = pd.pivot_table(df_inv, values=['Inventory_Quantity'], index=['Product_Number'],  aggfunc=np.sum)
  df_inv = df_inv.reset_index()                #index to columns
  
  df_sales20 = pd.pivot_table(df_sales20, values=['Sales20'], index=['Product_Number'],  aggfunc=np.sum)
  df_sales20 = df_sales20.reset_index()                #index to columns
  
  df_sales40 = pd.pivot_table(df_sales40, values=['Sales40'], index=['Product_Number'],  aggfunc=np.sum)
  df_sales40 = df_sales40.reset_index()                #index to columns
  
  
  df_sales60 = pd.pivot_table(df_sales60, values=['Sales60'], index=['Product_Number'],  aggfunc=np.sum)
  df_sales60 = df_sales60.reset_index()                #index to columns
  
  
  df_sales80 = pd.pivot_table(df_sales80, values=['Sales80'], index=['Product_Number'],  aggfunc=np.sum)
  df_sales80 = df_sales80.reset_index()                #index to columns
  
  df= pd.merge(df_inv, df_sales20, on=['Product_Number'], how='outer')
    
  df= pd.merge(df, df_sales40, on=['Product_Number'], how='outer')
  
  df= pd.merge(df, df_sales60, on=['Product_Number'], how='outer')
  df= pd.merge(df, df_sales80, on=['Product_Number'], how='outer')
  df=df.fillna(0)
  df_sfr= df.loc[df['Sales80']==0].copy()
  
  df_analiz= df.loc[df['Sales80'] > 0].copy()
  
  df_analiz['Range1']= df_analiz.Sales20
  df_analiz['Range2']= df_analiz.Sales40-df_analiz.Sales20
  df_analiz['Range3']= df_analiz.Sales60-df_analiz.Sales40
  df_analiz['Range4']= df_analiz.Sales80-df_analiz.Sales60
  
  df_analiz['ktsy']= (df_analiz[['Range1','Range2','Range3','Range4']].std(axis=1))/(df_analiz[['Range1','Range2','Range3','Range4']].mean(axis=1))
  
  kosul=[
  
  (df_analiz['ktsy']>= 0) & (df_analiz['ktsy']< 0.36), 
  (df_analiz['ktsy']>= 0.36) & (df_analiz['ktsy']< 0.70),
  (df_analiz['ktsy']>= 0.70 )& (df_analiz['ktsy']< 1.26),
  (df_analiz['ktsy']>= 1.26) ]
  
  secenek=[4,3,2,1]
  df_analiz['Category']= np.select(kosul,secenek,default=4)
  
  df_hedef= df_analiz[['Category','Range1','Range2','Range3','Range4']]
  
  hedef=df_hedef.values.tolist()
  kuple=[]
  tops=[]
  
  
  
  for i in hedef:
   bol=int(i[0])
   #print(bol)
   i.remove(i[0])
   kuple= sorted(i,reverse=True)
  
   tops.append(sum(kuple[0:bol])/bol)
   kuple=[]
  
  df_analiz['Predicted_Sales_Speed']= tops
  
  df_analiz['Stock_Cover'] = (df_analiz.Inventory_Quantity)/(df_analiz.Predicted_Sales_Speed/20)
  
  
  df_analiz['Category']=df_analiz['Category'].replace(1,'New Product1')
  df_analiz['Category']=df_analiz['Category'].replace(2,'New Product2')
  df_analiz['Category']=df_analiz['Category'].replace(3,'Predictable Sales')
  df_analiz['Category']=df_analiz['Category'].replace(4,'Very Predictable Sales')
  
  df_analiz.loc[((df_analiz['Range4'] != 0) & (df_analiz['Category'] == 'New Product1')), 'Category'] = 'Unpredictable Sales'
  
  df_analiz.loc[((df_analiz['Range1'] == 0) & (df_analiz['Category'] == 'New Product1')), 'Category'] = 'Unpredictable Sales'
  
  df_analiz.loc[((df_analiz['Range1'] != 0) & (df_analiz['Category'] == 'New Product1') & (df_analiz['Range3'] != 0) ), 'Category'] = 'Unpredictable Sales' 
  
  df_analiz.loc[((df_analiz['Range4'] != 0) & (df_analiz['Category'] == 'New Product2')), 'Category'] = 'Unpredictable Sales'
  
  df_analiz.loc[((df_analiz['Range2'] == 0) & (df_analiz['Category'] == 'New Product2')), 'Category'] = 'Unpredictable Sales'
  
  df_analiz.loc[((df_analiz['Range1'] == 0) & (df_analiz['Category'] == 'New Product2')), 'Category'] = 'Unpredictable Sales'
  
  df_analiz.loc[((df_analiz['Range1'] <df_analiz['Range2'] ) & (df_analiz['Category'] == 'Predictable Sales') & (df_analiz['Range1'] <df_analiz['Range3'] ) &
   (df_analiz['Range1'] <df_analiz['Range4'] )), 'Category'] = 'Decreasing Sales' 
  
  df_analiz.loc[((df_analiz['Range3']> df_analiz['Range1']) & (df_analiz['Range2']> df_analiz['Range1']) & 
   (df_analiz['Category'] == 'New Product2')), 'Category'] = 'Decreasing Sales'
  
  df_analiz=df_analiz.sort_values(by='Predicted_Sales_Speed', ascending=False) 
  
  df_analiz_download= df_analiz[['Product_Number','Inventory_Quantity','Sales20','Sales40','Sales60','Sales80','Category',
   'Stock_Cover', 'Predicted_Sales_Speed']].copy()
  
  df_analiz_download['Predicted_Sales_Speed']= df_analiz_download['Predicted_Sales_Speed'].round(0)
  df_analiz_download['Stock_Cover']= df_analiz_download['Stock_Cover'].round(0)
  
  
  
  
  df_analiz['Category']=df_analiz['Category'].replace('New Product1','New Products')
  df_analiz['Category']=df_analiz['Category'].replace('New Product2','New Products')
  
  df_analiz['Category']=df_analiz['Category'].replace('Very Predictable Sales','Predictable Sales')
   
  df_tutarlk = pd.pivot_table(df_analiz, values=['Product_Number'], index=['Category'],  aggfunc='count' )
  df_tutarlk = df_tutarlk.reset_index()                #index to columns
  
  df_tutarlk['Kum']=  df_tutarlk['Product_Number'].sum()
  total_product= df_tutarlk['Product_Number'].sum()
  df_tutarlk['Ratio']= df_tutarlk.Product_Number / df_tutarlk.Kum
  
  df_tutarlk.drop(['Kum'], inplace=True, axis=1)
  df_tutarlk.columns= ['Category','Product_Count','Ratio']
  df_tutarlk=df_tutarlk.sort_values(by='Ratio', ascending=False)
  total_product= str(total_product) + ' products analysed'
  #df.style.format("{:.2%}")
  #df.style.format({'B': "{:0<4.0f}", 'D': '{:+.2f}'})
  df_tutarlk= df_tutarlk.style.format({'Ratio': '{:.0%}'})
  st.info('A- Predictability Analysis') 
  total_product
  df_tutarlk
  'Predictability Analysis shows the quality of inventory management. The higher percentage of the "Predictable Sales" ratio indicates the good quality of the inventory management.'
  #download_data
  st.info('B- Inventory Planner')
  'Stock_Cover : The number of days until a product to be out of stock with the predicted sales speed.'
  'Predicted_Sales_Speed : Estimated 30-day sale values '
  
  isim= 'Analsed_Data.csv'
  indir = df_analiz_download.to_csv(index=False)
  b64 = base64.b64encode(indir.encode(encoding='ISO-8859-1')).decode(encoding='ISO-8859-1')  # some strings
  linko_final= f'<a href="data:file/csv;base64,{b64}" download={isim}>Download Analysed Data</a>'
  st.markdown(linko_final, unsafe_allow_html=True)  
  
  df_analiz_show= df_analiz[['Product_Number','Inventory_Quantity','Category','Stock_Cover', 'Predicted_Sales_Speed']].copy()
  
  df_analiz_show['Predicted_Sales_Speed']= df_analiz_show['Predicted_Sales_Speed'].round(0)
  df_analiz_show['Stock_Cover']= df_analiz_show['Stock_Cover'].round(0)
  
  
  
  df_analiz_show
  
  
  if len(df_sfr)>0:
   st.info('C- Zero Sales') 
   'The table shows the products which have no sales in last 80 days.'
   df_sfr   
 
 else:
  st.info('Once uploading is complete, analyses will automaticaly start')







#GETTING DOWNLOAD FILES READY
elif yan_sayfa_secenek == 'Getting CSV Files Ready' :
 #STOKLAR
 st.title('1- Inventory File')
 urly_download= f'<a target="_blank" rel="noopener noreferrer" href="https://www.youtube.com/watch?v=kzYUHItdyOQ">Click to watch partial upload.</a>'
 st.markdown(urly_download,unsafe_allow_html=True)
 urly_download_new= f'<a target="_blank" rel="noopener noreferrer" href="https://www.youtube.com/watch?v=3zrxMl0cueQ">Click to watch how to use one-file upload.</a>'
 st.markdown(urly_download_new,unsafe_allow_html=True)
   
 linko= f'<a target="_blank" rel="noopener noreferrer" href="https://drive.google.com/u/0/uc?id=1bfX9Em80nVK19sCVlpco7sKx7wATOI6K&export=download">Download Inventory_.csv.</a>'  
 'Use the link down to download empty "Inventory_.CSV" file.'
 st.markdown(linko, unsafe_allow_html=True)  
 
 htp1= 'https://raw.githubusercontent.com/ozgurdugmeci/easy-app/main/media/stok_resim.jpg'
 #image = Image.open(htp1)

 #image = Image.open('C:\\Users\\ozgur.dugmeci\\AppData\\Local\\Programs\\Python\\media\\stok_resim.jpg')
 st.image(htp1, caption= 'Inventory Data', width=300)
 'Copy your inventory data and paste it on the downloaded file as it is shown on the image above.'
 'And save the inventory file.'
 warning= f'<p style="color:red;">If you use special characters, it might cause an error.</p>'
 st.markdown(warning, unsafe_allow_html=True)  
 
 
 #20 GUNLUK SATISLAR 
 st.title('2- Sales (20 days) File')
 linko2= f'<a target="_blank" rel="noopener noreferrer" href="https://drive.google.com/u/0/uc?id=1dSGynYDu75J1myKuyoBFQGG0Tu3s6qS6&export=download">Download Sales20_.csv.</a>'  
 'Use the link down to download empty "Sales20_.CSV" file.'
 st.markdown(linko2, unsafe_allow_html=True)  
 htp2='https://raw.githubusercontent.com/ozgurdugmeci/easy-app/main/media/sats20_resim.jpg'
 #image2 = Image.open(htp2)

 #image2 = Image.open('C:\\Users\\ozgur.dugmeci\\AppData\\Local\\Programs\\Python\\media\\sats20_resim.jpg')
 st.image(htp2, caption= '20-day sale data', width=300)
 'Copy your 20-day sale data and paste it on the downloaded file as it is shown on the image above.'
 'And save the 20-day sale file.'
 st.markdown(warning, unsafe_allow_html=True)  
  
 #40 GUNLUK SATISLAR 
 st.title('3- Sales (40 days) File')
 linko3= f'<a target="_blank" rel="noopener noreferrer" href="https://drive.google.com/u/0/uc?id=1azeG8C0ez0Dlf0uU--iOHzM1HBXqyc9X&export=download">Download Sales40_.csv.</a>'
  
 'Use the link down to download empty "Sales40_.CSV" file.'
 st.markdown(linko3, unsafe_allow_html=True)  
 htp3= 'https://raw.githubusercontent.com/ozgurdugmeci/easy-app/main/media/sats40_resim.jpg'
 #image3 = Image.open(htp3)

 #image3 = Image.open('C:\\Users\\ozgur.dugmeci\\AppData\\Local\\Programs\\Python\\media\\sats40_resim.jpg')
 st.image(htp3, caption= '40-day sale data', width=300)
 'Copy your 40-day sale data and paste it on the downloaded file as it is shown on the image above.'
 'And save the 40-day sale file.'

 st.markdown(warning, unsafe_allow_html=True)

 #60 GUNLUK SATISLAR 
 st.title('4- Sales (60 days) File') 
 linko4= f'<a target="_blank" rel="noopener noreferrer" href="https://drive.google.com/u/0/uc?id=13WKDxRcoN9TKQ3aiGDO1V9XKKVeRIRpa&export=download">Download Sales60_.csv.</a>'
 'Use the link down to download empty "Sales60_.CSV" file.'
  
 st.markdown(linko4, unsafe_allow_html=True)  
 htp4= 'https://raw.githubusercontent.com/ozgurdugmeci/easy-app/main/media/sats60_resim.jpg'
 #image4 = Image.open(htp4)
 #image4 = Image.open('C:\\Users\\ozgur.dugmeci\\AppData\\Local\\Programs\\Python\\media\\sats60_resim.jpg')
 st.image(htp4, caption= '60-day sale data', width=300)
 'Copy your 60-day sale data and paste it on the downloaded file as it is shown on the image above.'
 'And save the 60-day sale file.'
 
 st.markdown(warning, unsafe_allow_html=True)
 
 #80 GUNLUK SATISLAR 
 st.title('5- Sales (80 days) File')
 #df_download_satslar40 = downloadSatslarK()[0]
 linko5= f'<a target="_blank" rel="noopener noreferrer" href="https://drive.google.com/u/0/uc?id=18mHbRayNG22gZq6ABxok1To2cNZihyet&export=download">Download Sales80_.csv.</a>'
 'Use the link down to download empty "Sales80_.CSV" file.'
  
 
 st.markdown(linko5, unsafe_allow_html=True)  
 htp5= 'https://raw.githubusercontent.com/ozgurdugmeci/easy-app/main/media/sats80_resim.jpg'
 #image5 = Image.open(htp5)

 #image5 = Image.open('C:\\Users\\ozgur.dugmeci\\AppData\\Local\\Programs\\Python\\media\\sats80_resim.jpg')
 st.image(htp5, caption= '80-day sale data', width=300)
 'Copy your 80-day sale data and paste it on the downloaded file as it is shown on the image above.'
 'And save the 80-day sale file.'
 
 st.markdown(warning, unsafe_allow_html=True)

 
elif yan_sayfa_secenek == 'About Analyses' :
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
 
 st.subheader('2- Inventory Planner') 
 

 
 htp7='https://raw.githubusercontent.com/ozgurdugmeci/easy-app/main/media/planner_resim.jpg'

 #htp7='gs://imajo/media/planner_resim.jpg'
 
 #image7 = Image.open(htp7)


 st.image(htp7, caption= 'Inventory Planner', width=800)
 planner= f'<p>This analysis gives the core insights to plan inventory. You can check the <b>"Stock_Cover" </b> values. In other words, it shows the number of days until a product\
  will be out of stock. Thus necessary actions can be taken before a product quantity comes to a critical low level. <b>"Predicted_Sales_Speed"</b> is the estimated 20-day \
  sale values.  Analysing these values with the category information can help you in taking decisions.</p>'
 
 st.markdown(planner,unsafe_allow_html=True)
 st.subheader('3- Zero Sales') 
 'The products have no sales in the last 80 days are listed here. If there are no such products, this analysis does not appear on the screen.' 
elif yan_sayfa_secenek == 'Contact' :
 
 st.title('Contact With Us')
 mail_b= f'<p>Your feed back is very important for us. Write about your user experience. Give us kudos! Ask questions. Inform us\
 about the errors you encountered. Tell about new ideas. You can reach us by clicking the link below. </p>'
 
 info_link= f'<a target="_blank" rel="noopener noreferrer" href="https://ozgur-dugmeci.medium.com/easy-inventory-planner-c1e5fc4aa0e">Click here to leave a comment.</a>'
 st.markdown(mail_b,unsafe_allow_html=True)
 st.markdown(info_link,unsafe_allow_html=True)

elif yan_sayfa_secenek == 'Direct Excel Upload & Analyses' :
 st.title("1- One File Upload")
 
 st.info('Once excel file is uploaded, analyses will automatically start.')
 urly_download_new= f'<a target="_blank" rel="noopener noreferrer" href="https://www.youtube.com/watch?v=3zrxMl0cueQ">Click to watch how to use one-file upload.</a>'
 st.markdown(urly_download_new,unsafe_allow_html=True)
 rowy=[]
 "Upload an excel file considering the column names below."
 
 rowy=['Product No','Category','Sub Category','21-Day Sale','42-Day Sale','63-Day Sale','84-Day Sale','Inventory Quantity']
 st.write('Column order in excel file must be :')
 rowy   
 st.set_option('deprecation.showfileUploaderEncoding', False)
 uploaded_file_x = st.file_uploader("Select Excel File To Upload", type=['xlsx'])
 
 if uploaded_file_x :
  try:
   df = pd.read_excel(uploaded_file_x)
   df.columns=['Product','Category','Sub-Category','Sales21','Sales42','Sales63','Sales84','Inventory']
   df['Product'] = df['Product'].astype('str')
   df['Category'] = df['Category'].astype('str')
   df['Sub-Category'] = df['Sub-Category'].astype('str')
   df_dummx= df.copy() 
   df_dummx= df_dummx.astype(str)
    
   df['Product'].fillna('-',inplace=True)
   df['Category'].fillna('-',inplace=True)
   df['Sub-Category'].fillna('-',inplace=True)
   df['Sales21'].fillna(0,inplace=True)
   df['Sales42'].fillna(0,inplace=True)
   df['Sales63'].fillna(0,inplace=True)
   df['Sales84'].fillna(0,inplace=True)
   df['Inventory'].fillna(0,inplace=True)
   st.dataframe(df_dummx) 
  except:
   'Upload Error.'
   'Check the excel file.'
   
   st.stop() 
  #df=pd.DataFrame(rows) 
  
  try:
   df_sfr= df.loc[df['Sales84']==0].copy()
    
   df_analiz= df.loc[df['Sales84'] > 0].copy()
    
   df_analiz['Range1']= df_analiz.Sales21
   df_analiz['Range2']= df_analiz.Sales42-df_analiz.Sales21
   df_analiz['Range3']= df_analiz.Sales63-df_analiz.Sales42
   df_analiz['Range4']= df_analiz.Sales84-df_analiz.Sales63
    
   df_analiz['ktsy']= (df_analiz[['Range1','Range2','Range3','Range4']].std(axis=1))/(df_analiz[['Range1','Range2','Range3','Range4']].mean(axis=1))
    
   kosul=[
    
   (df_analiz['ktsy']>= 0) & (df_analiz['ktsy']< 0.36), 
   (df_analiz['ktsy']>= 0.36) & (df_analiz['ktsy']< 0.70),
   (df_analiz['ktsy']>= 0.70 )& (df_analiz['ktsy']< 1.26),
   (df_analiz['ktsy']>= 1.26) ]
    
   secenek=[4,3,2,1]
   df_analiz['Label']= np.select(kosul,secenek,default=4)
    
   df_hedef= df_analiz[['Label','Range1','Range2','Range3','Range4']]
    
   hedef=df_hedef.values.tolist()
   kuple=[]
   tops=[]
    
    
    
   for i in hedef:
    bol=int(i[0])
    #print(bol)
    i.remove(i[0])
    kuple= sorted(i,reverse=True)
    
    tops.append(sum(kuple[0:bol])/bol)
    kuple=[]
    
   df_analiz['Predicted_Sales']= tops
    
    
    
   df_analiz['Label']=df_analiz['Label'].replace(1,'New Product1')
   df_analiz['Label']=df_analiz['Label'].replace(2,'New Product2')
   df_analiz['Label']=df_analiz['Label'].replace(3,'Predictable Sales')
   df_analiz['Label']=df_analiz['Label'].replace(4,'Very Predictable Sales')
    
   df_analiz.loc[((df_analiz['Range4'] != 0) & (df_analiz['Label'] == 'New Product1')), 'Label'] = 'Unpredictable Sales'
    
   df_analiz.loc[((df_analiz['Range1'] == 0) & (df_analiz['Label'] == 'New Product1')), 'Label'] = 'Unpredictable Sales'
    
   df_analiz.loc[((df_analiz['Range1'] != 0) & (df_analiz['Label'] == 'New Product1') & (df_analiz['Range3'] != 0) ), 'Label'] = 'Unpredictable Sales' 
    
   df_analiz.loc[((df_analiz['Range4'] != 0) & (df_analiz['Label'] == 'New Product2')), 'Label'] = 'Unpredictable Sales'
    
   df_analiz.loc[((df_analiz['Range2'] == 0) & (df_analiz['Label'] == 'New Product2')), 'Label'] = 'Unpredictable Sales'
    
   df_analiz.loc[((df_analiz['Range1'] == 0) & (df_analiz['Label'] == 'New Product2')), 'Label'] = 'Unpredictable Sales'
    
   df_analiz.loc[((df_analiz['Range1'] <df_analiz['Range2'] ) & (df_analiz['Label'] == 'Predictable Sales') & (df_analiz['Range1'] <df_analiz['Range3'] ) &
    (df_analiz['Range1'] <df_analiz['Range4'] )), 'Label'] = 'Decreasing Sales' 
    
   df_analiz.loc[((df_analiz['Range3']> df_analiz['Range1']) & (df_analiz['Range2']> df_analiz['Range1']) & 
    (df_analiz['Label'] == 'New Product2')), 'Label'] = 'Decreasing Sales'
    
   df_analiz['Stock_Cover'] = (df_analiz.Inventory)/(df_analiz.Predicted_Sales/21)
   df_analiz['Predicted_Sales'] = (df_analiz.Predicted_Sales/21)*30
     
   df_analiz=df_analiz.sort_values(by='Predicted_Sales', ascending=False) 
    
   df_analiz_download= df_analiz[['Product','Inventory','Sales21','Sales42','Sales63','Sales84','Label',
   'Stock_Cover', 'Predicted_Sales']].copy()
    
   df_analiz_download['Predicted_Sales']= df_analiz_download['Predicted_Sales'].round(0)
   df_analiz_download['Stock_Cover']= df_analiz_download['Stock_Cover'].round(0)
    
    
    
    
   df_analiz['Label']=df_analiz['Label'].replace('New Product1','New Products')
   df_analiz['Label']=df_analiz['Label'].replace('New Product2','New Products')
    
   df_analiz['Label']=df_analiz['Label'].replace('Very Predictable Sales','Predictable Sales')
     
   df_tutarlk = pd.pivot_table(df_analiz, values=['Product'], index=['Label'],  aggfunc='count' )
   df_tutarlk = df_tutarlk.reset_index()                #index to columns
    
   df_tutarlk['Kum']=  df_tutarlk['Product'].sum()
   total_product= df_tutarlk['Product'].sum()
   df_tutarlk['Ratio']= df_tutarlk.Product / df_tutarlk.Kum
    
   df_tutarlk.drop(['Kum'], inplace=True, axis=1)
   df_tutarlk.columns= ['Label','Product_Count','Ratio']
    
   df_tutarlk2=df_tutarlk.copy()
    
   df_tutarlk2['Ratio']=df_tutarlk2['Ratio']*100
   df_tutarlk2['Ratio']= df_tutarlk2['Ratio'].round(0)  
    
   total_product= str(total_product) + ' products analysed'
   #df_tutarlk['Product_Count']=df_tutarlk['Product_Count'].astype(str)
   #df_tutarlk['Ratio']=df_tutarlk['Ratio'].astype(str)
   #df.style.format("{:.2%}")
   #df.style.format({'B': "{:0<4.0f}", 'D': '{:+.2f}'})
   #df_tutarlk= df_tutarlk.style.format({'Ratio': '{:.0%}'})
   st.info('A- Predictability Analysis') 
   total_product
   df_tutarlk2=df_tutarlk2.astype(str)
   df_tutarlk2['Ratio']='%' + df_tutarlk2['Ratio']
   #df_tutarlk2=df_tutarlk2.sort_values(by='Ratio', ascending=False)
   st.dataframe(df_tutarlk2)
   'Predictability Analysis shows the quality of inventory management. The higher percentage of the "Predictable Sales" ratio indicates the good quality of the inventory management.'
   #download_data
   st.info('B- Inventory Planner')
   'Stock_Cover : The number of days until a product to be out of stock with the predicted sales speed.'
   'Predicted_Sales : Estimated 30-day sale values '
    
   isim= 'Analsed_Data.csv'
   indir = df_analiz_download.to_csv(index=False)
   b64 = base64.b64encode(indir.encode(encoding='ISO-8859-1')).decode(encoding='ISO-8859-1')  # some strings
   linko_final= f'<a href="data:file/csv;base64,{b64}" download={isim}>Download Analysed Data</a>'
   st.markdown(linko_final, unsafe_allow_html=True)  
    
   df_analiz_show= df_analiz[['Product','Category','Sub-Category','Inventory','Label','Stock_Cover', 'Predicted_Sales','Sales21','Sales42','Sales63','Sales84']].copy()
    
   df_analiz_show['Predicted_Sales']= df_analiz_show['Predicted_Sales'].round(0)
   df_analiz_show['Stock_Cover']= df_analiz_show['Stock_Cover'].round(0)
    
   df_analiz_show['Stock_Cover']=df_analiz_show['Stock_Cover'].astype(int)
   df_analiz_show['Predicted_Sales']=df_analiz_show['Predicted_Sales'].astype(int)
   df_analiz_show=df_analiz_show.reset_index(drop=True)
   df_analiz_show2=df_analiz_show.astype(str)
   st.dataframe(df_analiz_show2)
     
   if len(df_sfr)>0:
    st.info('C- Zero Sales') 
    'The table shows the products which have no sales in last 80 days.'
    df_sfr=df_sfr.reset_index(drop=True)
    df_sfr2=df_sfr.astype(str).copy()
    st.dataframe(df_sfr2)   
  except:
   'Excel dosya sütunlarını kontrol edin.'
 
   
 
 
 
elif yan_sayfa_secenek == 'Application Guide' :
  
 st.title('Easy Inventory Planner Guide')
    
 

 biry= f'<p>It is an easy-to-use and smart way to manage your inventory. <br> \
  This app uses an unsupervised machine learning model to analyze your sales and stock data, calculating the sales speed for each product. <br> This helps you estimate \
  how long your stock will last. With Easy Inventory Planner, you can easily keep track of your inventory levels, predict future needs, and avoid running out or having \
  too much stock. The app is simple and intuitive design makes it easy to use, helping you make better decisions and keep your business running smoothly.  <p>'
 
 st.markdown(biry,unsafe_allow_html=True)
    
 
 
 urly= f'<a target="_blank" rel="noopener noreferrer" href="https://www.youtube.com/watch?v=kzYUHItdyOQ">Click to watch partial upload.</a>'
 st.markdown(urly,unsafe_allow_html=True)
 urly_download_new= f'<a target="_blank" rel="noopener noreferrer" href="https://www.youtube.com/watch?v=3zrxMl0cueQ">Click to watch how to use one-file upload.</a>'
 st.markdown(urly_download_new,unsafe_allow_html=True)
 htp0='https://raw.githubusercontent.com/ozgurdugmeci/easy-app/main/media/model3.jpg'
 #image0 = Image.open(htp6)
 st.image(htp0, caption= 'Model', width=800)

 st.subheader('A- Getting uploading files ready (Partial Upload)')
 metin2= f'<p> - This part only accepts csv file format.</br> - Go to "Getting CSV Files Ready" page and download empty csv files. </br>- There are 5 csv files to download.\
  </br> - Paste related data to empty csv files.  </br> - Be sure column names exist on the csv files. </br>- On each csv file  product number information \
  has to be on column A.</br> - Quantity information has to be on column B. </br> - The data pasted on other columns, other than column A or column B, causes error.</p>'
 st.markdown(metin2,unsafe_allow_html=True)

 st.subheader('B- Uploading Files & Analyses (Partial Uopload)')
 metin4= f' <p> - There are upload spaces for each csv file.</br> - Drag and drop or simply browse and select the related csv file. </br> - Analyses will appear after\
  all files are uploaded. </br> - Check "About Analyses" page.'
 st.markdown(metin4,unsafe_allow_html=True)

 st.subheader('C- Direct Excel Upload & Analyses')
 metin_excel= f' <p> - Prepare excel file with the correct order of the columns.</br> - Upload excel file. </p>'
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
    
    
    
