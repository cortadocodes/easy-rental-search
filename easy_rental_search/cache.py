import datetime as dt
import os
import pickle


class SearchCache:

    def __init__(self, path=None):
        # if os.path.exists(path):
        #     self.load(path)
        # else:
        self._cache = {}

    def __setitem__(self, key, value):
        self._cache[key] = value

    def load(self, path):
        with open(path, 'rb') as f:
            self._cache = pickle.load(f)

    def save(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self._cache, f)

    def get_most_recent_search(self):
        if not self._cache:
            return None, None

        latest_search_time = sorted(self._cache.keys(), reverse=True)[0]
        return latest_search_time, self._cache[latest_search_time]

    def is_recent_search(self):
        latest_search_time, _ = self.get_most_recent_search()

        if latest_search_time is None:
            return False

        if dt.datetime.now() - latest_search_time <= dt.timedelta(minutes=30):
            return True

        return False
