import streamlit as st

st.set_page_config(page_title="3D Ad Generator", layout="centered")

# تعديل اتجاه النص ودعم اللغة العربية مع الـ 3D بشكل صحيح
st.markdown("""
    <div style="direction: rtl; text-align: right;">
        <h1 style="color: #31333F;">منصة توليد إعلانات الـ 3D بالذكاء الاصطناعي</h1>
        <p style="color: #31333F; font-size: 18px;">أدخل فكرة إعلانك لتوليد السيناريو والمشاهد تلقائياً.</p>
    </div>
""", unsafe_allow_html=True)

idea = st.text_area("فكرة الإعلان:", placeholder="مثال: إعلان عصير ليمون منعش في أجواء صيفية استوائية...")
style = st.selectbox("النمط البصري:", ["واقعي (Realistic)", "سينمائي (Cinematic)", "كرتوني (3D Cartoon)"])
duration = st.slider("المدة التقريبية (ثوانٍ):", min_value=5, max_value=30, value=15)

if st.button("إنشاء الإعلان"):
    if idea:
        with st.spinner("جاري تحليل الفكرة وتوليد السيناريو والأصول..."):
            st.markdown('<div style="direction: rtl; text-align: right;">', unsafe_allow_html=True)
            st.subheader("1. السيناريو المُولد:")
            st.write("مشهد 1: لقطة واسعة لشاطئ مشمس مع زجاجة عصير باردة تتصاعد منها قطرات الماء.")
            st.write("مشهد 2: حركة سريعة للكاميرا تقترب من الشعار.")
            
            st.subheader("2. الأصول ثلاثية الأبعاد:")
            st.write("تم استدعاء مجسم زجاجة العصير بنجاح.")
            
            st.success("تم الانتهاء من إعداد خط الإنتاج المبدئي!")
            st.info("لجعل الرابط ينتج فيديوهات حقيقية، قم بربط هذا الملف بمفاتيح الـ API الخاصة بك.")
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("يرجى كتابة فكرة الإعلان أولاً.")
        
