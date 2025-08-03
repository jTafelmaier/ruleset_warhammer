



function calculate_winning_state() {

    function set_texts(function_get_text) {

        function set_text(
            text_side,
            index) {

            element = document
                .getElementsByClassName(text_side)[0]
                .getElementsByClassName("outcome")[0]

            text = function_get_text(index)

            element.textContent = text
            element.classList = "outcome " + text
        }

        [
            "left",
            "right"]
            .forEach(set_text)
        }

    function determine_winning(property) {

        function get_int_value(text_side) {

            return parseInt(document
                .getElementsByClassName(text_side)[0]
                .getElementsByClassName(property)[0]
                .getElementsByClassName("value")[0]
                .textContent)
        }

        let int_difference = get_int_value("left") - get_int_value("right")

        if (int_difference == 0) {
            return false
        }

        let array_winning = [
            "winning",
            "losing"]

        if (int_difference < 0) {
            array_winning.reverse()
        }

        set_texts(index => array_winning[index])

        return true
    }

    if (determine_winning("victory_points")) {
        return
    }
    if (determine_winning("model_points")) {
        return
    }

    set_texts(index => "draw")
}


function update_victory_points(
    text_side,
    int_change) {

    let element_victory_points = document
        .getElementsByClassName(text_side)[0]
        .getElementsByClassName("victory_state")[0]
        .getElementsByClassName("value")[0]

    element_victory_points.textContent = Math.max(0, parseInt(element_victory_points.textContent) + int_change).toString()

    calculate_winning_state()
}


function calculate_points_total(
    text_side) {

    let int_points_cost_total = Array.from(document
        .getElementsByClassName(text_side)[0]
        .getElementsByClassName("unit_army_list"))
        .map(element => parseInt(element.getElementsByClassName("count_current")[0].textContent) * parseInt(element.getAttribute("points_per_model")))
        .reduce((a, b) => a + b)

    document
        .getElementsByClassName(text_side)[0]
        .getElementsByClassName("model_points")[0]
        .getElementsByClassName("value")[0]
        .textContent = int_points_cost_total.toString()

    calculate_winning_state()
}


function setup_health_bars() {

    function setup_health_bar(
        element_unit) {

        let element_health_bar = element_unit
            .getElementsByClassName("health_bar")[0]

        let array_tokens = Array.from(element_health_bar
            .getElementsByClassName("token"))

        function set_triggers(
            element_token,
            index_token) {

            function set_class_health_tokens(
                text_class) {

                array_tokens
                    .slice(0, index_token)
                    .forEach(element => element.classList.add(text_class))

                array_tokens
                    .slice(index_token, array_tokens.length)
                    .forEach(element => element.classList.remove(text_class))
            }

            function save_health_bar() {

                set_class_health_tokens("used")

                if (index_token == array_tokens.length - 1) {
                    element_health_bar.classList.add("red")
                } else {
                    element_health_bar.classList.remove("red")
                }
            }

            element_token.addEventListener("mouseenter", () => set_class_health_tokens("preview_used"))
            element_token.addEventListener("click", save_health_bar)
            }

        element_health_bar
            .addEventListener("mouseleave", () => array_tokens.forEach(element => element.classList.remove("preview_used")))

        array_tokens
            .forEach(set_triggers)
    }

    Array.from(document
        .getElementsByClassName("unit_army_list"))
        .forEach(setup_health_bar)
}


function initialise() {

    setup_health_bars()
    calculate_points_total("left")
    calculate_points_total("right")

}


function update_count_models(
    text_side,
    index_row,
    bool_increase) {

    let element_unit = document
        .getElementsByClassName(text_side)[0]
        .getElementsByClassName("unit_army_list")[index_row]

    let element_count_models = element_unit
        .getElementsByClassName("count_current")[0]

    var int_count_models_current = parseInt(element_count_models.textContent)
    let int_count_models_initial = parseInt(element_count_models.getAttribute("initial"))

    if (bool_increase) {
        if (int_count_models_current >= int_count_models_initial) {
            return
        }
        var int_count_models_new = int_count_models_current + 1

        element_unit
            .classList
            .remove("destroyed")
    } else {
        if (int_count_models_current <= 0) {
            return
        } else if (int_count_models_current == 1) {
            element_unit
                .classList
                .add("destroyed")
        }
        var int_count_models_new = int_count_models_current - 1
    }

    element_count_models.textContent = int_count_models_new
        .toString()

    calculate_points_total(text_side)
}


function toggle_inactive(
    text_side,
    index_row) {

    document
        .getElementsByClassName(text_side)[0]
        .getElementsByClassName("unit_army_list")[index_row]
        .classList
        .toggle("inactive")

}

function next_turn() {

    Array.from(document
        .getElementsByClassName("unit_army_list"))
        .forEach(element => element.classList.remove("inactive"))

}

