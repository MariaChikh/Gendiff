DEFAULT_IDENT = '    '
def format_value(value, depth=1):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance (value, str):
        return value
    elif isinstance(value, int):
        return str(value)
    elif isinstance(value, dict):
        for key in value:
            
            val = value[key]
            formated_value = format_value(val)
            
            return '{' + f'\n{DEFAULT_IDENT * (depth+1)} {key}: {formated_value}' + '\n' + DEFAULT_IDENT + '  }'
    depth += 1 
    


def stylish(data):
    result = []
    
    for key in data:
        
        type, value = data[key]
        formated_value = format_value(value)
        if type == 'added':
            result.append(f'{DEFAULT_IDENT}+ {key}: {formated_value}')
            
        elif type == 'removed':
            result.append(f'{DEFAULT_IDENT}- {key}: {formated_value}')
            
        elif type == 'unchanged':
            result.append(f'{DEFAULT_IDENT}  {key}: {formated_value}')
            
        elif type == 'changed':
            old_value, new_value = value
    
            result.append(f'{DEFAULT_IDENT}- {key}: {format_value(old_value)}\n{DEFAULT_IDENT}+ {key}: {format_value(new_value)}')
            
        elif type == 'nested':
            new_data = {}
            new_data[key] = value
            result.append(f'{DEFAULT_IDENT} {key}: {stylish(new_data[key])}')
    final_result = '{\n' + '\n'.join(result) + '\n}\n'
    return final_result