import os

def get_dev_key():

    ads_dev_key_filename = os.path.abspath(os.path.expanduser('~/.ads/dev_key'))

    if os.path.exists(ads_dev_key_filename):
        with open(ads_dev_key_filename, 'r') as fp:
            dev_key = fp.readline().rstrip()

        return dev_key

    if 'ADS_DEV_KEY' in os.environ:
        return os.environ['ADS_DEV_KEY']

    raise IOError("no ADS API key found in ~/.ads/dev_key")
