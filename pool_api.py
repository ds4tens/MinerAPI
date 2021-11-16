from time import sleep
from typing import NoReturn

from requests import request, exceptions, Response


class PoolStats(object):
    address = ''

    def __init__(self):
        pass

    def connect(self, url: str = None, method: str = 'GET') -> Response:
        while True:
            try:
                ans = request(method=method, url=url, timeout=10)
            except exceptions.ConnectionError:
                print('Ooops... Невозможно подключиться к {}'.format(self.__class__.__name__))
                sleep(15)
            except exceptions.TooManyRedirects:
                print('Ooops... Слишком много запросов от {}'.format(self.__class__.__name__))
                sleep(300)
            except exceptions.Timeout:
                print("Ooops.. превышено время ответа от {}".format(self.__class__.__name__))
                sleep(30)
            else:
                break
        return ans

    def get_name(self):
        return self.__class__.__name__


class TooMinersPool(PoolStats):
    __name__ = "2Miners"
    basic_link = "https://2miners.com/"
    coins_dict_links = {
        "eth": "eth-mining-pool",
        "rvn": "rvn-mining-pool",
        "ergo": "erg-mining-pool",
        "etc": "etc-mining-pool",
        "xmr": "xmr-mining-pool",
        "firo": "firo-mining-pool",
        "flux": "flux-mining-pool",
        "beam": "beam-mining-pool"
    }

    def __init__(self, address):
        super().__init__()
        self.address = address
        self.links_used = {}

    def add_link(self, link):
        self.links_used[link[0]] = link[0].value()

    def remove_link(self, link):
        pass


class BinancePool(PoolStats):
    """
    Нет готового API для работы со статистикой пула. Нужно написать свой парсер под HTML страницу
    """
    # TODO написать свой парсер под HTML страницу пула бинанс
    __name__ = "BinancePool"
    basic_llink = None

    def __init__(self):
        super().__init__()


class EtherminePool(PoolStats):
    __name__ = "Ethermine"

    coins_dict_links = {
        "eth": "https://api.ethermine.org/",
        "etc": "https://api-etc.ethermine.org/",
        "zcash": "https://api-zcash.flypool.org/",
        "beam": "https://api-beam.flypool.org/",
        "ergo": "https://api-ergo.flypool.org/",
        "rvn": "https://api-ravencoin.flypool.org/",
    }

    def __init__(self, address, atcive_algo=None) -> NoReturn:
        super().__init__()
        self.address = address
        self.active_algo = atcive_algo
        self.stat = {}

    def get_stat(self):
        resp = self.connect(url="{}miner/{}/dashboard".format(self.coins_dict_links["eth"], self.address))
        if resp.ok:
            return resp.json()


resp = EtherminePool('0x0116E0d3B69Dd5a3073388c111aAd411Ce5107c0')
txt = resp.get_stat()
print(txt)
