from newsapi import NewsApiClient
import textwrap

# API 키 설정
newsapi = NewsApiClient(api_key='73b17ead3cea453f9e12c3925f7c1f4d')

# 뉴스 데이터를 가져오는 함수
def fetch_news(query, from_date=None, to_date=None, language='en'):
    try:
        if language not in ['ar', 'de', 'en', 'es', 'fr', 'he', 'it', 'nl', 'no', 'pt', 'ru', 'se', 'ud', 'zh']:
            raise ValueError("invalid language")
        
        all_articles = newsapi.get_everything(q=query,
                                              from_param=from_date,
                                              to=to_date,
                                              language=language,
                                              sort_by='relevancy',
                                              page=1)
        return all_articles['articles']
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []

# 뉴스 요약을 위한 함수
def summarize_article(article, max_sentences=3):
    summary = textwrap.shorten(article['description'], width=150, placeholder="...")
    return summary
