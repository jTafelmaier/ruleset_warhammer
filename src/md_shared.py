



LIST_NAMES_SETTINGS = [
    "40k",
    "horus_heresy"]


def get_text_name_directory_faction(
    name_faction:str):

    return name_faction \
        .lower() \
        .replace(
            " ",
            "_")


def get_text_path_images_faction(
    name_setting:str,
    name_directory_faction:str):

    return "/" \
        .join(
            [
                "resources",
                name_setting,
                "images",
                "factions",
                name_directory_faction])

