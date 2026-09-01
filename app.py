import streamlit as st

st.title("Tra Cứu Trường Trúng Tuyển,(đừng tin)")

# Nhập tổng điểm thi
diem = st.number_input("Nhập điểm của bạn:", min_value=0.0, max_value=40.0, value=19.0)

if st.button("Kiểm tra ngay"):
    st.write("---")
    st.subheader("Kết quả xét tuyển:")
    
    # 1. Trường điểm cao nhất
    if diem >= 19.25:
        st.success("Bạn đủ điểm đỗ trường: Thanh Oai B (Mốc 19.25)")
        
    # 2. Trường điểm tiếp theo
    if diem >= 16.5:
        st.success("Bạn đủ điểm đỗ trường: Thanh Oai A (Mốc 16.5)")
        
    # 3. Trường điểm tiếp theo
    if diem >= 15.25:
        st.success("Bạn đủ điểm đỗ trường: Lý Tự Tấn (Mốc 15.25)")
        
    # 4. Trường điểm tiếp theo
    if diem >= 11.0:
        st.success("bạn đủ điểm đỗ trường: Lưu Hoàng (Mốc 11.0)")
        
    # 5. Trường điểm sàn
    if diem >= 8.0:
        st.success("Bạn đủ điểm đỗ trường: Thanh Xuân (Mốc 8.0)")
        
    # 6. Dưới mốc sàn -> Báo rớt
    if diem < 8.0:
        st.error("Điểm của bạn chưa đủ cho trường nào trong danh sách.")
        

# Thông tin bản quyền
st.sidebar.title("📌 Thông tin tác giả")
st.sidebar.info("Được thiết kế và phát triển bởi: **Đặng Kiên Cường**")
st.sidebar.write("---")

# Dưới chân trang web (Footer)
st.write("---")
st.caption("© 2026 Designed & name by Dang Kien Cuong. All rights reserved.")
