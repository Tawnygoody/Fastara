$(document).ready(function(){
    $(".sidenav").sidenav({edge:"right"});
    $('.modal').modal();
    $('.carousel.carousel-slider').carousel({
        fullWidth: true,
        indicators: true
    }, setTimeout(autoplay, 4000));
    AOS.init(); // Initilizes on-scroll library
    $('.tooltipped').tooltip();
    $('select').formSelect();
    validateMaterializeSelect();
    setInterval(changeLink, 100);

});

function autoplay() { // Help with autoplay for carousel taken from https://stackoverflow.com/questions/36581504/materialize-carousel-slider-autoplay
    $('.carousel').carousel('next');
    setTimeout(autoplay, 5000);
}

$("#add-ingredient").on("click", function() {
    new_ingredient = 
    `<div class="input-field new-item">
        <i class="fas fa-trash prefix trash-icon"></i>
        <textarea id="ingredients" name="ingredients" min-length="10" max-length="80" class="materialize-textarea validate content-light" placeholder="New Ingredient" required></textarea>
    </div>`;

    $("#ingredients-container").append(new_ingredient);

    $(".trash-icon").on("click", function() {
        $(this).parent().remove();
    });
    
});

$(".trash-icon").on("click", function() { // needs to be outside the add-ingredient function and add step function as when editing it means something needs to be added before it can be deleted.
    $(this).parent().remove();
});

$("#add-step").on("click", function() {
    new_step = 
    `<div class="input-field new-item">
        <i class="fas fa-trash prefix trash-icon"></i>
        <textarea id="recipe_method" name="recipe_method" min-length="10" max-length="80" class="materialize-textarea validate content-light" placeholder="New Step" required></textarea>
    </div>`;

    $("#method-container").append(new_step);

    $(".trash-icon").on("click", function() {
        $(this).parent().remove();
    });
    
});

function validateMaterializeSelect() {
    let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
    let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
    if ($("select.validate").prop("required")) {
        $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
    }
    $(".select-wrapper input.select-dropdown").on("focusin", function () {
        $(this).parent(".select-wrapper").on("change", function () {
            if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                $(this).children("input").css(classValid);
            }
        });
    }).on("click", function () {
        if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
            $(this).parent(".select-wrapper").children("input").css(classValid);
        } else {
            $(".select-wrapper input.select-dropdown").on("focusout", function () {
                if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                    if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                        $(this).parent(".select-wrapper").children("input").css(classInvalid);
                    }
                }
            });
        }
    });
}


function changeLink() { // thanks to https://stackoverflow.com/questions/10873363/how-to-get-the-href-of-selected-active-tab-using-jquery
    link = $(".carousel-item.active a").prop("href");
    $("#carousel-button").prop("href", link);
}