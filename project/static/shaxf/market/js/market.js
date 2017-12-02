$(function(){
   //全部分类的显示与隐藏
   $('#alltypebtn').bind('click', function(e){
        $('#typediv').toggle()
        $('#sortdiv').hide()
   })
    //排序的显示与隐藏
   $('#showsortbtn').bind('click', function(e){
        $('#sortdiv').toggle()
        $('#typediv').hide()
   })

   $('#sortdiv, #typediv').bind('click', function(e){
       $(this).hide()
   })
})
