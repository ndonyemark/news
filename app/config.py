class Config:

    NEWS_API_BASE_URL="https://newsapi.org/v2/sources?category={}&apiKey={}"
    NEWS_API_ARTICLES_URL = "https://newsapi.org/v2/top-headlines?category={}&apiKey={}"
    # print(NEWS_API_BASE_URL)

class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG = True