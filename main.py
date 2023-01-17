from arxiv import Search, SortCriterion

# Define las palabras clave para la búsqueda
keywords = "NLU, GPT3"

# Busca papers en arXiv.org
search = Search(
    query=keywords,
    max_results=100,
    sort_by = SortCriterion.SubmittedDate
)

# Imprime los títulos de los papers encontrados
print("Papers encontrados en arXiv:")
for result in search.results():
    print(result.title)
    """print(result.summary)
    print(result.authors)
    print(result.published)"""
    print(result.categories)
    print(result.entry_id)
    print(result.primary_category)
    print(result.journal_ref)
    print("#"*100)