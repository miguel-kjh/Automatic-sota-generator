from arxiv import Search, SortCriterion
import pandas as pd
from tqdm import tqdm
from rake_nltk import Rake

import nltk
nltk.download('stopwords')
nltk.download('punkt')

import warnings
warnings.filterwarnings("ignore")

keywords = "NLU, GPT3"
year = 2019
r = Rake()

search = Search(
    query=keywords,
    max_results=100,
    sort_by = SortCriterion.SubmittedDate
)

df = pd.DataFrame(columns=["title", "authors", "summary", "categories", "year", "keywords"])

for result in tqdm(search.results(), desc="Papers found"):
    if result.published.year >= year:
        r.extract_keywords_from_text(result.summary)
        ranked_phrases = r.get_ranked_phrases_with_scores()
        ranked_phrases = sorted(ranked_phrases, key=lambda x: x[1], reverse=True)
        top_phrases = ranked_phrases[:5]
        df = df.append({
            "title": result.title,
            "authors": result.authors,
            "summary": result.summary,
            "categories": result.categories,
            "year": result.published.year,
            "keywords": top_phrases
        }, ignore_index=True)

#sort by years
df = df.sort_values(by="year", ascending=False)
df.to_csv("papers.csv", index=False, encoding="utf-8", sep=";")