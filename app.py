import streamlit as st
import time

st.title("Tra Cứu Trường Trúng Tuyển,(đừng tin)")

# Nhập tổng điểm thi
diem = st.number_input("Nhập điểm của bạn:", min_value=0.0, max_value=40.0, value=19.0)

if st.button("Kiểm tra ngay"):
    st.write("---")
    st.subheader("Kết quả xét tuyển:")
    
# dòng này để tron nhé:
    khung_hinh = st.empty()
    time.sleep(5)
    khung_hinh.image("https://i.imgur.com/gK9J27P.jpeg", caption="https://i.postimg.cc/Bn20CrZj/phat-png.webp")
    
    
    # 1. Trường điểm cao nhất
    if diem >= 19.25:
        st.balloons()
        st.success("Bạn đủ điểm đỗ trường: Thanh Oai B (Mốc 19.25)")
    # Hiệu ứng vui rơi khi trúng tuyển
        st.markdown(
            """
            <style>
            @keyframes happy-fall {
                0% { top: -10%; opacity: 0; transform: rotate(0deg); }
                10% { opacity: 1; }
                90% { opacity: 1; }
                100% { top: 110%; opacity: 0; transform: rotate(360deg); }
            }
            .happy-emoji {
                position: fixed; font-size: 2rem;
                animation: happy-fall 6s linear infinite;
                z-index: 9999; pointer-events: none;
            }
            </style>
            <div class="happy-emoji" style="left: 15%; animation-delay: 0s;">🥳</div>
            <div class="happy-emoji" style="left: 35%; animation-delay: 1.2s;">🎉</div>
            <div class="happy-emoji" style="left: 55%; animation-delay: 0.5s;">🥳</div>
            <div class="happy-emoji" style="left: 75%; animation-delay: 2s;">✨</div>
            <div class="happy-emoji" style="left: 90%; animation-delay: 1s;">🥳</div>
            <div class="happy-emoji" style="left: 89%; animation-delay: 3s;">🥳</div>
            <div class="happy-emoji" style="left: 40%; animation-delay: 2,5s;">🥳</div>
            <div class="happy-emoji" style="left: 80%; animation-delay: 2,8s;">🥳</div>
            <div class="happy-emoji" style="left: 85%; animation-delay: 2,7s;">🥳</div>
            <div class="happy-emoji" style="left: 23%; animation-delay: 2,3s;">🥑</div>
            <div class="happy-emoji" style="left: 59%; animation-delay: 4s; background-image: url('https://i.postimg.cc/Bn20CrZj/phat-png.webp'); background-size: contain; background-repeat: no-repeat; width: 65px; height: 65px; display: inline-block;"></div>
            <div class="happy-emoji" style="left: 80%; animation-delay: 5s; background-image: url('https://i.postimg.cc/Bn20CrZj/phat-png.webp'); background-size: contain; background-repeat: no-repeat; width: 70px; height: 70px; display: inline-block;"></div>
            <div class="happy-emoji" style="left: 30%; animation-delay: 5s; background-image: url('https://i.postimg.cc/Bn20CrZj/phat-png.webp'); background-size: contain; background-repeat: no-repeat; width: 70px; height: 70px; display: inline-block;"></div>
            
            """,
            unsafe_allow_html=True
        )
        
    # 2. Trường điểm tiếp theo
    if diem >= 16.5:
        st.balloons()
        st.success("Bạn đủ điểm đỗ trường: Thanh Oai A (Mốc 16.5)")
        
    # 3. Trường điểm tiếp theo
    if diem >= 15.25:
        st.balloons()
        st.success("Bạn đủ điểm đỗ trường: Lý Tự Tấn (Mốc 15.25)")
        
    # 4. Trường điểm tiếp theo
    if diem >= 11.0:
        st.balloons()
        st.success("bạn đủ điểm đỗ trường: Lưu Hoàng (Mốc 11.0)")
        
    # 5. Trường điểm sàn
    if diem >= 8.0:
        st.balloons()
        st.success("Bạn đủ điểm đỗ trường: Thanh Xuân (Mốc 8.0)")
        
    # 6. Dưới mốc sàn -> Báo rớt
    if diem < 8.0:
        st.error("Điểm của bạn chưa đủ cho trường nào trong danh sách.")
        st.markdown(
            """
            <style>
            @keyframes sad-fall {
                0% { top: -10%; opacity: 0; transform: rotate(0deg); }
                10% { opacity: 1; }
                90% { opacity: 1; }
                100% { top: 110%; opacity: 0; transform: rotate(360deg); }
            }
            .sad-emoji {
                position: fixed; font-size: 2rem;
                animation: sad-fall 6s linear infinite;
                z-index: 9999; pointer-events: none;
            }
            </style>
            <div class="sad-emoji" style="left: 10%; animation-delay: 1,2s;">😭</div>
            <div class="sad-emoji" style="left: 25%; animation-delay: 1.5s;">😥</div>
            <div class="sad-emoji" style="left: 40%; animation-delay: 0.9s;">😞</div>
            <div class="sad-emoji" style="left: 60%; animation-delay: 2s;">😢</div>
            <div class="sad-emoji" style="left: 80%; animation-delay: 1s;">😭</div>
            <div class="sad-emoji" style="left: 30%; animation-delay: 1.3s;">😭</div>
            <div class="sad-emoji" style="left: 90%; animation-delay: 1,7s;">😭</div>
            <div class="sad-emoji" style="left: 20%; animation-delay: 1.9s;">😭</div>
            <div class="sad-emoji" style="left: 97%; animation-delay: 2.2s;"😿</div>
            """,
            unsafe_allow_html=True
        )
        

# Thông tin bản quyền
st.sidebar.title("📌 Thông tin tác giả")
st.sidebar.info("Được thiết kế và phát triển bởi: **Đặng Kiên Cường**")
st.sidebar.info("Ngày công bố dự án: **2 giờ sáng ngày 1/9/2026**")
st.sidebar.write("---")

# Dưới chân trang web (Footer)
st.write("---")
st.caption("© 2026 Designed & name by Dang Kien Cuong. All rights reserved.")
