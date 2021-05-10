def sample_response(input_txt):
    user_message = str(input_txt).lower()
    if '%' in user_message:
        print('frek')
    if 'buy zone' in user_message and 'target' in user_message or 'sell zone' in user_message:
        if '%' in user_message:
            return 'falese signal'    
        else:    
            print('work?')
            print(user_message)
            return 'potential signal'

    if user_message in('hai'):
        return 'go find a gf'


    return 'tf u talkin about?'