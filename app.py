import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Title of the app
st.title("Lesson Plan Generator")

# Explanation
st.write("이 앱은 반복되는 수업 요일과 특정 휴일을 제외한 수업 계획서와 추가 수업 계획서를 자동으로 생성합니다.")

# Input fields
class_name = st.text_input("수업반 이름:")
start_date = st.date_input("수업 시작 날짜:")
end_date = st.date_input("수업 종료 날짜:")
class_days = st.multiselect("수업 요일 선택:", ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"])
skip_dates = st.multiselect("수업 빠지는 날짜 선택:", pd.date_range(start=start_date, end=end_date))
makeup_dates = st.multiselect("보강 날짜 선택:", pd.date_range(start=start_date, end=end_date))

# Map days of the week to numbers for easy comparison
day_map = {
    "월요일": 0,
    "화요일": 1,
    "수요일": 2,
    "목요일": 3,
    "금요일": 4,
    "토요일": 5,
    "일요일": 6
}

# Generate lesson plan dates
def generate_dates(start_date, end_date, class_days, skip_dates, makeup_dates):
    current_date = start_date
    lesson_dates = set()  # Use a set to avoid duplicate dates
    
    while current_date <= end_date:
        if current_date.weekday() in [day_map[day] for day in class_days] and current_date not in skip_dates:
            lesson_dates.add(current_date)
        current_date += timedelta(days=1)
    
    # Add makeup dates, ensuring no duplicates
    lesson_dates.update(makeup_dates)
    
    return sorted(lesson_dates)

# Generate and display the lesson plan
if st.button("수업 계획서 생성"):
    if class_name and start_date and end_date and class_days:
        lesson_dates = generate_dates(start_date, end_date, class_days, skip_dates, makeup_dates)
        df = pd.DataFrame(lesson_dates, columns=["수업 날짜"])
        df["수업반"] = class_name
        df["비고"] = df["수업 날짜"].apply(lambda x: "보강" if x in makeup_dates else "")
        st.write(f"{class_name}의 수업 계획서")
        st.dataframe(df)
        
        # Option to download as CSV
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(label="수업 계획서 다운로드 (CSV)", data=csv, file_name=f"{class_name}_lesson_plan.csv", mime='text/csv')
    else:
        st.error("모든 입력 필드를 채워주세요.")
