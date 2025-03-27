import streamlit as st

#st.login("google")
####-------------------------------------------------
st.set_page_config(
    page_title="Login Page",
    page_icon="✨",
    initial_sidebar_state="expanded"   
)
#initial_sidebar_state="collapsed",
# Define app pages
landing_page = st.Page("./pages/_01_Home.py", title="Demand Planning", icon=":material/home:")
about_page = st.Page("./pages/_02_About_Analyses.py", title="About Analyses", icon=":material/play_arrow:")
analiz_page = st.Page("./pages/_03_Excel Upload & Analyses.py", title="App", icon=":material/admin_panel_settings:"
)



if not st.experimental_user.is_logged_in:
    pg = st.navigation(
        [landing_page],
        position="hidden",
    )
elif st.experimental_user.email == 'ozgur.dugmeci@gmail.com':
    pg = st.navigation(
        [analiz_page,about_page],
    )
else:
    pg = st.navigation(
        [analiz_page,about_page],
        
    )

# Head to first page of navigation
pg.run()
