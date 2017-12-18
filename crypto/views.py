from django.views.generic.base import TemplateView
import requests

class HomeView(TemplateView):
    template_name = 'crypto/crypto_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            btc = requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=BRL')
            ltc = requests.get('https://api.coinmarketcap.com/v1/ticker/litecoin/?convert=BRL')
            eth = requests.get('https://api.coinmarketcap.com/v1/ticker/ethereum/?convert=BRL')
            bch = requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin-cash/?convert=BRL')

            context['btc'] = float(btc.json()[0]['price_brl'])
            context['ltc'] = float(ltc.json()[0]['price_brl'])
            context['eth'] = float(eth.json()[0]['price_brl'])
            context['bch'] = float(bch.json()[0]['price_brl'])
        except:
            context['btc'] = 0.0
            context['ltc'] = 0.0
            context['eth'] = 0.0
            context['bch'] = 0.0
            pass

        return context