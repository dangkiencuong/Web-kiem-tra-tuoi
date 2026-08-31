import streamlit as st

st.title("Tra Cuu Truong Trung Tuyen")

# Nhập tổng điểm thi
diem = st.number_input("Nhap diem cua ban:", min_value=0.0, max_value=40.0, value=19.0)

if st.button("Kiem tra ngay"):
    st.write("---")
    st.subheader("Ket qua xet tuyen:")
    
    # 1. Trường điểm cao nhất
    if diem >= 19.25:
        st.success("Ban du diem do truong: Thanh Oai B (Moc 19.25)")
        
    # 2. Trường điểm tiếp theo
    if diem >= 16.5:
        st.success("Ban du diem do truong: Thanh Oai A (Moc 16.5)")
        
    # 3. Trường điểm tiếp theo
    if diem >= 15.25:
        st.success("Ban du diem do truong: Ly Tu Tan (Moc 15.25)")
        
    # 4. Trường điểm sàn
    if diem >= 8.0:
        st.success("Ban du diem do truong: Thanh Xuan (Moc 8.0)")
        
    # 5. Dưới mốc sàn -> Báo rớt
    if diem < 8.0:
        st.error("Diem cua ban chua du do truong nao trong danh sach.")
        
