CURRENCIES = {
    'USD': 1,
    'EUR': 1.06,
    'YEN': 0.0067,
    'GBP': 1.23,
    'AUD': 0.64,
    'CAD': 0.74
}

def to_usd(curr, amount):

    if curr not in CURRENCIES:
        return f"{curr} is not supported"
    
    if amount < 0:
        return "Invalid amount"

    if curr == 'USD':
        return amount * CURRENCIES['USD']
    elif curr == 'EUR':
        return amount * CURRENCIES['EUR']
    elif curr == 'YEN':
        return amount * CURRENCIES['YEN']
    elif curr == 'GBP':
        return amount * CURRENCIES['GBP']
    elif curr == 'AUD':
        return amount * CURRENCIES['AUD']
    elif curr == 'CAD':
        return amount * CURRENCIES['CAD']
    
def from_usd(curr, amount):

    if curr not in CURRENCIES:
        return f"{curr} is not supported"
    
    if amount < 0:
        return "Invalid amount"
    
    if curr == 'USD':
        return round(amount * (1 / CURRENCIES['USD']), 4)
    elif curr == 'EUR':
        return round(amount * (1 / CURRENCIES['EUR']), 4)
    elif curr == 'YEN':
        return round(amount * (1 / CURRENCIES['YEN']), 4)
    elif curr == 'GBP':
        return round(amount * (1 / CURRENCIES['GBP']), 4)
    elif curr == 'AUD':
        return round(amount * (1 / CURRENCIES['AUD']), 4)
    elif curr == 'CAD':
        return round(amount * (1 / CURRENCIES['CAD']), 4)
    
def convert(curr, amount, to_curr):
    try:
        if curr not in CURRENCIES:
            return f"{curr} is not supported"
    
        if to_curr not in CURRENCIES:
            return f"{to_curr} is not supported" 
    
        if amount < 0:
            return "Invalid amount"
        
        usd_amount = to_usd(curr, amount)
        convert_amount = from_usd(to_curr, usd_amount)

        return f"{amount} {curr} is {convert_amount} {to_curr}"
    
    except Exception as e:
        print(e)


        
    





    


    
