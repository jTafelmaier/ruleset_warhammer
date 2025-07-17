



function toggle_display_state(text_id_element) {

    let style_element = document.getElementById(text_id_element).style;

    if (style_element.display == "none") {
        style_element.display = "block"
        }
    else {
        style_element.display = "none"
        }
    }


function restore_action_tokens() {
    Array.prototype.forEach.call(
        document.getElementsByClassName("action_token toggleable"),
        (element) => element.classList.remove("used"));
}


function destroy_unit(text_id_element) {

    element = document.getElementById(text_id_element);

    element.classList.toggle("destroyed")
}


function toggle_token(text_id_element) {

    document.getElementById(text_id_element)
        .classList
        .toggle("used");
    }


function display_faction(text_id_faction) {

    let style_div_faction = document.getElementById(text_id_faction).style;

    if (style_div_faction.display == "none") {

        Array.prototype.forEach.call(
            document.getElementsByClassName("div_container_faction_rules"),
            (element) => element.classList.add("grayscale"));

        document.getElementsByClassName(text_id_faction)
            [0]
            .classList
            .remove("grayscale");

        Array.prototype.forEach.call(
            document.getElementsByClassName("div_faction"),
            (element) => element.style.display = "none");

        style_div_faction.display =  "block"}

    else {
        Array.prototype.forEach.call(
            document.getElementsByClassName("div_container_faction_rules"),
            (element) => element.classList.remove("grayscale"));

        style_div_faction.display =  "none"}

    }
