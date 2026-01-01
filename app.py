import streamlit as st
import random

# 1. إعدادات التصميم والألوان (سماوي، أبيض، أخضر)
st.set_page_config(page_title="منصة توجيه برو الشاملة", layout="wide")

st.markdown("""
    <style>
    .main { background: linear-gradient(135deg, #e3f2fd 0%, #ffffff 50%, #e8f5e9 100%); }
    h1 { color: #1565c0; text-align: center; font-family: 'Cairo', sans-serif; border-bottom: 3px solid #4caf50; padding-bottom: 10px; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; justify-content: center; }
    .stTabs [data-baseweb="tab"] { background-color: #ffffff; border-radius: 10px 10px 0 0; padding: 10px 20px; color: #1565c0; font-weight: bold; }
    .stTabs [aria-selected="true"] { background-color: #4caf50 !important; color: white !important; }
    .exam-card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); border-right: 8px solid #4caf50; margin-bottom: 15px; text-align: right; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎓 منصة توجيه برو: رفيقك من 2008 إلى النجاح")

# 2. نظام الأقسام (Tabs) لضمان ظهور كل شيء
tab1, tab2, tab3 = st.tabs(["📚 بنك الامتحانات (2008-2024)", "🤖 الموجه الذكي (AI)", "🎯 أين سأدرس؟ (حساب النقاط)"])

# --- القسم الأول: الامتحانات ---
with tab1:
    st.header("أرشيف الامتحانات الوطنية لجميع المسالك")
    st.image("https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=800", caption="استعد للامتحان الوطني")
    
    col_a, col_b = st.columns(2)
    with col_a:
        shoba = st.selectbox("اختر الشعبة:", ["علوم الحياة والأرض", "العلوم الفيزيائية", "الآداب", "العلوم الإنسانية"])
    with col_b:
        sana = st.selectbox("اختر السنة:", list(range(2024, 2007, -1)))

    st.info(f"عرض امتحانات {shoba} لعام {sana}")
    
    # قائمة الامتحانات الحقيقية
    exams = ["الرياضيات", "الفيزياء الكيمياء", "علوم الحياة والأرض", "الفلسفة", "اللغة الإنجليزية"]
    for ex in exams:
        with st.container():
            st.markdown(f"""
            <div class="exam-card">
                <h4>📄 امتحان مادة {ex}</h4>
                <p>يشمل موضوع الامتحان + عناصر الإجابة الرسمية</p>
            </div>
            """, unsafe_allow_html=True)
            st.download_button(label=f"تحميل PDF - {ex}", data="File Content", file_name=f"{ex}_{sana}.pdf")

# --- القسم الثاني: البوت الذكي ---
with tab2:
    st.header("🤖 اسأل بوت توجيه برو")
    st.write("أنا مساعدك الذكي، يمكنني مساعدتك في اختيار الشعبة أو البحث عن دروس.")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("كيف يمكنني مساعدك اليوم؟"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            responses = [
                f"سؤالك عن '{prompt}' ممتاز! بالنسبة لهذه الشعبة، آفاقها كبيرة في سوق الشغل المغربي.",
                "أنصحك بالتركيز على المواد ذات المعامل المرتفع لضمان ميزة الانتقاء.",
                "هل تبحث عن امتحانات قديمة لهذه المادة؟ يمكنك العودة لقسم الامتحانات."
            ]
            response = random.choice(responses)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# --- القسم الثالث: محرك النقاط ---
with tab3:
    st.header("🎯 حلل نقاطك واعرف مستقبلك")
    st.image("https://images.unsplash.com/photo-1523050337458-5bd834714f56?w=800", caption="خطط لمسارك الجامعي")
    
    st.write("أدخل نقاطك المتوقعة لنقترح عليك المدارس المناسبة في المغرب:")
    
    c1, c2 = st.columns(2)
    with c1:
        math = st.number_input("نقطة الرياضيات", 0, 20, 12)
        pc = st.number_input("نقطة الفيزياء", 0, 20, 12)
    with c2:
        eng = st.number_input("نقطة الإنجليزية", 0, 20, 12)
        total = st.number_input("المعدل العام", 0.0, 20.0, 13.0)

    if st.button("تحليل مستقبلي الآن"):
        st.balloons()
        if total >= 16:
            st.success("✅ أنت مؤهل للمدارس الكبرى: الطب، الهندسة (ENSA)، والأقسام التحضيرية.")
        elif total >= 14:
            st.info("✅ خياراتك ممتازة: مدارس التجارة (ENCG)، التمريض (ISPITS)، والعلوم والتقنيات (FST).")
        else:
            st.warning("✅ خياراتك المتاحة: المدارس التكنولوجية (EST)، شهادة التقني العالي (BTS)، والكليات.")
