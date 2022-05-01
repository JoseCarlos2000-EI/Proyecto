    var $contain_business=$("#catalog-business");
    var $load=$("#loader");
    $.ajax({
        url: UrlListEmpresa,
        method: 'GET',
        success: function(data){
            console.log(data);
            var html="";
            data.forEach(function (empresa){
                console.log(empresa.name);
                html=html+ '   <div  class="single-products-catagory clearfix">'
                +'<a href="'+empresa.urlCategoria+'">'
                    +'<img  src="'+empresa.image+'" alt="">'
                    +'<div class="hover-content">'
                        +'<div class="line"></div>'
                        +'<h4>'+empresa.name+'</h4>'
                    +'</div>'
                +'</a>'
            +'</div>';
         });
         console.log(html);
         $contain_business.html(html);
         $load.hide();
        },
        error: function(){
            alert('Error');
        }
        
    });
