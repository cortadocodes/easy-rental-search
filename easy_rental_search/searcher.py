import datetime as dt
import os

from zoopla import Zoopla

from easy_rental_search.cache import SearchCache
from easy_rental_search import configuration as conf


CACHE_PATH = os.path.join('data', 'cache.pkl')


def apply_filters_to_result(result):
    for filter_ in conf.RESULT_FILTERS.values():
        if filter_(result) is False:
            return False
    return True


def search(key, cache, criteria):

    if cache.is_recent_search():
        latest_search_time, search = cache.get_most_recent_search(cache)

    else:
        zoopla = Zoopla(api_key=key)
        search = zoopla.property_listings(params=criteria)
        cache[dt.datetime.now()] = search

    # Adjust weekly price to monthly price.
    for result in search.listing:
        result.price = 4 * result.price

    filtered_results = list(filter(apply_filters_to_result, search.listing))

    print([result.price for result in filtered_results])


if __name__ == '__main__':
    cache = SearchCache(CACHE_PATH)
    search(conf.KEY, cache, conf.SEARCH_CRITERIA)
    cache.save(CACHE_PATH)
