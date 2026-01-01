import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="منصة توجيه برو", page_icon="🎓", layout="wide")

# 2. تصميم CSS احترافي (ألوان السماء، الأبيض، والأخضر)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Cairo', sans-serif; text-align: right; }
    
    /* خلفية متدرجة بألوان السماء */
    .stApp {
        background: linear-gradient(180deg, #e3f2fd 0%, #ffffff 100%);
    }
    
    /* تنسيق العنوان الرئيسي */
    .main-title {
        color: #1a5276;
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        padding: 20px;
        border-bottom: 2px solid #4caf50;
        margin-bottom: 30px;
    }

    /* بطاقات الامتحانات */
    .exam-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border-right: 8px solid #4caf50;
        margin-bottom: 20px;
        transition: 0.3s;
    }
    .exam-card:hover { transform: translateY(-5px); }

    /* أزرار التحميل */
    .btn-download {
        display: inline-block;
        padding: 12px 25px;
        background: linear-gradient(45deg, #2ecc71, #27ae60);
        color: white !important;
        text-decoration: none;
        border-radius: 30px;
        font-weight: bold;
        text-align: center;
    }

    /* شريط المطور في الأسفل */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: rgba(26, 82, 118, 0.9);
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        backdrop-filter: blur(5px);
        z-index: 100;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. العنوان الرئيسي للمنصة
st.markdown("<div class='main-title'>🎓 منصة توجيه برو</div>", unsafe_allow_html=True)

# 4. الأقسام الرئيسية (Tabs)
tab1, tab2, tab3 = st.tabs(["📚 أرشيف الامتحانات (2008-2024)", "🎯 حساب النقاط والتوجيه", "🤖 المساعد الذكي"])

with tab1:
    st.header("تحميل الامتحانات الوطنية الشاملة")
    st.image("https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=800", caption="طريقك نحو التميز الدراسي")
    
    c1, c2 = st.columns(2)
    with c1:
        shoba = st.selectbox("اختر الشعبة:", ["علوم الحياة والأرض", "العلوم الفيزيائية", "الآداب", "العلوم الرياضية"])
    with c2:
        year = st.selectbox("اختر السنة:", list(range(2024, 2007, -1)))

    st.subheader(f"امتحانات {shoba} - دورة {year}")
    
    # قائمة المواد مع روابط بحث مباشرة لضمان الوصول للملفات
    materials = ["الرياضيات", "الفيزياء", "الفلسفة", "اللغة الإنجليزية"]
    
    for mat in materials:
        search_url = f"https://www.google.com/search?q=site:moutamadris.ma+امتحان+{mat}+{shoba}+{year}+pdf"
        st.markdown(f"""
        <div class='exam-card'>
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <a href='{search_url}' target='_blank' class='btn-download'>🔗 فتح رابط التحميل المباشر</a>
                <h4 style='margin:0;'>مادة {mat}</h4>
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.header("🎯 أين سأدرس بعد البكالوريا؟")
    st.image("https://images.unsplash.com/photo-1541339907198-e08759df9a73?w=800")
    score = st.slider("أدخل معدلك العام المتوقع:", 10.0, 20.0, 13.0)
    if st.button("تحليل المسار"):
        if score >= 16: st.success("خياراتك الكبرى: الطب، الهندسة (ENSA)، الأقسام التحضيرية.")
        elif score >= 13: st.info("خياراتك الجيدة: ENCG، FST، معاهد التمريض (ISPITS).")
        else: st.warning("خياراتك المتاحة: المدارس التكنولوجية (EST)، التكوين المهني، والكليات.")

with tab3:
    st.header("🤖 المساعد الذكي للمنصة")
    st.chat_message("assistant").write("أهلاً بك في منصة توجيه برو! أنا هنا للإجابة على تساؤلاتك حول الامتحانات أو التوجيه.")
    st.chat_input("اكتب سؤالك هنا...")

# 5. شريط المطور (بصمة أناس المعزوري)
st.markdown("""
    <div class='footer'>
        🚀 تم تطوير هذا الموقع بواسطة المبرمج: أناس المعزوري © 2026
    </div>
    """, unsafe_allow_html=True)
