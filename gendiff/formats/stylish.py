INDENT = '    '


def format_stylish(diff, depth=1):
    return '\n'.join(process_diff(diff, depth))


def process_diff(diff, depth):
    result = []
    indent = get_indent(depth)
    for item in diff:
        result.append(format_node(item, depth, indent))
    return result


def format_node(item, depth, indent):
    key = item['key']
    type_ = item['type']
    if type_ == 'nested':
        children = '\n'.join(process_diff(item['children'], depth + 1))
        return f"{indent}  {key}: {{\n{children}\n{indent}  }}"
    if type_ == 'added':
        return f"{indent}+ {key}: {format_value(item['value'], depth)}"
    if type_ == 'removed':
        return f"{indent}- {key}: {format_value(item['value'], depth)}"
    if type_ == 'unchanged':
        return f"{indent}  {key}: {format_value(item['value'], depth)}"
    if type_ == 'changed':
        return (f"{indent}- {key}: {format_value(item['old_value'], depth)}\n"
                f"{indent}+ {key}: {format_value(item['new_value'], depth)}")


def format_value(value, depth):
    if isinstance(value, dict):
        indent = INDENT * (depth * 4)
        formatted = '\n'.join(f"{indent}{INDENT}{k}: "
                              f"{format_value(v, depth + 1)}"
                              for k, v in value.items())
        return f"{{\n{formatted}\n{indent}}}"
    if value is None:
        return "null"
    return str(value).lower() if isinstance(value, bool) else value


def get_indent(depth):
    return INDENT * (depth * 4 - 2)
