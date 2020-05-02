from app import app
from .models import news
import urllib.request, json

News = news.News
Articles = news.Articles

api_key = app.config["NEWS_API_URL"]
# print(api_key)
base_url = app.config["NEWS_API_BASE_URL"]
articles_url = app.config["NEWS_API_ARTICLES_URL"]
# print(base_url)
def get_sources(category):
    
    get_news_source_url = base_url.format(category, api_key)
    print(get_news_source_url)
    with urllib.request.urlopen(get_news_source_url) as url:

        get_news_source_data = url.read()
        get_news_source_response = json.loads(get_news_source_data)

        news_results = None

        if get_news_source_response['sources']:

            news_results_list = get_news_source_response["sources"]
            news_results = process_results(news_results_list)
    
    return news_results

def process_results(news_list):

    news_results = []

    for news_item in news_list:
        id = news_item.get('id')
        name=news_item.get("name")
        description=news_item.get("description")
        url=news_item.get("url")
        category=news_item.get("category")
        language=news_item.get("language")
        country=news_item.get("country")

        if language == 'en':
            news_object = News(id,name,description,url,category,language,country)
            news_results.append(news_object)
    
    return news_results


def get_articles(category):
    
    get_news_articles_url = articles_url.format(category, api_key)
    print(get_news_articles_url)
    with urllib.request.urlopen(get_news_articles_url) as url:

        get_news_articles_data = url.read()
        get_news_articles_response = json.loads(get_news_articles_data)

        articles_results = None

        if get_news_articles_response['articles']:
            articles_results_list = get_news_articles_response["articles"]
            articles_results = process_articles(articles_results_list)
    
    return articles_results

def process_articles(articles_list):
    articles_results = []
    for article_item in articles_list:
        author = article_item.get("author")
        title = article_item.get("title")
        description = article_item.get("description")
        url = article_item.get("url")
        urlToImage = article_item.get("urlToImage")
        publishedAt = article_item.get("publishedAt")
        content = article_item.get("content")

        # if urlToImage:
        articles_object = Articles(author, title, description, url, urlToImage, publishedAt, content)
        articles_results.append(articles_object)
    
    return articles_results