import streamlit as st

#st.login("google")
####-------------------------------------------------
st.set_page_config(
    page_title="page_title",
    page_icon="✨",
    initial_sidebar_state="expanded"   
)
#initial_sidebar_state="collapsed",
# Define app pages
landing_page = st.Page("./pages/_01_Home.py", title="Landing", icon=":material/home:")
about_page = st.Page("./pages/_02_About_Analyses.py", title="App", icon=":material/play_arrow:")
admin_page = st.Page("./pages/_03_Excel Upload & Analayses.py", title="Admin", icon=":material/admin_panel_settings:"
)



if not st.experimental_user.is_logged_in:
    pg = st.navigation(
        [landing_page],
        position="hidden",
    )
elif st.experimental_user.email == 'ozgur.dugmeci@gmail.com':
    pg = st.navigation(
        [admin_page],
    )
else:
    pg = st.navigation(
        [app_page],
        position="hidden",
    )

# Head to first page of navigation
pg.run()
