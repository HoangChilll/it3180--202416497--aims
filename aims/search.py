def search_by_title(items, keyword):
    query = keyword.casefold()
    return [dvd for dvd in items if query in dvd.title.casefold()]
