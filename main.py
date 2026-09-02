from fastapi import FastAPI
from fastapi.responses import HTMLResponse

Webapp = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "Ichigo Kurasaki",
        "title": "Bleach is Awesome",
        "content": "Bleach has amazing writing, symoblism and character development.",
        "date_posted": "02/09/2020",
    },

    {
        "id": 2,
        "author": "Son Goku",
        "title": "Dragon Ball Z is Awesome",
        "content": "Dragon Ball Z has amazing fights, a great power system and likable characters",
        "date_posted": "03/09/2020",
    },

]

@Webapp.get("/", response_class = HTMLResponse, include_in_schema=False)
@Webapp.get("/posts", response_class = HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"

@Webapp.get("/api/posts")
def getposts():
    return posts