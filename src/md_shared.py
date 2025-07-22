



def get_text_name_directory_faction(
    name_faction:str):

    return name_faction \
        .lower() \
        .replace(
            " ",
            "_")


def get_text_path_images_faction(
    name_directory_faction:str):

    return "/" \
        .join(
            [
                "resources",
                "factions",
                name_directory_faction])

