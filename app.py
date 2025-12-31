import streamlit as st
import time

# 1. إعدادات الصفحة والألوان (أبيض، أزرق سماوي، أخضر)
st.set_page_config(page_title="توجيه برو - أرشيف الامتحانات", layout="wide")

st.markdown("""
    <style>
    /* خلفية الموقع بألوان السماء والنبات */
    .main {
        background: linear-gradient(135deg, #e0f7fa 0%, #ffffff 50%, #e8f5e9 100%);
    }
    .stApp { background: transparent; }
    
    /* تنسيق النصوص والقوائم */
    h1, h2, h3, p { color: #1a5276; text-align: right; font-family: 'Cairo', sans-serif; }
    
    /* تنسيق البطاقات (Cards) */
    .exam-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        border-bottom: 4px solid #2e7d32; /* لمسة خضراء */
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    
    /* تنسيق الأزرار */
    .stButton>button {
        background: linear-gradient(to right, #2980b9, #27ae60);
        color: white;
        border-radius: 25px;
        border: none;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 5px 15px rgba(0,0,0,0.2); }
    </style>
    """, unsafe_allow_html=True)

# 2. القائمة الجانبية
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🎓 Tawjih Pro</h2>", unsafe_allow_html=True)
    st.image("http://googleusercontent.com/image_collection/image_retrieval/14287485657387170816_0") # صورة طلاب
    menu = st.sidebar.selectbox("اختر الخدمة:", 
        ["📚 أرشيف امتحانات البكالوريا", "🎯 محرك التوجيه الذكي", "🤖 مساعد الطالب (AI)"])
    st.markdown("---")
    st.success("مرحباً بك! جميع الامتحانات من 2008 إلى 2024 متوفرة هنا.")

# 3. قسم أرشيف الامتحانات (2008 - 2024)
if menu == "📚 أرشيف امتحانات البكالوريا":
    st.title("📚 بنك الامتحانات الوطنية (2008 - 2024)")
    st.write("اختر المسلك والسنة لتحميل الامتحان مع التصحيح:")

    col1, col2, col3 = st.columns(3)
    with col1:
        track = st.selectbox("المسلك / الشعبة:", 
            ["علوم الحياة والأرض (SVT)", "العلوم الفيزيائية (PC)", "الآداب والعلوم الإنسانية", "العلوم الرياضية (SM)"])
    with col2:
        year = st.selectbox("السنة:", list(range(2024, 2007, -1)))
    with col3:
        session = st.radio("الدورة:", ["العادية", "الاستدراكية"])

    st.markdown("---")
    
    # عرض النتائج كبطاقات احترافية
    st.subheader(f"نتائج البحث: {track} - سنة {year}")
    
    # محاكاة لملفات الامتحانات
    exams = ["اللغة العربية", "الفلسفة", "اللغة الإنجليزية", "المادة الأساسية (تخصص)"]
    for exam in exams:
        with st.container():
            st.markdown(f"""
            <div class="exam-card">
                <h3 style='margin:0;'>📝 امتحان {exam}</h3>
                <p style='margin:5px 0;'>دورة {session} - ملف PDF جاهز للتحميل</p>
            </div>
            """, unsafe_allow_html=True)
            col_btn1, col_btn2 = st.columns([1, 4])
            with col_btn1:
                st.button(f"تحميل {exam}", key=exam+str(year))
    
    st.image("

http://googleusercontent.com/image_collection/image_retrieval/17079072951484124098_0
", caption="طلاب يراجعون في المكتبة")

# 4. قسم التوجيه بالنقاط
elif menu == "🎯 محرك التوجيه الذكي":
    st.title("🎯 تحليل المسار الدراسي")
    st.image("http://googleusercontent.com/image_collection/image_retrieval/6077781395330756265_0") # صورة جامعة
    st.write("أدخل نقاطك لنرشدك إلى الكلية أو المعهد المناسب:")
    
    avg = st.slider("معدل البكالوريا المتوقع:", 10.0, 20.0, 12.0)
    if st.button("تحليل مستقبلي"):
        if avg >= 16:
            st.balloons()
            st.success("معدلك يؤهلك لـ: كليات الطب، مدارس المهندسين (ENSA)، والأقسام التحضيرية.")
        elif avg >= 14:
            st.info("خياراتك المتاحة: ENCG، FST، ومعاهد التمريض (ISPITS).")
        else:
            st.warning("خياراتك المتاحة: EST، التكوين المهني المتخصص، وكليات العلوم والاقتصاد.")

# 5. المساعد الذكي
elif menu == "🤖 مساعد الطالب (AI)":
    st.title("🤖 الموجه الافتراضي")
    st.chat_message("assistant").write("أهلاً بك! أنا هنا لمساعدتك في الحصول على أي امتحان قديم أو نصيحة دراسية. ماذا تريد أن تعرف؟")
    input_text = st.chat_input("اكتب سؤالك هنا...")
