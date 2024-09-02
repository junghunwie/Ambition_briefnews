import streamlit as st
from datetime import date
from news import fetch_news, summarize_article

# 제목 설정
st.title("🔎 실시간 뉴스 요약 서비스")

# 사이드바에 기능 구성
with st.sidebar:
    st.header("Select News")

    # 첫번째 기능: 날짜 선택
    with st.expander("🗓️ Date"):
        selected_date = st.date_input("Choose a date", value=date.today())

    # 두번째 기능: 카테고리 선택 (get_top_headlines에서 사용 가능)
    with st.expander("📚 Category"):
        categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
        selected_category = st.selectbox("Choose a category", categories)

    # 세번째 기능: 언어 선택
    with st.expander("🇰🇷 Language"):
        languages = ["en", "es", "fr", "de", "zh"]  # 지원되는 언어 코드
        selected_language = st.selectbox("Choose a language", languages)

# 검색창 구현 (검색창 내부에 연한 회색 글씨로 기본 문구 설정)
search_query = st.text_input("", "", placeholder="키워드를 입력하세요.")

# NewsAPI를 사용하여 뉴스 데이터를 가져옵니다.
if search_query:
    news_articles = fetch_news(query=search_query, 
                               from_date=selected_date, 
                               to_date=selected_date, 
                               language=selected_language)
else:
    news_articles = []

# 검색 결과 리스트 출력
st.markdown("<h4>🔽 키워드에 해당하는 검색 결과입니다.</h4>", unsafe_allow_html=True)

if news_articles:
    for article in news_articles:
        st.markdown(f"### [{article['title']}]({article['url']})")
        st.write(summarize_article(article))
        st.write(f"*출처: {article['source']['name']}*")
        st.write("---")  # 구분선 추가
else:
    st.write("해당 검색어와 일치하는 뉴스가 없습니다.")
