from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="Templates")

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

@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts":posts, "title":"Home"})

@app.get("/api/posts")
def getposts():
    return posts