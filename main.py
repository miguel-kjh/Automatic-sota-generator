from arxiv import Search, SortCriterion
import pandas as pd
from tqdm import tqdm

import warnings
warnings.filterwarnings("ignore")

keywords = "NLU, GPT3"
year = 2019

search = Search(
    query=keywords,
    max_results=100,
    sort_by = SortCriterion.SubmittedDate
)

df = pd.DataFrame(columns=["title", "authors", "summary", "categories", "year"])

for result in tqdm(search.results(), desc="Papers found"):
    if result.published.year >= year:
        df = df.append({
            "title": result.title,
            "authors": result.authors,
            "summary": result.summary,
            "categories": result.categories,
            "year": result.published.year
        }, ignore_index=True)

#sort by years
df = df.sort_values(by="year", ascending=False)
df.to_csv("papers.csv", index=False, encoding="utf-8", sep=";")