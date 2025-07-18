



function toggle_display_state(text_id_element) {

    let style_element = document.getElementById(text_id_element).style

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
        (element) => element.classList.remove("used"))
}


function reduce_health(text_id_element) {

    element_health_bar = document.getElementById(text_id_element).getElementsByClassName("health_bar")[0]

    var int_count_tokens_new = parseInt(element_health_bar.getAttribute("count")) - 1
    var int_count_tokens_max = parseInt(element_health_bar.getAttribute("max"))

    if (int_count_tokens_new == 0) {
        int_count_tokens_new = int_count_tokens_max
        for (element_health_token of element_health_bar.getElementsByClassName("health_token")) {
            element_health_token.classList.remove("used")
        }
    }

    if (int_count_tokens_new == 1) {
        element_health_bar.classList.add("red")
    } else {
        element_health_bar.classList.remove("red")
    }

    element_health_bar.setAttribute("count", int_count_tokens_new)

    for (element_health_token of element_health_bar.getElementsByClassName("health_token")) {
        if (parseInt(element_health_token.getAttribute("index")) >= int_count_tokens_new) {
            element_health_token.classList.add("used")
        }
    }
}


function destroy_unit(text_id_element) {

    element = document.getElementById(text_id_element)

    element.classList.toggle("destroyed")
}


function toggle_token(text_id_element) {

    document.getElementById(text_id_element)
        .classList
        .toggle("used")
    }


function display_faction(text_id_faction) {

    let style_div_faction = document.getElementById(text_id_faction).style

    if (style_div_faction.display == "none") {

        Array.prototype.forEach.call(
            document.getElementsByClassName("div_container_faction_rules"),
            (element) => element.classList.add("grayscale"))

        document.getElementsByClassName(text_id_faction)
            [0]
            .classList
            .remove("grayscale")

        Array.prototype.forEach.call(
            document.getElementsByClassName("div_faction"),
            (element) => element.style.display = "none")

        style_div_faction.display =  "block"}

    else {
        Array.prototype.forEach.call(
            document.getElementsByClassName("div_container_faction_rules"),
            (element) => element.classList.remove("grayscale"))

        style_div_faction.display =  "none"}

    }
