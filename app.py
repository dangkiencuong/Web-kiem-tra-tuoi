import streamlit as st

st.title("Web Kiểm Tra Độ Tuổi tuất")

tuoi = st.number_input("Nhập tuổi của bạn vào đây:", min_value=1, max_value=100, value=18)

if st.button("Kiểm tra ngay"):
    if tuoi >= 18:
        st.success("Bạn đã đủ 18 tuổi, được phép xem phim xes!")
    else:
        st.error("Bạn chưa đủ 18 tuổi, hãy quay lại sau nhé!")
