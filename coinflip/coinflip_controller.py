from coinflip_models import COINFLIPS
from coinflip_view import render_coinflip

def flip_a_coin(model, coinflip_config, test=False):
    '''Flip a coin according to a distribution model

    Args:
        model (str): The distribution model to use
        coinflip_config (CoinflipConfig): Configurations for the "coinflip" call
            to random.org
        test (bool): mock the call random.org if true

    Returns:
        (str) the results of the coinflip
    
    Side-effect:
        Writes the results using stdio

    '''
    from MODELS[model] import the_ask, the_answer
    coinflip = the_answer(the_ask(test, **coinflip_configuration)))
    render_coinflip(coinflip, **render_configuration)
    return coinflip
