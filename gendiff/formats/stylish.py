INDENT = '    '


def format_stylish(diff, depth=1):
    return '\n'.join(build_stylish_diff(diff, depth))


def build_stylish_diff(diff, depth):
    result = []
    indent = calculate_indent(depth)
    for item in diff:
        result.append(format_diff_entry(item, depth, indent))
    return result


def format_diff_entry(item, depth, indent):
    key = item['key']
    type_ = item['type']
    match type_:
        case 'nested':
            children = '\n'.join(build_stylish_diff(item['children'],
                                                    depth + 1))
            return f"{indent}  {key}: {{\n{children}\n{indent}  }}"
        case 'added':
            return f"{indent}+ {key}: {stringify_value(item['value'], depth)}"
        case 'removed':
            return f"{indent}- {key}: {stringify_value(item['value'], depth)}"
        case 'unchanged':
            return f"{indent}  {key}: {stringify_value(item['value'], depth)}"
        case 'changed':
            return (f"{indent}- {key}: "
                    f"{stringify_value(item['old_value'], depth)}\n"
                    f"{indent}+ {key}: "
                    f"{stringify_value(item['new_value'], depth)}")


def stringify_value(value, depth):
    if isinstance(value, dict):
        indent = ' ' * (depth * 4)
        formatted = '\n'.join(f"{indent}{INDENT}{k}: "
                              f"{stringify_value(v, depth + 1)}"
                              for k, v in value.items())
        return f"{{\n{formatted}\n{indent}}}"
    if value is None:
        return "null"
    return str(value).lower() if isinstance(value, bool) else value


def calculate_indent(depth):
    return ' ' * (depth * 4 - 2)
