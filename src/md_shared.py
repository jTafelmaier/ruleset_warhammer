

import json
import os
import typing




def get_text_file(
    list_texts_path:typing.List[str]):

    path = os.path.join(
        *list_texts_path)

    with open(file=path, mode="r", encoding="utf-8") as file:
        return file.read()


def get_dict_json(
    list_texts_path:typing.List[str]):

    return json.loads(get_text_file(list_texts_path))


def get_dict_setting(
    name_file:str):

    return get_dict_json(
        [
            "src",
            "data",
            name_file])


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

