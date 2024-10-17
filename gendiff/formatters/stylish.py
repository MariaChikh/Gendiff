DEFAULT_IDENT = '....'
def format_value(value, depth=1):
    result =[]
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
            formated_value = format_value(val, depth+1)
            ident = '.' * (4 * depth - 2)
            result.append(f'{DEFAULT_IDENT}{ident}{key}: {formated_value}')
            final_result = '{\n' + '\n'.join(result) + '\n' + (DEFAULT_IDENT+ident) + '}'     
        return final_result
     
    


def stylish(data):
    result = []
    sorted_data = dict(sorted(data.items()))

    for key in sorted_data:
    
        type, *value = sorted_data[key]
        
        formated_value = format_value(value[0])
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
            new_data[key] = value[0]
            result.append(f'{DEFAULT_IDENT}  {key}: {(stylish(new_data[key]))}')
    
    final_result = '{\n' + '\n'.join(result) + '\n}'
    return final_result