import mureq as mur

page = 1


def request():
    try:
        response = mur.get(
            'https://novosibirsk.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p={}&region=4897'.format(page))
        if response.status_code != 200:
            print(response.status_code)
            raise StopIteration
        else:
            print(response.status_code)
            return response.body
    except:
        raise StopIteration
