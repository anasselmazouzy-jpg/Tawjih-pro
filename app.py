import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Tawjih Pro | Anas El Mazouri", layout="wide")

# 2. تصميم CSS احترافي (ألوان السماء والأبيض والأخضر)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Cairo', sans-serif; text-align: right; }
    
    .stApp {
        background: linear-gradient(135deg, #e3f2fd 0%, #ffffff 50%, #e8f5e9 100%);
    }
    
    .exam-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        border-right: 6px solid #2e7d32;
        margin-bottom: 15px;
    }

    .download-btn {
        display: inline-block;
        padding: 10px 20px;
        background-color: #2ecc71;
        color: white !important;
        text-decoration: none;
        border-radius: 25px;
        font-weight: bold;
        transition: 0.3s;
    }
    .download-btn:hover { background-color: #27ae60; transform: scale(1.05); }

    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #1a5276;
        color: white;
        text-align: center;
        padding: 8px;
        font-size: 14px;
        z-index: 100;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. شريط العنوان
st.markdown("<h1 style='text-align:center; color:#1a5276;'>🎓 منصة أناس المعزوري للتوجيه</h1>", unsafe_allow_html=True)

# 4. الأقسام
tab1, tab2, tab3 = st.tabs(["📚 تحميل الامتحانات (روابط حقيقية)", "🎯 محرك النقاط", "🤖 المساعد الذكي"])

with tab1:
    st.header("تحميل الامتحانات الوطنية (2008-2024)")
    st.image("https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=800", caption="الاستعداد هو مفتاح النجاح")
    
    col1, col2 = st.columns(2)
    with col1:
        shoba = st.selectbox("اختر المسلك:", ["علوم الحياة والأرض", "العلوم الفيزيائية", "الآداب", "العلوم الرياضية"])
    with col2:
        year = st.selectbox("اختر السنة:", list(range(2024, 2007, -1)))

    st.write(f"### امتحانات {shoba} لعام {year}")
    
    # مصفوفة تحاكي المواد مع روابط حقيقية (كمثال)
    # ملاحظة: يمكنك تغيير الروابط بروابط مباشرة من موقع moutamadris أو وزارة التربية
    materials = [
        {"name": "مادة الرياضيات", "link": "https://www.google.com/search?q=site:moutamadris.ma+امتحان+الرياضيات+" + str(year)},
        {"name": "مادة الفيزياء", "link": "https://www.google.com/search?q=site:moutamadris.ma+امتحان+الفيزياء+" + str(year)},
        {"name": "مادة الفلسفة", "link": "https://www.google.com/search?q=site:moutamadris.ma+امتحان+الفلسفة+" + str(year)}
    ]

    for mat in materials:
        st.markdown(f"""
        <div class="exam-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <a href="{mat['link']}" target="_blank" class="download-btn">اضغط هنا للتحميل (PDF)</a>
                <h4 style="margin:0;">{mat['name']}</h4>
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.header("حلل نقاطك مع أناس المعزوري")
    st.image("https://images.unsplash.com/photo-1541339907198-e08759df9a73?w=800")
    avg = st.number_input("أدخل معدلك العام المتوقع:", 10.0, 20.0, 14.0)
    if st.button("تحليل المسار الدراسى"):
        if avg >= 16: st.success("وجهتك: الطب أو الهندسة.")
        elif avg >= 13: st.info("وجهتك: ENCG أو FST.")
        else: st.warning("وجهتك: الكليات أو التكوين المهني.")

with tab3:
    st.header("الموجه الآلي الذكي")
    st.chat_message("assistant").write("أهلاً بك! أنا مساعد أناس المعزوري، كيف أساعدك اليوم؟")
    st.chat_input("اسألني عن أي شعبة...")

# 5. Footer بصمة المطور
st.markdown("""
    <div class='footer'>
        تم تطويره بواسطة المبرمج أناس المعزوري - Anas El Mazouri © 2026
    </div>
    """, unsafe_allow_html=True)
