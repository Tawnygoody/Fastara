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
