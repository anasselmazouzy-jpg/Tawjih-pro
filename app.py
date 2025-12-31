import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="توجيه برو | منصة الطالب الذكية", layout="wide")

# تصميم CSS احترافي
st.markdown("""
    <style>
    .main { background-color: #f0f2f5; }
    .stButton>button { width: 100%; border-radius: 12px; background: linear-gradient(45deg, #007bff, #0056b3); color: white; height: 50px; font-weight: bold; border: none; }
    .result-card { padding: 20px; border-radius: 15px; background-color: white; border-right: 6px solid #28a745; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
    .exam-box { padding: 25px; border-radius: 15px; background-color: white; border-right: 6px solid #007bff; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
    h1, h2, h3 { color: #1e3a8a; text-align: right; font-family: 'Cairo', sans-serif; }
    .timer { font-size: 24px; font-weight: bold; color: #dc3545; text-align: center; border: 2px solid #dc3545; border-radius: 12px; padding: 10px; background: #fff5f5; }
    </style>
    """, unsafe_allow_html=True)

# القائمة الجانبية للتنقل
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=200", width=100)
    st.title("توجيه برو")
    st.markdown("---")
    choice = st.radio("اختر القسم:", [
        "🎯 أين يمكنني الدراسة؟ (حساب النقاط)",
        "🤖 مساعدك الذكي (AI Tutor)", 
        "📝 مراجعة امتحانات البكالوريا", 
        "📊 مساري الدراسي"
    ])

# 1. قسم التوجيه بناءً على النقاط (جديد)
if choice == "🎯 أين يمكنني الدراسة؟ (حساب النقاط)":
    st.title("🎯 محرك التوجيه الذكي")
    st.write("أدخل معدلاتك التقديرية لنقترح عليك أفضل الآفاق الدراسية بعد البكالوريا:")
    
    col1, col2 = st.columns(2)
    with col1:
        math = st.number_input("نقطة الرياضيات:", 0.0, 20.0, 10.0)
        physics = st.number_input("نقطة الفيزياء:", 0.0, 20.0, 10.0)
    with col2:
        english = st.number_input("نقطة الإنجليزية:", 0.0, 20.0, 10.0)
        average = st.number_input("المعدل العام المتوقع:", 0.0, 20.0, 10.0)

    if st.button("تحليل الفرص المتاحة"):
        st.subheader("المدارس المقترحة لك:")
        
        if average >= 16:
            st.markdown("<div class='result-card'>✅ <b>كليات الطب والصيدلة (FMP):</b> معدلك ممتاز ويؤهلك لاجتياز المباراة.</div>", unsafe_allow_html=True)
            st.markdown("<div class='result-card'>✅ <b>مدارس المهندسين (ENSA/ENSAM):</b> لديك حظوظ قوية جداً.</div>", unsafe_allow_html=True)
        elif average >= 14:
            st.markdown("<div class='result-card'>✅ <b>مدارس التجارة والتسيير (ENCG):</b> اختيار ممتاز لمعدلك.</div>", unsafe_allow_html=True)
            st.markdown("<div class='result-card'>✅ <b>الأقسام التحضيرية (CPGE):</b> يمكنك المنافسة في التخصصات العلمية أو التقنية.</div>", unsafe_allow_html=True)
        elif average >= 12:
            st.markdown("<div class='result-card'>✅ <b>كليات العلوم والتقنيات (FST):</b> تخصصات تقنية مطلوبة جداً.</div>", unsafe_allow_html=True)
            st.markdown("<div class='result-card'>✅ <b>المعاهد العليا للمهن التمريضية (ISPITS):</b> خيار جيد جداً.</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='result-card'>✅ <b>التكوين المهني (OFPPT) أو الكليات ذات الاستقطاب المفتوح:</b> يمكنك التخصص في مجالات واعدة.</div>", unsafe_allow_html=True)

# 2. قسم البوت الذكي
elif choice == "🤖 مساعدك الذكي (AI Tutor)":
    st.title("🤖 اسأل الموجه الذكي")
    st.write("اطرح أي سؤال حول التخصصات أو المواد الدراسية:")
    user_question = st.text_input("مثال: ما هي آفاق شعبة العلوم الرياضية؟")
    if user_question:
        with st.spinner('جاري التحليل...'):
            time.sleep(1)
            st.info(f"نصيحة توجيه برو: سؤالك حول '{user_question}' مهم جداً. بشكل عام، ننصحك بالاطلاع على 'دليل الطالب' وتركيز مجهودك على المواد ذات المعامل الأكبر في شعبتك.")

# 3. قسم الامتحانات (مع تحسين المحتوى)
elif choice == "📝 مراجعة امتحانات البكالوريا":
    st.title("📝 منصة التدريب على الامتحانات")
    
    # عداد تنازلي حقيقي
    if 'start_time' not in st.session_state: st.session_state.start_time = time.time()
    remaining = max(3600 - int(time.time() - st.session_state.start_time), 0)
    mins, secs = divmod(remaining, 60)
    st.markdown(f"<div class='timer'>⏳ الوقت المتبقي: {mins:02d}:{secs:02d}</div>", unsafe_allow_html=True)

    st.write("---")
    st.subheader("نموذج امتحان الفلسفة (مفهوم الشخص)")
    st.markdown("<div class='exam-box'>", unsafe_allow_html=True)
    q1 = st.radio("السؤال: هل هوية الشخص تقوم على الذاكرة أم الإرادة حسب 'أرتور شوبنهاور'؟", 
                 ["الذاكرة", "الإرادة", "الشكل الخارجي"])
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("تصحيح الإجابة"):
        if q1 == "الإرادة":
            st.success("إجابة صحيحة! يرى شوبنهاور أن الإرادة هي نواة كينونة الإنسان.")
        else:
            st.error("إجابة خاطئة. شوبنهاور يركز على 'الإرادة' كأصل لهوية الشخص.")

# 4. قسم مساري الدراسي
elif choice == "📊 مساري الدراسي":
    st.title("📊 تتبع تطورك الدراسي")
    st.write("هنا تظهر إحصائياتك بناءً على الامتحانات التي قمت بحلها في الموقع.")
    st.progress(45, text="مستوى الاستعداد الحالي: 45%")
