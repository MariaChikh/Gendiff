def stylish(data):
    result = '{\n' + build_tree(data) + '\n}'
    return result


def build_tree(data, depth=1):
    lines = []
    sorted_data = (sorted(data.items()))
    for key, (type, *value) in sorted_data:
        lines = make_lines(key, value, type, lines, depth)
        result = '\n'.join(lines)
    return result


def make_lines(key, value, type, lines, depth):

    prefix = '  '
    if type == 'added':
        prefix = '+ '
        lines = formate_lines(depth, prefix, key, value[0], lines)
    elif type == 'removed':
        prefix = '- '
        lines = formate_lines(depth, prefix, key, value[0], lines)
    elif type == 'unchanged':
        lines = formate_lines(depth, prefix, key, value[0], lines)
    elif type == 'changed':
        lines = format_changed_data(depth, key, value, lines)
    elif type == 'nested':
        indent = ' ' * (4 * depth - 2)
        children = build_tree(value[0], depth + 1)
        formated_value = f'{{\n{children}\n{indent}  }}'
        lines = formate_lines(depth, prefix, key, formated_value, lines)
    return lines


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
            indent = ' ' * (4 * (depth - 1))
            lines = formate_lines(depth, prefix, key, formated_value, lines)
        return '{\n' + '\n'.join(lines) + '\n' + indent + '}'


def formate_lines(depth, prefix, key, value, lines):
    formated_value = format_value(value, depth + 1)
    indent = ' ' * (4 * depth - 2)
    lines.append(f'{indent}{prefix}{key}: {formated_value}')
    return lines


def format_changed_data(depth, key, value, lines):
    old_value, new_value = value
    indent = ' ' * (4 * depth - 2)
    lines.append(f'{indent}- {key}: {format_value(old_value, depth+1)}'
                 f'\n{indent}+ {key}: {format_value(new_value, depth+1)}')
    return lines
