$(document).ready(function() {
    var $contain_categories=$("#catalog-categories");
    $.ajax({
        url: UrlListaCategorias,
        method: 'GET',
        data:{'id': IdEmpresa},
        success: function(data){
            console.log(data);
            var html="";
            data.forEach(function (categories){
                console.log(categories.name);
                html=html+ '<div class="single-products-catagory clearfix">'
                +'<a href='+categories.urlTienda+'>'
                    +'<img src="'+categories.image+'" alt="">'
                    +'<div class="hover-content">'
                        +'<div class="line"></div>'
                        +'<p>Desde S/. '+categories.minPrice+'</p>'
                        +'<h4>'+categories.name+'</h4>'
                    +'</div>'
                +'</a>'
            +'</div>';
         });
         console.log(html);
         $contain_categories.html(html);
        },
        error: function(){
            alert("Error");
        }
    });
});