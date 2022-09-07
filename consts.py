from datetime import date, datetime, timedelta

year = datetime.now().year
day_options = {'сегодня': date.today().strftime('%Y-%m-%d'),
                'вчера': (date.today() - timedelta(days=1)).strftime('%Y-%m-%d')}
months = {'янв': '01', 'фев': '02', 'мар': '03', 'апр': '04', 'май': '05', 'июн': '06',
          'июл': '07', 'авг': '08', 'сен': '09', 'окт': '10', 'ноя': '11', 'дек': '12'}
