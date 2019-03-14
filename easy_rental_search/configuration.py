import os


KEY = os.getenv('ZOOPLA_KEY')

MINIMUM_MONTHLY_PRICE = 500
MAXIMUM_MONTHLY_PRICE = 900

SEARCH_CRITERIA = {
    'area': 'CB42RZ',
    'radius': 3,
    'minimum_beds': 1,
    'maximum_beds': 1,
    'minimum_price': MINIMUM_MONTHLY_PRICE / 4,
    'maximum_price': MAXIMUM_MONTHLY_PRICE / 4,
    'listing_status': 'rent',
    'page_size': 100,
    'order_by': 'price',
    'ordering': 'ascending'
}

RESULT_FILTERS = {
    'unshared': lambda result: 'shared' not in result.description and 'share' not in result.description,
    'has_pictures': lambda result: result.image_url != '' and result.image_url is not None,
    'has_description': lambda result: result.description != '' and result.description is not None
}
