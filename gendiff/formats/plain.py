def format_plain(diff, path=""):
    result = []

    for item in diff:
        key = item['key']
        type_ = item['type']
        full_path = f"{path}.{key}" if path else key

        if type_ == 'nested':
            children = format_plain(item['children'], full_path)
            result.append(children)

        elif type_ == 'added':
            result.append(f"Property '{full_path}' was added with value: {format_value(item['value'])}")

        elif type_ == 'removed':
            result.append(f"Property '{full_path}' was removed")

        elif type_ == 'changed':
            result.append(f"Property '{full_path}' was updated. "
                          f"From {format_value(item['old_value'])} to {format_value(item['new_value'])}")

    return '\n'.join(result)


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    if value is None:
        return "null"
    if isinstance(value, int):
        return value
    if isinstance(value, bool):
        return str(value).lower()
    return f"'{value}'"
