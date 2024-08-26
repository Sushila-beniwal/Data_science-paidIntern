import streamlit as st



st.markdown("<h2 style='color: #036029;'>scrap data of available doctors from practo.com</h2>",unsafe_allow_html=True)
st.image("41667647-medical-background-with-a-doctor.jpg",width=400,caption="scrape available doctors from practo",use_column_width=False,output_format='auto',channels='RGB')
Location = st.text_input("enter the location")
Specialization = st.selectbox("select the specialization you need",('dermatologist','dentist','general physician','gynecologist/obstetrician','homoeopath','ayurveda','Ear-nose-throat (ent) Specialist'))






def no_of_doctors_available(Loc,speciality):
    #import required libraries for web scrapping

    import requests
    from bs4 import BeautifulSoup 
    from urllib.request import urlopen



    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'} 

    url = "https://www.practo.com/"+Loc+"/"+speciality

    

    try:
        url = requests.get(url,headers=headers).text

        beautify = BeautifulSoup(url,'html.parser')
        ans = beautify.find('div',{"class":"c-listing-wrapper"}).div.div.div.div
        if ans:
            
            doctors_available = ans.text.strip()
            return doctors_available
           
        else:
            return "we couldn't find doctors for you"
        
    except requests.exceptions.RequestException as e:
        return f"an error occured {e}"





#create button using streamlit
Button = st.button("Scrape")


#if doctors available returns noof available doctors
#else print no doctor is available

if Button:
    st.write(no_of_doctors_available(Location,Specialization))



