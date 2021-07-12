$(document).ready(function(){

    /* Initializes Collapsible side nav */
    $(".sidenav").sidenav({edge:"right"});

    /* Initializes Modal */
    $('.modal').modal();

    /* Initializes Carousel & calls autoplay function */
    $('.carousel.carousel-slider').carousel({
        fullWidth: true,
        indicators: true
    }, setTimeout(autoplay, 5000));

    /* Initializes the AOS on scroll library */
    AOS.init();

    /* Initializes Tooltips */
    $('.tooltipped').tooltip();

    /* Initialization for materialize css Select element */
    $('select').formSelect();

    /* Sets an interval for the changeLink function */
    setInterval(changeLink, 100);

});

// Help with autoplay for carousel taken from https://stackoverflow.com/questions/36581504/materialize-carousel-slider-autoplay
/* Autoplay function means carousel items rotate
at 5 second intervals */
function autoplay() {
    $('.carousel').carousel('next');
    setTimeout(autoplay, 5000);
}

/* Adds a new ingredient field whenever add ingredient
button is clicked. Clicking the trash icon removes any 
unwanted ingredient field */
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

/* Needs to be outside the add-ingredient function and 
add step function as when editing it means something needs 
to be added before it can be deleted. */
$(".trash-icon").on("click", function() {
    $(this).parent().remove();
});

/* Adds a new step field whenever add step
button is clicked. Clicking the trash icon removes any 
unwanted step field */
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


$("#recipe-submit").click(function() {
    let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
    let category_name = document.getElementById("category_name").value;

    if (category_name == "Choose your meal") {
        alert("Please select a category for your recipe.");
        $(".select-wrapper").children("input").css(classInvalid);
        return false;
    };
    return true
})


// thanks to https://stackoverflow.com/questions/35786433/how-to-listen-on-select-change-events-in-materialize-css
$("#category_name").on("change", function () {
    let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
    $(".select-wrapper").children("input").css(classValid);
})


// thanks to https://stackoverflow.com/questions/15975586/jquery-change-href-when-image-slider-changes
/* Changes the link to the carousel button so 
that the user is taken to the correct recipe when 
clicking the carousel's view recipe button */
function changeLink() { 
    link = $(".carousel-item.active a").attr("href");
    $("#carousel-button").attr("href", link);
}


// thanks to https://stackoverflow.com/questions/52850091/materialize-select-and-dropdown-touch-event-selecting-wrong-item
/* Prevents touch events from selecting the wrong
option when selecting categories on add recipe and 
edit recipe pages */
$(document).click(function(){
    $('li[id^="select-options"]').on('touchend', function (e) {
        e.stopPropagation();
    });
});