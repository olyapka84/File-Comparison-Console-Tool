INDENT = '    '


def format_stylish(diff, depth=1):
    indent = calculate_indent(depth)
    result = []

    for item in diff:
        key = item['key']
        type_ = item['type']

        match type_:
            case 'nested':
                children = format_stylish(item['children'], depth + 1)
                result.append(f"{indent}  {key}: {{\n{children}\n{indent}  }}")
            case 'added':
                result.append(f"{indent}+ {key}: {stringify_value(item['value'], depth)}")
            case 'removed':
                result.append(f"{indent}- {key}: {stringify_value(item['value'], depth)}")
            case 'unchanged':
                result.append(f"{indent}  {key}: {stringify_value(item['value'], depth)}")
            case 'changed':
                result.append(f"{indent}- {key}: {stringify_value(item['old_value'], depth)}")
                result.append(f"{indent}+ {key}: {stringify_value(item['new_value'], depth)}")

    return '\n'.join(result)


def stringify_value(value, depth):
    if isinstance(value, dict):
        indent = ' ' * (depth * 4)
        formatted = '\n'.join(
            f"{indent}{INDENT}{k}: {stringify_value(v, depth + 1)}"
            for k, v in value.items()
        )
        return f"{{\n{formatted}\n{indent}}}"
    if value is None:
        return "null"
    return str(value).lower() if isinstance(value, bool) else value


def calculate_indent(depth):
    return ' ' * (depth * 4 - 2)
