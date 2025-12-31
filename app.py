import streamlit as st
import streamlit.components.v1 as components 

# إعداد الصفحة
st.set_page_config(page_title="توجيه برو", layout="centered") 

# الكود الاحترافي الذي طلبته (HTML + JS)
html_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
        body { font-family: 'Cairo', sans-serif; background-color: #f0f2f5; display: flex; justify-content: center; padding-top: 20px; }
        .card { background: white; width: 100%; max-width: 400px; padding: 2rem; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); text-align: center; }
        .logo-img { width: 100px; height: 100px; border-radius: 50%; border: 3px solid #007bff; margin-bottom: 10px; }
        input { width: 100%; padding: 12px; margin: 10px 0; border: 2px solid #e1e1e1; border-radius: 10px; box-sizing: border-box; }
        .btn { background: #007bff; color: white; border: none; padding: 15px; width: 100%; border-radius: 10px; font-weight: bold; cursor: pointer; }
        .error { color: #dc3545; font-size: 0.8rem; display: none; margin-bottom: 10px; }
    </style>
</head>
<body>
    <div class="card">
        <img src="https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=200" class="logo-img">
        <h2>توجيه برو</h2>
        <input type="email" id="email" placeholder="البريد الإلكتروني (Gmail)">
        <div id="emailErr" class="error">⚠️ يجب إدخال Gmail صحيح للمتابعة</div>
        
        <div id="phoneBox" style="display:none">
            <input type="tel" id="phone" placeholder="رقم الهاتف">
            <div id="phoneErr" class="error">⚠️ يرجى إدخال رقم الهاتف</div>
        </div>
        
        <button class="btn" onclick="check()">متابعة</button>
    </div> 

    <script>
        function check() {
            const email = document.getElementById('email').value;
            const phoneBox = document.getElementById('phoneBox');
            const phone = document.getElementById('phone').value; 

            if (!email.includes('@')) {
                document.getElementById('emailErr').style.display = 'block';
            } else {
                document.getElementById('emailErr').style.display = 'none';
                phoneBox.style.display = 'block';
                if (phoneBox.style.display === 'block' && phone.length < 8) {
                    document.getElementById('phoneErr').style.display = 'block';
                } else if (phone.length >= 8) {
                    alert("تم التسجيل بنجاح في توجيه برو!");
                }
            }
        }
    </script>
</body>
</html>
""" 

# تشغيل الكود داخل Streamlit
components.html(html_code, height=600)
