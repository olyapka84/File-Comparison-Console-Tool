def format_stylish(diff, depth=1):
    indent = ' ' * (depth * 4 - 2)
    result = []

    for item in diff:
        key = item['key']
        type_ = item['type']

        if type_ == 'nested':
            children = format_stylish(item['children'], depth + 1)
            result.append(f"{indent}  {key}: {{\n{children}\n{indent}  }}")

        elif type_ == 'added':
            result.append(f"{indent}+ {key}: "
                          f"{format_value(item['value'], depth)}")

        elif type_ == 'removed':
            result.append(f"{indent}- {key}: "
                          f"{format_value(item['value'], depth)}")

        elif type_ == 'unchanged':
            result.append(f"{indent}  {key}: "
                          f"{format_value(item['value'], depth)}")

        elif type_ == 'changed':
            result.append(f"{indent}- {key}: "
                          f"{format_value(item['old_value'], depth)}")
            result.append(f"{indent}+ {key}: "
                          f"{format_value(item['new_value'], depth)}")

    return '\n'.join(result)


def format_value(value, depth):
    if isinstance(value, dict):
        indent = ' ' * (depth * 4)
        formatted = '\n'.join(f"{indent}    {k}: {format_value(v, depth + 1)}"
                              for k, v in value.items())
        return f"{{\n{formatted}\n{indent}}}"

    if value is None:
        return "null"

    return str(value).lower() if isinstance(value, bool) else value
