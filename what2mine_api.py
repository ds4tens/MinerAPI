from pprint import pprint

from requests import request, Response, exceptions

DEFAULT_COINS_STAT = {
    "eth_hash": 0, "eth_power": 0,
    "e4g_hr": 0, "e4g_pw": 0,
    "zh_hr": 0, "zh_pw": 0,
    "cnh_hr": 0, "cnh_pw": 0,
    "cng_hr": 0, "cng_pw": 0,
    "cnr_hr": 0, "cnr_pw": 0,
    "cnf_hr": 0, "cnf_pw": 0,
    "eqa_hr": 0, "eqa_pw": 0,
    "cc_hr": 0, "cc_pw": 0,
    "cr29_hr": 0, "cr29_pw": 0,
    "ct31_hr": 0, "ct31_pw": 0,
    "ct32_hr": 0, "ct32_pw": 0,
    "eqb_hr": 0, "eqb_pw": 0,
    "rmx_hr": 0, "rmx_pw": 0,
    "ns_hr": 0, "ns_pw": 0,
    "al_hr": 0, "al_pw": 0,
    "ops_hr": 0, "ops_pw": 0,
    "eqz_hr": 0, "eqz_pw": 0,
    "zlh_hr": 0, "zlh_pw": 0,
    "kpw_hr": 0, "kpw_pw": 0,
    "ppw_hr": 0, "ppw_pw": 0,
    "x25x_hr": 0, "x25x_pw": 0,
    "fpw_hr": 0, "fpw_pw": 0,
    "vh_hr": 0, "vh_pw": 0
}


class What2Mine(object):
    profit_currency = {}

    def __init__(self):
        pass

    def get_stat(self, coins_stat: dict = None) -> dict:
        if coins_stat is None:
            coins_stat = DEFAULT_COINS_STAT
        ans = request(
            'GET',
            url=
            "https://whattomine.com/coins.json?eth=true&factor%5Beth_hr%5D={eth_hash}&factor%5Beth_p%5D={eth_power}&e4g"
            "=true&factor%5Be4g_hr%5D={e4g_hr}&factor%5Be4g_p%5D={e4g_pw}&zh=true&factor%5Bzh_hr%5D={zh_hr}&factor%5Bzh_p%5D"
            "={zh_pw}&cnh=true&factor%5Bcnh_hr%5D={cnh_hr}&factor%5Bcnh_p%5D={cnh_pw}&cng=true&factor%5Bcng_hr%5D={cng_hr}&factor"
            "%5Bcng_p%5D={cng_pw}&cnr=true&factor%5Bcnr_hr%5D={cnr_hr}&factor%5Bcnr_p%5D={cnr_pw}&cnf=true&factor%5Bcnf_hr%5D"
            "={cnf_hr}&factor%5Bcnf_p%5D={cnf_pw}&eqa=true&factor%5Beqa_hr%5D={eqa_hr}&factor%5Beqa_p%5D={eqa_pw}&cc=true&factor"
            "%5Bcc_hr%5D={cc_hr}&factor%5Bcc_p%5D={cc_pw}&cr29=true&factor%5Bcr29_hr%5D={cr29_hr}&factor%5Bcr29_p%5D={cr29_pw}&ct31"
            "=true&factor%5Bct31_hr%5D={ct31_hr}&factor%5Bct31_p%5D={ct31_pw}&ct32=true&factor%5Bct32_hr%5D={ct32_hr}&factor"
            "%5Bct32_p%5D={ct32_pw}&eqb=true&factor%5Beqb_hr%5D={eqb_hr}&factor%5Beqb_p%5D={eqb_pw}&rmx=true&factor%5Brmx_hr%5D"
            "={rmx_hr}&factor%5Brmx_p%5D={rmx_pw}&ns=true&factor%5Bns_hr%5D={ns_hr}&factor%5Bns_p%5D={ns_pw}&al=true&factor"
            "%5Bal_hr%5D={al_hr}&factor%5Bal_p%5D={al_pw}&ops=true&factor%5Bops_hr%5D={ops_hr}&factor%5Bops_p%5D={ops_pw}&eqz"
            "=true&factor%5Beqz_hr%5D={eqz_hr}&factor%5Beqz_p%5D={eqz_pw}&zlh=true&factor%5Bzlh_hr%5D={zlh_hr}&factor%5Bzlh_p"
            "%5D={zlh_pw}&kpw=true&factor%5Bkpw_hr%5D={kpw_hr}&factor%5Bkpw_p%5D={kpw_pw}&ppw=true&factor%5Bppw_hr%5D={ppw_hr}"
            "&factor%5Bppw_p%5D={ppw_pw}&x25x=true&factor%5Bx25x_hr%5D={x25x_hr}&factor%5Bx25x_p%5D={x25x_pw}&fpw=true&factor"
            "%5Bfpw_hr%5D={fpw_hr}&factor%5Bfpw_p%5D={fpw_pw}&vh=true&factor%5Bvh_hr%5D={vh_hr}&factor%5Bvh_p%5D={vh_pw}&factor"
            "%5Bcost%5D=0.1&sort=Profitability24&volume=0&revenue=24h&factor%5Bexchanges%5D%5B%5D=&factor"
            "%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D"
            "=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=coinex&factor"
            "%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate"
            "&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B"
            "%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor"
            "%5Bexchanges%5D%5B%5D=stex&dataset=Main"
                .format(
                **coins_stat
            )
        )
        return ans.json()




cls = What2Mine()
pprint(cls.get_stat())
