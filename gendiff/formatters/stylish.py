DEFAULT_INDENT = 4


def stylish(data):
    result = '{\n' + build_tree(data) + '\n}'
    return result


def build_tree(data, depth=1):
    lines = []
    sorted_data = (sorted(data.items()))
    for key, (node_type, *value) in sorted_data:
        lines.append(make_lines(key, value, node_type, depth))
    return '\n'.join(lines)
    

def make_lines(key, value, node_type, depth):
    prefix = '  '
    if node_type == 'added':
        prefix = '+ '
        return format_lines(depth, prefix, key, value[0])
    elif node_type == 'removed':
        prefix = '- '
        return format_lines(depth, prefix, key, value[0])
    elif node_type == 'unchanged':
        return format_lines(depth, prefix, key, value[0])
    elif node_type == 'changed':
        return format_changed_data(depth, key, value)
    elif node_type == 'nested':
        indent = ' ' * (DEFAULT_INDENT * depth - 2)
        children = build_tree(value[0], depth + 1)
        formated_value = f'{{\n{children}\n{indent}  }}'
        return format_value(formated_value, depth)


def format_value(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str) or isinstance(value, int):
        return value
    elif isinstance(value, dict):
        prefix = '  '
        lines = []
        for key, val in value.items():
            formated_value = format_value(val, depth + 1)
            indent = ' ' * (DEFAULT_INDENT * (depth - 1))
            lines.append(format_lines(depth, prefix, key, formated_value))
        return '{\n' + '\n'.join(lines) + '\n' + indent + '}'


def format_lines(depth, prefix, key, value):
    
    formated_value = format_value(value, depth + 1)
    indent = ' ' * (DEFAULT_INDENT * depth - 2)
    return (f'{indent}{prefix}{key}: {formated_value}')
    

def format_changed_data(depth, key, value):
    
    old_value, new_value = value
    indent = ' ' * (DEFAULT_INDENT * depth - 2)
    return (f'{indent}- {key}: {format_value(old_value, depth + 1)}'
                 f'\n{indent}+ {key}: {format_value(new_value, depth + 1)}')
