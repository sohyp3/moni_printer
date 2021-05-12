import analyzer

def sample_response(input_txt):
    user_message = str(input_txt).lower()

    if '%' in user_message:
        return 'frek'

    if 'buy zone' in user_message and 'target' in user_message or 'sell zone' in user_message:
        # print(user_message)
        analyzer.yosh(user_message)
        return 'potential signal'        
        # if '%' in user_message:
        #     return 'falese signal'    
        # else:    
            # # print(user_message)
            # analyzer.yosh(user_message)
            # return 'potential signal'
    

    if user_message in('hai'):
        return 'go find a gf'

    if user_message in ('fuck you'):
        return 'ikr life is difficult'

    return 'tf u talkin about?'