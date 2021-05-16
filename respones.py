import analyzer

def sample_response(input_txt,datuu):
    print(datuu)
    user_message_without_lower = str(input_txt)
    user_message = str(input_txt).lower()
    if '%' in user_message:
        return 'frek'

    if 'buy zone' in user_message and 'target' in user_message or 'sell zone' in user_message:
        if '%' in user_message:
            return 'false signal'
        else:
            print(datuu)
            analyzer.yosh(user_message_without_lower,datuu)
            return 'potential signal'
    
    if 'دهب' in user_message or 'ذهب' in user_message or 'زياد' in user_message or 'gold' in user_message:
        return 'الذهب سعره ثابت. كيف بتحكي استثمار آمن؟'
        
    if user_message in('hai'):
        return 'go find a gf'

    if user_message in ('fuck you'):
        return 'ikr life is difficult'

    if 'goat' in user_message:
        return "hyp3 sama is GOAT\nHYP3 IS THE LORD"
    return 'tf u talkin about?'