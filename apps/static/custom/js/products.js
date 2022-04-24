$(document).ready(function() {
    var $contain_products=$("#catalog-products");
    $.ajax({
        url:UrlListProducto,
        method:"GET",
        data:{
            "idEmpresa":idEmpresa,
            "idCategoria":idCategoria,
        },
        success: function(data){
            console.log(data);
            var html ="";
            data.forEach(function(producto){
                html = html +'<div class="col-12 col-sm-6 col-md-12 col-xl-6">'
                +'<div class="single-product-wrapper">'
                    +'<div class="product-img">'
                        +'<img src="'+producto.image1+'" alt="">'
                        +'<img class="hover-img" src="'+producto.image2+'" alt="">'
                    +'</div>'

                    +'<div class="product-description d-flex align-items-center justify-content-between">'
                        +'<div class="product-meta-data">'
                            +'<div class="line"></div>'
                            +'<p class="product-price">S/. 180.00</p>'
                            +'<a href="product-details.html">'
                                +'<h6>Modern Chair</h6>'
                            +'</a>'
                        +'</div>'
                        
                        +'<div class="ratings-cart text-right">'
                            +'<div class="ratings">'
                                +'<i class="fa fa-star" aria-hidden="true"></i>'
                                +'<i class="fa fa-star" aria-hidden="true"></i>'
                                +'<i class="fa fa-star" aria-hidden="true"></i>'
                                +'<i class="fa fa-star" aria-hidden="true"></i>'
                                +'<i class="fa fa-star" aria-hidden="true"></i>'
                            +'</div>'
                            +'<div class="cart">'
                                +'<a href="cart.html" data-toggle="tooltip" data-placement="left" title="Add to Cart"><img src="" alt=""></a>'
                            +'</div>'
                        +'</div>'
                    +'</div>'
                +'</div>'
            +'</div>';
            });
            console.log(html);
            $contain_products.html(html);
        },
        error: function(){
            alert("Error");
        }
    });
});