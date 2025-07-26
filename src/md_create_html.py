

import json
import os
import typing

import bs4

from src import md_army_list
from src import md_faction_rules
from src import md_shared




def generate_htmls():

    def create_html():

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

        path_images_general = "resources/" \
            + "/general"

        text_html_template = get_text_file(
            [
                "src",
                "data",
                "index_template.html"])

        dict_keywords = get_dict_json(
            [
                "src",
                "data",
                "data_keywords.json"])

        list_dicts_factions = get_dict_setting("data_factions.json") \
            ["data"]

        dict_army_list_left = get_dict_setting("army_list_left.json")

        dict_army_list_right = get_dict_setting("army_list_right.json")

        soup_full = bs4.BeautifulSoup(
                markup=text_html_template,
                features="html.parser")

        soup_full \
            .find(
                name="div",
                id="header_document") \
            ["style"] \
            = "background-image: url('" \
                + path_images_general \
                + "/image_cover.jpg');"

        soup_logo_warhammer = soup_full \
            .new_tag(
                name="img",
                attrs={
                    "class": "logo_warhammer",
                    "src": path_images_general \
                        + "/logo_warhammer.png"})

        soup_factions = bs4.BeautifulSoup(
                markup=md_faction_rules.get_text_html_faction_rules(
                    list_dicts_factions=list_dicts_factions,
                    dict_keywords=dict_keywords),
                features="html.parser")

        soup_army_list = bs4.BeautifulSoup(
                markup=md_army_list.get_text_html_army_lists(
                    list_dicts_factions=list_dicts_factions,
                    dict_keywords=dict_keywords,
                    dict_army_list_left=dict_army_list_left,
                    dict_army_list_right=dict_army_list_right),
                features="html.parser")

        dict_replacements = {
            "id_logo_warhammer": soup_logo_warhammer,
            "id_factions": soup_factions,
            "id_army_lists": soup_army_list}

        for id_placeholder, soup_replacement in dict_replacements.items():
            soup_full \
                .find(
                    name="placeholder",
                    id=id_placeholder) \
                .replace_with(soup_replacement)

        text_html_full = soup_full \
            .prettify()

        with open("index.html", mode="w", encoding="utf-8") as file_html:
            file_html \
                .write(text_html_full)

    create_html()

    return None

