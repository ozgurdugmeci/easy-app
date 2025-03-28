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
from datetime import *
import pymongo
#there you go mate
mail=st.experimental_user.email
tarh=datetime.now()
tarh=str(tarh)
tarh=tarh[:10]

if 'keyo' not in st.session_state:
 st.session_state['keyo']= 1
a=st.session_state.keyo
'heyo'
a
st.title("1- Excel Upload & Analyses")
if st.button("🔓 Logout"):
 st.logout()

app_name= st.secrets['mongo']['app']
host=st.secrets['mongo']['host']
user_name= st.secrets['mongo']['username']
password= st.secrets['mongo']['password']
dbase=st.secrets['database']['dbase']
koleksiyon=st.secrets['database']['koleksiyon']


# Create a new client and connect to the server
# Uses st.cache_resource to only run once.

if st.session_state.keyo == 1:

 client = pymongo.MongoClient(f"mongodb+srv://{user_name}:{password}@{host}/?retryWrites=true&w=majority&appName={app_name}")

 
 # Select the database and collection
 db = client[dbase]  # Replace with your actual database name
 collection = db[koleksiyon]  # Replace with your actual collection name

 # New document to insert
 new_document = {
    "company": "easy-free",
    "email": mail,
    "date": tarh}

 insert_result = collection.insert_one(new_document)
 st.session_state.keyo= 0


st.info('Upload excel file or click the button below. Analyses will automatically start.')
but= st.button("Upload Test Data",type="primary") 
urly_download_new= f'<a target="_blank" rel="noopener noreferrer" href="https://www.youtube.com/watch?v=wahIMj-G3sE">Click to watch how to upload excel file.</a>'
st.markdown(urly_download_new,unsafe_allow_html=True)
rowy=[]
"Upload an excel file considering the column names below."

rowy=['Product No','Category','Sub Category','21-Day Sale Qty','42-Day Sale Qty','63-Day Sale Qty','84-Day Sale Qty','Inventory Quantity']
st.write('Column order in excel file must be :')
rowy   
#st.set_option('deprecation.showfileUploaderEncoding', False)
uploaded_file_x = st.file_uploader("Select Excel File To Upload", type=['xlsx'])

if uploaded_file_x or but :
 try:
  if uploaded_file_x: 
   df = pd.read_excel(uploaded_file_x)
  elif but:
   df = pd.read_csv('https://docs.google.com/spreadsheets/d/' + 
                  '1xkaMB5vc_Jx5MqTc97ukyQgYOqFnGgNUQ7SP2FfQm_Q' +
                  '/export?gid=0&format=csv') 
   
   
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
  'Firs 4 rows of the uploaded data'
  st.dataframe(df_dummx.head(4)) 
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
  b64 = base64.b64encode(indir.encode(encoding='utf-8')).decode(encoding='utf-8')  # some strings
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
  
takip= """ 
<!-- Default Statcounter code for easy_analyses
https://demand-planning-tool.streamlit.app/ -->
<script type="text/javascript">
var sc_project=13027553; 
var sc_invisible=1; 
var sc_security="8a9f5352"; 
</script>
<script type="text/javascript"
src="https://www.statcounter.com/counter/counter.js"
async></script>
<noscript><div class="statcounter"><a title="Web Analytics
Made Easy - Statcounter" href="https://statcounter.com/"
target="_blank"><img class="statcounter"
src="https://c.statcounter.com/13027553/0/8a9f5352/1/"
alt="Web Analytics Made Easy - Statcounter"
referrerPolicy="no-referrer-when-downgrade"></a></div></noscript>
<!-- End of Statcounter Code -->
"""
#st.markdown(takip, unsafe_allow_html=True)  
components.html(takip,width=200, height=200)
    
