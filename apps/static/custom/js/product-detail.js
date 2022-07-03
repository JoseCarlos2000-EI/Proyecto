$(document).ready(function() {
    var $contain_product_details_1=$("#Product-Details-1");
    var $contain_product_details_2=$("#Product-Details-2");
    var $item_product = $("#AgregaItem");
    var $qty = $("#qty");
    var $load=$("#loader");
    if (localStorage.getItem("carrito")!=null){
        var carrito = JSON.parse(localStorage.getItem("carrito"));
        console.log(carrito);
    }
    else{
        var carrito = new Array(); 
    }
     
    var item = {};
    $.ajax({
        url:UrlProductoDetalle,
        method: 'GET',
        data:{"idProducto":idProducto},
        success: function(data){
            //console.log(data);
            var html1="";
            var html2="";
            data.forEach(function (producto){
                html1=html1+'<div id="product_details_slider" class="carousel slide" data-ride="carousel"> <ol class="carousel-indicators">'
                +'<li class="active" data-target="#product_details_slider" data-slide-to="0" style="background-image: url('+producto.image1+');">'
                +'</li>'
                +'<li data-target="#product_details_slider" data-slide-to="1" style="background-image: url('+producto.image2+');">'
                +'</li>'
                +'<li data-target="#product_details_slider" data-slide-to="2" style="background-image: url('+producto.image3+');">'
                +'</li>'
                +'<li data-target="#product_details_slider" data-slide-to="3" style="background-image: url('+producto.image4+');">'
                +'</li>'
            +'</ol>'
            +'<div class="carousel-inner">'
                +'<div class="carousel-item active">'
                    +'<a class="gallery_img" href="'+producto.image1+'">'
                        +'<img class="d-block w-100" src="'+producto.image1+'" alt="First slide">'
                    +'</a>'
                +'</div>'
                +'<div class="carousel-item">'
                    +'<a class="gallery_img" href="'+producto.image2+'">'
                        +'<img class="d-block w-100" src="'+producto.image2+'" alt="Second slide">'
                    +'</a>'
                +'</div>'
                +'<div class="carousel-item">'
                    +'<a class="gallery_img" href="'+producto.image3+'">'
                        +'<img class="d-block w-100" src="'+producto.image3+'" alt="Third slide">'
                    +'</a>'
                +'</div>'
                +'<div class="carousel-item">'
                    +'<a class="gallery_img" href="'+producto.image4+'">'
                        +'<img class="d-block w-100" src="'+producto.image4+'" alt="Fourth slide">'
                    +'</a>'
                +'</div>'
            +'</div>'
            +'</div>';

            html2 = html2 +'<div class="product-meta-data">'
            +'<div class="line"></div>'
            +'<p class="product-price">S/. '+producto.price+'</p>'
            +'<a href="product-details.html">'
                +'<h6>'+producto.name+'</h6>'
            +'</a>'
            +'<div class="ratings-review mb-15 d-flex align-items-center justify-content-between">'
                +'<div class="ratings">'
                    +'<i class="fa fa-star" aria-hidden="true"></i>'
                    +'<i class="fa fa-star" aria-hidden="true"></i>'
                    +'<i class="fa fa-star" aria-hidden="true"></i>'
                    +'<i class="fa fa-star" aria-hidden="true"></i>'
                    +'<i class="fa fa-star" aria-hidden="true"></i>'
                +'</div>'

            +'</div>'
            +'<p class="avaibility"><i class="fa fa-circle"></i> En Stock</p>'
        +'</div>'

        +'<div class="short_overview my-5">'
            +'<p>'+producto.description+'</p>'
       +'</div>';
                item = {
                    "id": producto.id,
                    "name": producto.name,
                    "price": producto.price,
                    "image": producto.image1
                };
                console.log(item);
            });

            $contain_product_details_1.html(html1);
            $contain_product_details_2.html(html2);
            $load.hide();
        },
        complete: function(){
            $item_product.click(function(){    
            
            if (carrito.length > 0){
                carrito.forEach(function(p_item){
                    if(p_item.id === item.id){
                        p_item.quantity += parseInt($qty.val()); 
                                           
                        
                    }
                    
                    else{
                        if (((carrito.filter(i => i.id === item.id).length) ? true :false) === false)
                        {
                            item.quantity = parseInt($qty.val());
                            carrito.push(item); 
                        }
                    }
                })   
            }
            else{
                item.quantity = parseInt($qty.val());
                carrito.push(item);
            }               

            localStorage.setItem("carrito", JSON.stringify(carrito)); 

            });
           
        },
        error: function(){
            alert("Error");
        }
    });
});