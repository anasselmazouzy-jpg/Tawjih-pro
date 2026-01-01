import streamlit as st
from datetime import datetime

# 1. إعدادات الصفحة
st.set_page_config(page_title="منصة توجيه برو", page_icon="🎓", layout="wide")

# 2. تصميم CSS احترافي متوافق مع Dark Mode و Light Mode
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    /* تثبيت الخطوط والألوان لتعمل في كل الأوضاع */
    html, body, [class*="st-"] { 
        font-family: 'Cairo', sans-serif; 
        text-align: right; 
    }
    
    /* خلفية ثابتة لا تتغير بالوضع الليلي لضمان وضوح الألوان */
    .stApp {
        background: linear-gradient(180deg, #e3f2fd 0%, #ffffff 100%) !important;
    }

    /* تثبيت لون العناوين والنصوص لتبقى واضحة (داكنة) */
    h1, h2, h3, h4, p, span, label {
        color: #1a5276 !important;
    }

    .main-title {
        color: #1a5276;
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        padding: 10px;
        border-bottom: 3px solid #4caf50;
    }

    /* عداد الوقت التنازلي */
    .timer-box {
        background-color: #fdf2f2;
        border: 2px solid #ef4444;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        margin: 20px 0;
    }
    .timer-text { color: #dc2626 !important; font-size: 20px; font-weight: bold; }

    .exam-card {
        background: white !important;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border-right: 8px solid #4caf50;
        margin-bottom: 20px;
    }

    .btn-download {
        display: inline-block;
        padding: 10px 20px;
        background: #27ae60;
        color: white !important;
        text-decoration: none;
        border-radius: 25px;
        font-weight: bold;
    }

    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #1a5276;
        color: white !important;
        text-align: center;
        padding: 5px;
        font-size: 14px;
        z-index: 100;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. حساب العداد التنازلي للامتحان الوطني (مثال: 10 يونيو 2026)
exam_date = datetime(2026, 6, 10)
now = datetime.now()
delta = exam_date - now
days_left = delta.days

# 4. واجهة الموقع
st.markdown("<div class='main-title'>🎓 منصة توجيه برو</div>", unsafe_allow_html=True)

# عرض العداد التنازلي
if days_left > 0:
    st.markdown(f"""
    <div class='timer-box'>
        <span class='timer-text'>⏳ متبقي {days_left} يوم على الامتحان الوطني 2026</span>
    </div>
    """, unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📚 الأرشيف (2008-2024)", "🎯 محرك التوجيه", "🤖 المساعد الذكي"])

with tab1:
    st.image("https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=800")
    col1, col2 = st.columns(2)
    with col1:
        shoba = st.selectbox("المسلك:", ["SVT", "PC", "آداب", "رياضية"])
    with col2:
        year = st.selectbox("السنة:", list(range(2024, 2007, -1)))

    # قائمة مواد
    subjects = ["الرياضيات", "الفيزياء", "الفلسفة"]
    for s in subjects:
        st.markdown(f"""
        <div class='exam-card'>
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <a href='https://www.google.com/search?q=pdf+امتحان+{s}+{shoba}+{year}' target='_blank' class='btn-download'>تحميل PDF</a>
                <h4 style='margin:0;'>{s}</h4>
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.header("🎯 حساب النقاط")
    avg = st.number_input("المعدل العام:", 10.0, 20.0, 13.0)
    if st.button("حلل مستقبلي"):
        st.success("تم التحليل بنجاح!")

with tab3:
    st.header("🤖 المساعد الذكي")
    st.chat_message("assistant").write("أهلاً بك! أنا مساعد أناس المعزوري، كيف أساعدك؟")

# 5. Footer (بصمة أناس المعزوري)
st.markdown(f"""
    <div class='footer'>
        🚀 تم تطوير المنصة بواسطة المبرمج أناس المعزوري © {now.year}
    </div>
    """, unsafe_allow_html=True)
