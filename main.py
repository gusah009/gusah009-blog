import requests

URL = "https://gusah009.github.io"
DATA = requests.get(URL + "/page-data/index/page-data.json").json()["result"]["data"]["allMarkdownRemark"]["edges"]

markdown_text = """
## ✅ Latest Blog Post

"""  # list of blog posts will be appended here

MAX_POST = 5
for idx, feed in enumerate(DATA):
    if idx > MAX_POST:
        break
    else:
        print(feed)
        feed_path = feed["node"]["fields"]["slug"]
        feed_date = feed["node"]["frontmatter"]["date"][:-1].replace(".", "-")
        feed_title = feed["node"]["frontmatter"]["title"]
        print(feed_path, feed_date, feed_title)
        markdown_text += (
            f"[{feed_date} - {feed_title}]({URL + feed_path}) <br/>\n".replace("", "")
        )

f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
