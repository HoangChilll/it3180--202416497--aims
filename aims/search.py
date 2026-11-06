def search_by_category(items, category):
    return [dvd for dvd in items if dvd.category.casefold() == category.casefold()]


def search_by_title(items, keyword):
    query = keyword.casefold()
    return [dvd for dvd in items if query in dvd.title.casefold()]
