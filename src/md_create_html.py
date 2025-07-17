

import json
import os
import typing

import bs4

from lib.unary import _iters
from lib.unary.main import unary

from src import md_army_list
from src import md_faction_rules
from src import md_shared




def generate_html():

    @unary()
    def update_setting(
        name_setting:str):

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
                        "resources",
                        name_setting,
                        "data",
                        name_file])

            path_images_general = "resources/" \
                + name_setting \
                + "/images/general"

            text_html_template = get_text_file(
                [
                    "resources",
                    "template.html"])

            dict_keywords = get_dict_json(
                [
                    "resources",
                    "data",
                    "data_keywords.json"])

            dict_factions = get_dict_setting("data_factions.json")

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

            soup_image_core_rules = soup_full \
                .new_tag(
                    name="img",
                    attrs={
                        "class": "image_core_rules",
                        "src": path_images_general \
                            + "/image_core_rules.jpg"})

            soup_factions = bs4.BeautifulSoup(
                    markup=md_faction_rules.get_text_html_faction_rules(
                        dict_factions=dict_factions,
                        dict_keywords=dict_keywords,
                        name_setting=name_setting),
                    features="html.parser")

            soup_army_list = bs4.BeautifulSoup(
                    markup=md_army_list.get_text_html_army_lists(
                            dict_factions=dict_factions,
                            dict_keywords=dict_keywords,
                            name_setting=name_setting,
                            dict_army_list_left=dict_army_list_left,
                            dict_army_list_right=dict_army_list_right),
                    features="html.parser")

            dict_replacements = {
                "id_logo_warhammer": soup_logo_warhammer,
                "id_image_core_rules": soup_image_core_rules,
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

            with open("index_" + name_setting + ".html", mode="w", encoding="utf-8") as file_html:
                file_html \
                    .write(text_html_full)

        create_html()

    md_shared.LIST_NAMES_SETTINGS \
        >> _iters.to_iterable_for_each_eager(
            update_setting)

    return

