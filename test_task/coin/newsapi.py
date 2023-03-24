import requests as req


def get_news(query):
    api_key = '19574c18582b4cc5af06e1faadb2d7ee'
    path = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={api_key}"
    response = req.get(path)
    if response.status_code == 200:
        return response.json()
    else:
        return None