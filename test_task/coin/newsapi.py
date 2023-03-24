import requests as req


def get_news(query):
    api_key = '19574c18582b4cc5af06e1faadb2d7ee'
    path = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={api_key}"
    resp = req.get(path)
    if resp.status_code == 200:
        return resp.json()
    else:
        return None