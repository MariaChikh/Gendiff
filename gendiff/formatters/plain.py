def plain(data):
    result = make_lines(data)
    return result


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str) or isinstance(value, int):
        return f"'{value}'"


def make_lines(data, path=''):
    lines = []
    sorted_data = sorted(data.items())
    for key, (node_type, *value) in sorted_data:
        item = f'{path}{key}'
        formated_value = format_value(value[0])
        if node_type == 'added':
            lines.append(f"Property '{item}'"
                         f" was added with value: {formated_value}")
        elif node_type == 'removed':
            lines.append(f"Property '{item}' was removed")
        elif node_type == 'changed':
            old_value, new_value = value
            lines.append(f"Property '{item}' was updated."
                         f" From {format_value(old_value)}"
                         f" to {format_value(new_value)}")
        elif node_type == 'nested':
            nested_value = make_lines(value[0], f'{item}.')
            lines.append(nested_value)
    return '\n'.join(lines)
