def answer_from_query(cmd, value, file_name):
    match cmd:
        case "filter":
            return list(filter(lambda x: value in x, file_name))
        case "map":
            return "\n".join([x.split()[int(value)] for x in file_name])
        case "unique":
            return list(set(file_name))
        case "sort":
            return sorted(file_name, reverse=value == "desc")
        case "limit":
            return list(file_name)[:int(value)]
