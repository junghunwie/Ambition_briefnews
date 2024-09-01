import streamlit as st
from datetime import date

# 제목 설정
st.title("🔎 실시간 뉴스 요약 서비스")

# 사이드바에 기능 구성
with st.sidebar:
    st.header("Select News")

    # 첫번째 기능: 날짜 선택
    with st.expander("🗓️ Date"):
        selected_date = st.date_input("Choose a date", value=date.today())

    # 두번째 기능: 카테고리 선택
    with st.expander("📚 Category"):
        categories = ["Business", "Economy", "General", "Entertain", "Politics", "Sports"]
        selected_category = st.selectbox("Choose a category", categories)

    # 세번째 기능: 언어 선택
    with st.expander("🇰🇷 Language"):
        languages = ["English", "Spanish", "French", "German", "Chinese", "Japanese", "Korean"]
        selected_language = st.selectbox("Choose a language", languages)

# 현재 선택된 옵션을 보여주는 섹션
#st.subheader("Selected Options")
#st.write(f"**Date:** {selected_date}")
#st.write(f"**Category:** {selected_category}")
#st.write(f"**Language:** {selected_language}")

# 추후 데이터가 추가되면, 선택된 옵션에 따라 뉴스를 표시하는 영역을 구현할 수 있습니다.
#st.subheader("News Summary")
#st.write("Here will be the summarized news based on your selection.")


# 검색창 구현 (검색창 내부에 연한 회색 글씨로 기본 문구 설정)
search_query = st.text_input("", "", placeholder="키워드를 입력하세요.")

# 임시로 뉴스 리스트를 정의 (나중에 실제 데이터를 여기에서 가져옵니다)
# 실제 NewsAPI를 사용하면 이 리스트를 API 결과로 대체할 수 있습니다.
example_news_data = [
    {
        "title": "Example News 1",
        "summary": "This is a summary of news 1.",
        "source": "News Agency 1",
        "url": "https://example.com/news1"  # 뉴스 원문 링크
    },
    {
        "title": "Example News 2",
        "summary": "This is a summary of news 2.",
        "source": "News Agency 2",
        "url": "https://example.com/news2"  # 뉴스 원문 링크
    },
    {
        "title": "Example News 3",
        "summary": "This is a summary of news 3.",
        "source": "News Agency 3",
        "url": "https://example.com/news3"  # 뉴스 원문 링크
    }
]

# 검색어가 입력되었는지 확인하고, 해당하는 뉴스 필터링
if search_query:
    filtered_news = [news for news in example_news_data if search_query.lower() in news['title'].lower()]
else:
    filtered_news = example_news_data

# 검색 결과 리스트 출력
#st.subheader()
st.markdown("<h4>🔽 키워드에 해당하는 검색 결과입니다.</h4>", unsafe_allow_html=True)

if filtered_news:
    for news in filtered_news:
        # 제목을 하이퍼링크로 설정
        st.markdown(f"### [{news['title']}]({news['url']})")
        st.write(news['summary'])
        st.write(f"*출처: {news['source']}*")
        st.write("---")  # 구분선 추가
else:
    st.write("해당 검색어와 일치하는 뉴스가 없습니다.")



