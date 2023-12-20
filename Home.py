import streamlit as st
from streamlit_option_menu import option_menu
import time
st.set_page_config(
        page_title="Hello world",
        page_icon="chart_with_upwards_trend",
        layout="wide",
    )
sbb = st.sidebar
with sbb:
    st.markdown("""
            <html>
            <head>
            <title>My Button</title>
            <style>
            .my-button {
                background-color: #4CAF50;
                border: none;
                color: white;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 10px; /* adds rounded corners with a radius of 10px */
                background-image: url('https://play-lh.googleusercontent.com/fJwcR6E_LgEvhaU5mUlPGjJkx-SwfZF1PO2lLynHiKaZ8nL28SzRjvtPWXcJTy2yIA');
            }
            .center {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100px;
}
            </style>
        </head>
        <body>
            <a href="https://rajaneha.github.io/Aboutus/" target="_self">
            <div class="center">
                <button class="my-button">About Us</button>
            </div>
            </a>
        </body>
        </html>
                """,unsafe_allow_html=True)


insta = f"""
        <html>

        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-github" viewBox="0 0 16 16">
        <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
        </svg>
        </html>"""

st.header("Heart Beat Analysis❤️❤️-with Noise reduction 🔇")
selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Projects", "Contact"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.pinimg.com/originals/12/9e/d1/129ed173a7801dcfc668e48e84dd0e27.jpg");
background-size: 180%;
background-position: top left;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("""
<html>
<head>
	<title>Marquee Example</title>
	<style>
		/* CSS styles */
		.marquee {
			font-size: 24px; /* change to desired font size */
            color:red;
            font-family: sans-serif;
		}
	</style>
</head>
<body>
	<marquee behavior="scroll" direction="center" class="marquee" scrollamount="10">
		DID YOU CALL FOR A CARDIOLOGIST?
	</marquee>
</body>
</html>
""",unsafe_allow_html=True)

st.markdown("""
<html>
<head>
	<title>Marquee Example</title>
	<style>
		/* CSS styles */
		.marquee {
			font-size: 24px; /* change to desired font size */
            color:white;
            font-family: sans-serif;
		}
	</style>
</head>
<body>
	<marquee behavior="scroll" direction="center" class="marquee" scrollamount="10">
		BECAUSE I'M HERE TO FIX YOUR BROKEN HEART
	</marquee>
</body>
</html>
""",unsafe_allow_html=True)


with st.sidebar:
    st.image("images/heartfly.gif")



if selected == "Home":
    with st.expander("BMI impact on heart"):
            st.write("""BMI (Body Mass Index) can impact the health of the heart.
          BMI is a measure of body fat based on height and weight, 
          and it is often used as an indicator of overall health. 
          High BMI is associated with an increased risk of cardiovascular disease, 
          including heart disease and stroke.""")
            weight = st.number_input("Enter your weight (in kgs)")

            # TAKE HEIGHT INPUT
            # radio button to choose height format
            status = st.radio('Select your height format: ',
                            ('cms', 'meters', 'feet'))

            # compare status value
            if(status == 'cms'):
                # take height input in centimeters
                height = st.number_input('Centimeters')

                try:
                    bmi = weight / ((height/100)**2)
                except:
                    st.text("Enter some value of height")

            elif(status == 'meters'):
                # take height input in meters
                height = st.number_input('Meters')

                try:
                    bmi = weight / (height ** 2)
                except:
                    st.text("Enter some value of height")

            else:
                # take height input in feet
                height = st.number_input('Feet')

                # 1 meter = 3.28
                try:
                    bmi = weight / (((height/3.28))**2)
                except:
                    st.text("Enter some value of height")

            # check if the button is pressed or not
            if(st.button('Calculate BMI')):

                # print the BMI INDEX
                st.text("Your BMI Index is {}.".format(bmi))

                # give the interpretation of BMI index
                if(bmi < 16):
                    st.error("You are Extremely Underweight")
                elif(bmi >= 16 and bmi < 18.5):
                    st.warning("You are Underweight")
                elif(bmi >= 18.5 and bmi < 25):
                    st.success("Healthy")
                elif(bmi >= 25 and bmi < 30):
                    st.warning("Overweight")
                elif(bmi >= 30):
                    st.error("Extremely Overweight")

    with st.expander("Tips for good heart"):
        st.code("""Waist circumference: People with a larger waist circumference (more than 40 inches for men and 35 inches for women) are at increased risk for heart disease.

Physical activity: Regular exercise is important for maintaining a healthy weight and reducing the risk of heart disease.

Diet: A diet rich in fruits, vegetables, whole grains, and lean proteins can help reduce the risk of heart disease.

Smoking: Smoking is a major risk factor for heart disease and should be avoided.

Blood pressure and cholesterol levels: High blood pressure and cholesterol levels can increase the risk of heart disease, so it's important to get regular check-ups and monitor these levels.""")

    
    #Latest News
    st.markdown("""
        <html>
        <head>
            <link rel="stylesheet" type="text/css" href="style1.css">
        </head>
        <body>
        <div class="container">
        <ul class="cards">
            <li class="card">
            <img src="https://images.livemint.com/img/2023/02/14/600x338/covid_vaccines_1676340332969_1676340333180_1676340333180.jpg" >
            <div><br>
                <h4 class="card-title">Covid-19 vaccines affecting heart?</h4>
                <div class="card-content">
                <p>While the Covid-19 vaccines are saving lives, some side effects related to heart has been reported..</p>
                </div>
            </div>
            <div class="card-link-wrapper">
                <a href="https://www.livemint.com/news/india/are-covid-19-vaccines-covishield-covaxin-affecting-the-heart-what-doctors-say-11676338426015.html" class="card-link">Learn More</a>
            </div>
            </li>
            <li class="card">
            <img src="https://assets.medpagetoday.net/media/images/103xxx/103281.jpg" alt="news2" style="width:100%">
            <div><br>
                <h4 class="card-title">Erythritol and cardiovascular events</h4>
                <div class="card-content">
                <p>Artificial sweeteners have become a widespread way to reduce sugar and calorie intake.Regulatory agencies..</p>
                </div>
            </div>
            <div class="card-link-wrapper">
                <a href="https://www.nih.gov/news-events/nih-research-matters/erythritol-cardiovascular-events" class="card-link">Learn More</a>
            </div>
            </li>
            <li class="card">
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSw9PnEG-Y1UJwoxE_wmtL5oY1LG2cxHYpZwQ&usqp=CAU" alt="news3" style="width:100%">
            <div><br>
                <h4 class="card-title">Heart Attack risk</h4>
                <div class="card-content">
                <p> In this post-Covid era, healthcare has become essential and something all of us should keep up with. There are two ways that...</p>
                </div>
            </div>
            <div class="card-link-wrapper">
                <a href="https://zeenews.india.com/health/exclusive-heart-attack-what-screening-tests-do-you-need-to-track-heart-health-check-doctors-advice-2582808" class="card-link">Learn More</a>
            </div>
            </li>
            <li class="card">
            <img src="https://images.indianexpress.com/2023/03/poor-sleep.jpg?w=640" alt="news4" style="width:100%">
            <div><br>
                <h4 class="card-title">Poor sleep</h4>
                <div class="card-content">
                <p>Poor sleep is associated with up to seven years’ worth of increased heart disease risk and even premature death, according to a study..</p>
                </div>
            </div>
            <div class="card-link-wrapper">
                <a href="https://indianexpress.com/article/lifestyle/health/poor-sleep-increased-heart-disease-risk-study-8478705/" class="card-link">Learn More</a>
            </div>
            </li>
            <li class="card">
            <img src="https://d2jx2rerrg6sh3.cloudfront.net/image-handler/picture/2019/9/%40shutterstock_721804543.jpg" alt="news5" style="width:100%">
            <div><br>
                <h4 class="card-title">Chronic Heart Diseases</h4>
                <div class="card-content">
                <p>World Health Organization (WHO)  in its reports has said that cardiovascular diseases are the number one cause of death globally...</p>
                </div>
            </div>
            <div class="card-link-wrapper">
                <a href="https://www.indiatvnews.com/health/chronic-heart-diseases-prevent-heart-problems-with-these-essential-cooking-methods-2023-03-15-854722" class="card-link">Learn More</a>
            </div>
            </li>
            <li class="card">
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRivig12ejPMuCUMQlJ0g0-CTnAK-OBQlLy0S6m_4dr_kvzitmpxtj_PIwcLmXj-zqtjPQ&usqp=CAU" alt="news6" style="width:100%">
            <div><br>
                <h4 class="card-title">Apple Watch </h4>
                <div class="card-content">
                <p>A man from the UK received back-to-back notifications of irregular heart rhythm during his sleep. He was later diagnosed with atrial...</p>
                </div>
            </div>
            <div class="card-link-wrapper">
                <a href="https://www.indiatoday.in/technology/news/story/apple-watch-helps-man-detect-undiagnosed-heart-condition-by-sending-alerts-for-irregular-heart-rate-2346518-2023-03-14" class="card-link">Learn More</a>
            </div>
            </li>
            <li class="card">
            <img src="https://i0.wp.com/post.medicalnewstoday.com/wp-content/uploads/sites/3/2023/03/racing-heart-pulse-anxiety-1296x728-header-1024x575.jpg?w=1155&h=1528" alt="news7" style="width:100%">
            <div><br>
                <h3 class="card-title">Can heart rhythms influence anxiety?</h3>
                <div class="card-content">
                <p>Recently, researchers used optogenetics to assess how increasing heart rate affects behavior in mice.Optogenetics...</p>
                </div>
            </div>
            <div class="card-link-wrapper">
                <a href="https://www.medicalnewstoday.com/articles/could-a-racing-heart-trigger-anxiety-rather-than-the-other-way-around" class="card-link">Learn More</a>
            </div>
            </li>
        </ul>
        </div>
        </body>
        </html>
        <style>
        :root {
        --red: #ef233c;
        --darkred: #c00424;
        --platinum: #e5e5e5;
        --black: #2b2d42;
        --white: #fff;
        --thumb: #edf2f4;
        --baby: #89cff0;
        --ba: #add8e6;
        }
        * {
        box-sizing: border-box;
        padding: 0;
        margin: 0;
        }
        body {
        font: 16px / 24px "Rubik", sans-serif;
        color: var(--white);
        background: var(--black);
        margin: 50px 0;
        }
        .container {
        width: 600px;
        height:500px;
        padding: 0 15px;
        margin: 0 auto;
        }
        h2 {
        font-size: 32px;
        margin-bottom: 1em;
        }
        .cards {
            width: 500px;
        height:400px;
        display: flex;
        padding: 25px 0px;
        list-style: none;
        overflow-x: scroll;
        scroll-snap-type: x mandatory;
        }
        .card {
            width: 500px;
        height:400px;
        display: flex;
        flex-direction: column;
        flex: 0 0 100%;
        padding: 20px;
        background: var(--ba);
        border-radius: 12px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 15%);
        scroll-snap-align: start;
        transition: all 0.2s;
        }
        .card:not(:last-child) {
        margin-right: 10px;
        }
        .card:hover {
        color: var(--white);
        background:#89cff0;
        }
        .card .card-title {
        font-size: 20px;
        }
        .card .card-content {
        margin: 20px 0;
        width: 85%;
        }
        .card .card-link-wrapper {
        margin-top: auto;
        }
        .card .card-link {
        display: inline-block;
        text-decoration: none;
        color: white;
        background: var(--red);
        padding: 6px 10px;
        border-radius: 8px;
        transition: background 0.2s;
        }
        .card:hover .card-link {
        background: var(--darkred);
        }
        .cards::-webkit-scrollbar {
        height: 12px;
        }
        .cards::-webkit-scrollbar-thumb,
        .cards::-webkit-scrollbar-track {
        border-radius: 92px;
        }
        .cards::-webkit-scrollbar-thumb {
        background: var(--darkred);
        }
        .cards::-webkit-scrollbar-track {
        background: var(--thumb);
        }
        @media (width: 200%) {
        .card {
            flex-basis: calc(50% - 10px);
        }
        .card:not(:last-child) {
            margin-right: 20px;
        }
        }
        @media (max-width: 500px) {
        .card {
            flex-basis: calc(calc(100% / 3) - 20px);
        }
        .card:not(:last-child) {
            margin-right: 30px;
        }
        }
        @media (width: 800px) {
        .card {
            flex-basis: calc(25% - 30px);
        }
        .card:not(:last-child) {
            margin-right: 40px;
        }
        }
        /* FOOTER STYLES
        –––––––––––––––––––––––––––––––––––––––––––––––––– */
        .page-footer {
        position: fixed;
        right: 0;
        bottom: 50px;
        display: flex;
        align-items: center;
        padding: 5px;
        z-index: 1;
        }
        .page-footer a {
        display: flex;
        margin-left: 4px;
        }
        </style>
        """,unsafe_allow_html=True)

    st.markdown("<br><hr>", unsafe_allow_html=True)


    split = st.columns(1)
    #st.image("https://cdn-icons-png.flaticon.com/512/3621/3621464.png",width=100)
    
if selected == "Projects":
    icon_size = 20
    st.markdown(insta,unsafe_allow_html=True)
    st.markdown("[Click here to go to GitHub!](https://github.com/Rajaneha/Heart-Beat-Analysis-Noise-Reduction)")

    tab1,tab2 = st.tabs(['Source Code','Model Accuracy'])
    with tab1:
        with open('Modelrnn\ModelBuilding.py','r') as f:
            st.code(f.read(),language="python")
    with tab2:
        st.write("""Model train data score  :  78 %\n
        model test data score               :  75 %\n
        model validation data score         :  83 %\n
        model unlabeled data score          :  76 %\n
        Total score                         :  0.7457627058029175""")
if selected == "Contact":
    st.markdown("""
            <html>
            <head>
            <title>My Button</title>
            <style>
            .my-button {
                background-color: #4CAF50;
                border: none;
                color: white;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 10px; /* adds rounded corners with a radius of 10px */
                background-image: url('https://play-lh.googleusercontent.com/fJwcR6E_LgEvhaU5mUlPGjJkx-SwfZF1PO2lLynHiKaZ8nL28SzRjvtPWXcJTy2yIA');
            }
            .center {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100px;
}
            </style>
        </head>
        <body>
            <a href="https://rajaneha.github.io/contactpage/" target="_self">
            <div class="center">
                <button class="my-button">Contact Form</button>
            </div>
            </a>
        </body>
        </html>
                """,unsafe_allow_html=True)




    st.markdown("""<html>
    <head>
    <title>Rating Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f7f7f7;
        }
        h1 {
            text-align: center;
            margin-top: 40px;
        }
        .rating {
            display: flex;
            flex-direction: row-reverse;
            justify-content: center;
            align-items: center;
            font-size: 60px;
            color: #ffd700;
            margin-top: 60px;
        }
        .rating > label {
            margin: 0 15px;
            cursor: pointer;
        }
        .rating > label:hover,
        .rating > label:hover ~ label {
            color: #f5bc42;
        }
        .rating > input:checked ~ label {
            color: #f5bc42;
        }
        .rating > input:checked ~ label:hover,
        .rating > input:checked ~ label:hover ~ label {
            color: #ffd700;
        }
        .submit-button {
            display: block;
            margin-top: 60px;
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            font-size: 24px;
            font-weight: bold;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
    </head>
    <body>
    <h1>Rate our WebPage</h1>
    <div class="rating">
        <input type="radio" id="star5" name="rating" value="5" /><label for="star5">&#9733;</label>
        <input type="radio" id="star4" name="rating" value="4" /><label for="star4">&#9733;</label>
        <input type="radio" id="star3" name="rating" value="3" /><label for="star3">&#9733;</label>
        <input type="radio" id="star2" name="rating" value="2" /><label for="star2">&#9733;</label>
        <input type="radio" id="star1" name="rating" value="1" /><label for="star1">&#9733;</label>
    </div>
    <button class="submit-button">Submit</button>
    </body>
    </html>""",unsafe_allow_html=True)



#st.balloons()
st.markdown(
    """
    <style>
    .icon-container {
        bottom: 20px;
        right: 20px;
    }
    .icon-container a {
        margin-left: 10px;
    }
    </style>
    """,unsafe_allow_html=True
)


yt = f"""
        <html>
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-youtube" viewBox="0 0 16 16">
        <path d="M8.051 1.999h.089c.822.003 4.987.033 6.11.335a2.01 2.01 0 0 1 1.415 1.42c.101.38.172.883.22 1.402l.01.104.022.26.008.104c.065.914.073 1.77.074 1.957v.075c-.001.194-.01 1.108-.082 2.06l-.008.105-.009.104c-.05.572-.124 1.14-.235 1.558a2.007 2.007 0 0 1-1.415 1.42c-1.16.312-5.569.334-6.18.335h-.142c-.309 0-1.587-.006-2.927-.052l-.17-.006-.087-.004-.171-.007-.171-.007c-1.11-.049-2.167-.128-2.654-.26a2.007 2.007 0 0 1-1.415-1.419c-.111-.417-.185-.986-.235-1.558L.09 9.82l-.008-.104A31.4 31.4 0 0 1 0 7.68v-.123c.002-.215.01-.958.064-1.778l.007-.103.003-.052.008-.104.022-.26.01-.104c.048-.519.119-1.023.22-1.402a2.007 2.007 0 0 1 1.415-1.42c.487-.13 1.544-.21 2.654-.26l.17-.007.172-.006.086-.003.171-.007A99.788 99.788 0 0 1 7.858 2h.193zM6.4 5.209v4.818l4.157-2.408L6.4 5.209z"/>
        </svg>
        </html>"""

        
st.markdown(insta,unsafe_allow_html=True)
st.markdown(yt,unsafe_allow_html=True)




st.write("Helpline: 0300 330 3311📞")


st.markdown(
    """
    <div class="icon-container">
      <a href="#" onclick="showAccount('instagram')"><img src="https://cdn4.iconfinder.com/data/icons/social-media-icons-the-circle-set/48/instagram_circle-512.png" width="30" height="30"></a>
      <a href="#" onclick="showAccount('whatsapp')"><img src="https://cdn4.iconfinder.com/data/icons/social-messaging-ui-color-shapes-2-free/128/social-whatsapp-circle-512.png" width="30" height="30"></a>
      <a href="#" onclick="showAccount('twitter')"><img src="https://cdn3.iconfinder.com/data/icons/social-icons-5/607/Twitterbird.png" width="30" height="30"></a>
      <a href="#" onclick="showAccount('mail')"><img src="https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/gmail-512.png" width="30" height="30"></a>
    </div>
    """,
    unsafe_allow_html=True
)




#test heart diesease calculator
#heart rate