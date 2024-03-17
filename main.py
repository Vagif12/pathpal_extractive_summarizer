from summarizer import summarize
from fastapi import FastAPI
from typing import List

app = FastAPI()


@app.post("/summarize_entries/")
async def summarize_entries(data: dict):
    entries = data.get("entries", [])
    summarized_entries = []
    for entry in entries:
        title = entry.get("title", "")
        content = entry.get("content").get("entryContent")
        summary_text = summarize(title, content.replace("🙂", ""))
        entry["summary"] = " ".join(summary_text)
        summarized_entries.append(entry)
    return summarized_entries

# title = "The Tortoise Trainer – Painting by Osman Hamdi Bey"
# text = "Like most people this is one of my favourite paintings to stare at for hours. It is a painting by Osman Hamdi Bey which was originally called in Turkish “Kaplumbağalar ve Adam” (The tortoises and The man) but later, with popularity, it was generally named The Tortoise Trainer.\nThe painter painted two versions of this, one in 1906 and the other in 1907. The one documented in the photo is the first version and is located in one of the best contemporary/orientalist/classical museums of İstanbul Pera Museum. It is displayed in this Museum for the public and photos can be taken (without flash obviously).\nIt’s an oil on canvas with 221,5 x 120 cm dimensions. If you are an art lover I would definitely suggest you have a stop at the Pera Museum just to only see this painting as it’s extremely worthwhile"

# for i in range(100):
#     summary = summarize(title, text.replace("🙂",""))

#     print(summary)