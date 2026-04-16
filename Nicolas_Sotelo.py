import streamlit as st
import os
from PIL import Image

# 1. Configuración de la página y Sidebar
st.set_page_config(page_title="David Sotelo | Portfolio", layout="wide")

# --- SIDEBAR ---
with st.sidebar:
    st.title("📍 Contact Info")
    st.markdown("""
    - 📧[nicolassotelo1026@gmail.com](mailto:nicolassotelo1026@gmail.com)
    - 🔗[linkedin.com/in/nicolas-sotelo26](https://www.linkedin.com/in/nicolas-sotelo26)
    - 💻[github.com/nico1026](https://github.com/nico1026)
    """)
    #st.divider()
    # Botón para descargar CV (Simulado)
    #st.download_button(label="📄 Download Full CV", data="Contenido del CV", file_name="David_Sotelo_CV.pdf")

# --- ESTILO CSS PERSONALIZADO ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    stSubheader {
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. ENCABEZADO PRINCIPAL
st.title('I am :green[David Nicolas Sotelo Merchán]', text_alignment="center")
st.header('⚙️ Mechanical Engineering | 📊 Data Science',text_alignment="center")
st.divider()

# 3. IMAGEN Y SKILLS
base_dir = os.path.dirname(__file__)
ruta = os.path.join(base_dir, "images", "david_sotelo.jpg")
image = Image.open(ruta)

col_left, col_mid, col_right = st.columns([2, 0.8, 2])

with col_left:
    st.markdown("<br><br>", unsafe_allow_html=True) # Espaciador
    # Usamos HTML para centrar el título y la lista
    st.markdown("""
        <div style="text-align: center;">
            <h3 style="color: orange;">💻 <b>Skills</b></h3>
            <p><b>Programming:</b><br>Python, R, JavaScript, Excel (VBA)</p>
            <p><b>CAD/CAE:</b><br>Inventor (Nastran), ANSYS (Fluent)</p>
            <p><b>3D Printing & Design (entrepreneurship) :</b><br>Fusion 360, Orca Slicer</p>
        </div>
    """, unsafe_allow_html=True)

with col_mid:
    st.image(image, use_container_width=True)

with col_right:
    st.markdown("<br><br>", unsafe_allow_html=True) # Espaciador
    # Usamos HTML para centrar el contenido de idiomas
    st.markdown("""
        <div style="text-align: center;">
            <h3 style="color: orange;">🌐 <b>Languages</b></h3>
            <p><b>English:</b><br>Advanced</p>
            <p><b>French:</b><br>Basic (In progress)</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style="
        background-color: #E3FAEC; 
        color: #003B1E; 
        padding: 15px; 
        border-radius: 10px; 
        text-align: center;
        border: 1px solid #E3FAEC;
        font-size: 16px;
        font-weight: 500;
    ">
         ✅ Continuous learner in Data Science & Engineering.
    </div>
""", unsafe_allow_html=True)

st.divider()

st.text("I’m David Nicolas Sotelo Merchan, a Mechanical Engineer focused on the design, modeling, and optimization of engineering systems, " \
"integrating strong foundations in mechanics and thermodynamics with programming, advanced analytics, and statistical modeling. I combine experience in Python," \
" process automation, and the application of machine learning models to support data-driven technical decision-making. " \
"I have worked with CAD/CAE simulation and computational analysis to solve complex problems, bringing an interdisciplinary perspective that bridges engineering and data science." \
" Currently pursuing a Master’s degree in Data Science, I aim to integrate advanced analytics into engineering solutions. " \
"Additionally, I have experience in industrial inspection using Non-Destructive Testing (NDT), which strengthens my ability to work with real-world industrial data. " \
"I am characterized by strong analytical thinking, attention to detail, effective technical communication, and a self-taught mindset oriented toward continuous improvement."
,text_alignment="justify")

st.divider()

# 5. EDUCATION & AWARDS
col1, col2 = st.columns(2)
with col1:
    st.subheader('🎓 :blue[Education]')
    st.markdown("""
    **M.Sc. in Data Science** *University Colombian School of Engineering Julio Garavito*  
    <span style="color:gray;">Jan 2026 – Present</span>
    
    <br>
    
    **B.Sc. in Mechanical Engineering** *University Colombian School of Engineering Julio Garavito*  
    <span style="color:gray;">Jan 2020 – Aug 2025</span>
    """, unsafe_allow_html=True)

with col2:
    st.subheader("🏆 :blue[Honors & Awards]")
    st.markdown("""
    **Academic Excellence Scholarship (Data Science)** *Second Highest GPA (4.23)*  
    University Colombian School of Engineering Julio Garavito  
    <span style="color:gray;">2025-2</span>
    
    **Academic Excellence Scholarship** *Top GPA*  
    University Colombian School of Engineering Julio Garavito  
    <span style="color:gray;">2022</span>
    
    **DSIM Research Group** *Fluid dynamics study of intake manifolds for racing engines*  
    University Colombian School of Engineering Julio Garavito             
     <span style="color:gray;">(2023 – 2024)</span>
    """, unsafe_allow_html=True)

st.divider()

# 6. WORK EXPERIENCE
st.subheader("⚙️💼 :yellow[Work Experience]")
exp_tab1, exp_tab2 = st.tabs(["Inspection Engineer", "Engineering Intern"])

with exp_tab1:
    st.markdown("### **Integrity NDT** | `Nov 2025 – Apr 2026`")
    st.write(f'<div style="text-align: justify;">'
         f'Responsible for analyzing and interpreting ultrasonic inspection data to characterize discontinuities and assess material integrity. '
         f'Perform calibration and verification of UT and PAUT equipment, thickness measurements, and application of advanced techniques '
         f'(PAUT and TFM) under Level III supervision. Experienced in field inspections at the Cartagena Refinery, executing PAUT '
         f'examinations on in-service high-temperature piping within critical industrial environments. Contribute to the development and '
         f'updating of NDT procedures in compliance with applicable standards, and design inspection tools through 3D modeling and '
         f'additive manufacturing to improve operational efficiency.'
         f'</div>', unsafe_allow_html=True)


with exp_tab2:
    st.markdown("### **NYS / Yazaki Ciemel S.A.** | `Jan 2025 – Jul 2025`")
    st.write(f'<div style="text-align: justify;">'
         f'Supported production process optimization through modeling and data analysis, including automation of workflow tools using '
         f'Excel VBA. Participated in tool design and simulation using Autodesk Inventor and contributed to production line improvements '
         f'through motion analysis. Additionally supported continuous improvement initiatives through Kaizen and Jishuken methodologies.'
         f'</div>', unsafe_allow_html=True)
st.divider()

# 7. BEYOND THE CODE
st.subheader("🎉 :rainbow[Beyond the Code & CAD]")
tab1, tab2 = st.tabs(['Summer Lifeguard Era', 'Hobbies'])

with tab1:
    st.subheader('☀️ :rainbow[Summer Lifeguard Era]')
    st.markdown('''During the summers of 2023 and 2024, I traded my CAD simulations and Python scripts for a whistle and some sunscreen. I headed to the US to work as a lifeguard at a theme park. It wasn't just about watching pools; it was a deep dive into new cultures and making friends from all over the world. My English went from "textbook mode" to "real-world fluent" while I was busy making sure the only thing "dropping" at the park were the roller coasters, not the guests!''')
    col3, col4 = st.columns(2)
    with col3:
        st.image(os.path.join(base_dir, "images", "pipe.jpg"), use_container_width=True)


    with col4:
        # Asegúrate de que esta ruta sea correcta
        st.image(os.path.join(base_dir, "images", "kd.jpg"), use_container_width=True)

with tab2:
    col5,col6 =st.columns(2)
    with col5:
        st.subheader('⚽ :rainbow[Balancing the System]')
        # Texto justificado con HTML
        st.write(f'''
            <div style="text-align: justify;">
            When I’m not designing and interpreting engineering drawings, debugging code, 
            or analyzing engine components, you’ll find me running my own physical 
            "stress tests" at the gym or on the football pitch. I’m a total sports 
            data-miner—whether it’s NBA, MLB, NFL, or Football, if there’s a scoreboard 
            and a strategy, I’m watching it. To recharge, I dive into video games, 
            travel the world to collect new experiences, and explore international cuisines. 
            Basically, I’m a foodie who travels for the views and stays for the flavors, 
            always making sure my family is part of the "core team" along the way.
            </div>
            <br>
        ''', unsafe_allow_html=True)
        
        base_dir3 = os.path.dirname(__file__)
        ruta3 = os.path.join(base_dir3, "images", "gym.jpg")
        image3 = Image.open(ruta3)
        st.image(image3, use_container_width=True) # Recomendado usar el ancho del contenedor

    with col6:
        st.subheader('🏎️ :rainbow[High-Octane Passions & Low-Stress Vibes]')
        # Texto justificado con HTML
        st.write(f'''
            <div style="text-align: justify;">
            My heart beats at 15,000 RPM. I’m obsessed with Formula 1, high-performance 
            engines, and the pure physics of speed—it’s where my mechanical engineering 
            background meets my adrenaline-junkie side. But it’s not all fast-paced; 
            I also enjoy the "steady state" of life: getting lost in a good series, 
            discovering new music, and the intellectual challenge of learning new languages. 
            I believe in working hard on complex problems but living life with a 
            "tranquilo" mindset—high speed on the track, high peace at home.
            </div>
            <br>
        ''', unsafe_allow_html=True)
        
        base_dir4 = os.path.dirname(__file__)
        ruta4 = os.path.join(base_dir4, "images", "car.jpg")
        image4 = Image.open(ruta4)
        st.image(image4, use_container_width=True)