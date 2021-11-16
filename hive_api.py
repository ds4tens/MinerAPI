import pprint
from time import sleep
from typing import NoReturn

from requests import request, exceptions


class HiveOS(object):
    url = 'https://api2.hiveos.farm/api/v2'

    def __init__(self, access_token: str) -> NoReturn:
        self.token = access_token

    def api_query(self, method: str, command: str, params: str = None, data: str = None) -> dict:
        data = data or {}
        params = params or {}
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.token
        }

        while True:
            try:
                ans = request(
                    method=method,
                    url=self.url + command,
                    headers=headers,
                    params=params,
                    json=data,
                    timeout=15
                )
            except exceptions.ConnectionError:
                print('Ooops... Подключение к HiveOS невозмоно')
                sleep(15)
            except exceptions.Timeout:
                print('Ooops... Превышено время ожидания ответа от HiveOS')
                sleep(15)
            except exceptions.TooManyRedirects:
                print('Ooops... Превышено количество запросов от HiveOS')
                sleep(300)
            else:
                print(ans)
                break

        return ans.json()

    def get_farms(self) -> dict:
        return self.api_query(method='GET', command='/farms')

    def get_curr_farm(self, id_farm: str) -> dict:
        return self.api_query(method='GET', command='/farms/' + id_farm)


token = ''
hive = HiveOS(token)
# ans = hive.get_farms()
ans = hive.get_curr_farm("1444743")
pprint.pprint(ans)
