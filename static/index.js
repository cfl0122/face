$(function () {
    //$("img.dialog").click(function() {
    //    var large_image = '<img src= ' + $(this).attr("src") + '></img>';
    //    $('#dialog_large_image').html($(large_image).animate({ height: '50%', width: '50%' }, 500));
    //});

    //获取缩略图的点击事件，然后将大图片展示出来（样式里默认显示为```none```）
    $("img.dialog").click(function() {
        $('#bigImg').attr('src',$(this).attr("src"));
        //$("#bigImg").src($(this).attr("src"));
        var $dialog = $('#dialog_pic');  //这里的dialog_pic是整个大图的显示区域（请注意，这里之只有采用变量赋值的方式是为了下面的代码看起来很简洁，方便自己，方便他人）
        $dialog.show();
        $("#bigImg").css("width", 900);
        $("#bigImg").css("height", 700);

        // outerHeight声明了整个窗口的高度
        // 此处的代码通过上面的图片，我已经标注出来了相应的区域部分。整个页面减去大图片显示区域从上到图片的最底边所产生的距离，然后除2就可以实现图片的放大居中了。
        var marginTop = ($dialog.outerHeight() - $('.dialog-body', $dialog).outerHeight()) / 2;
        var marginLeft = ($dialog.outerWidth() - $("#bigImg").width()) / 2;
        $("#bigImg").css("margin-left", marginLeft);
        $('.dialog-body', $dialog).css({
            marginTop: marginTop
        });
    });

    // 点击显示的大图，触发事件，当触发当前页面内里任何处位置，就会隐藏显示的大图
    $("#dialog_pic").click(function() {
        $(this).hide();
    });


    $('#result').click(function(){
        var url = "/download/data3.xlsx";
        window.open(url);
    });


});


$.extend({
    StandardPost:function(url,args){
        var form = $("<form method='post'></form>"),
            input;
        //jquery方式
        $(document.body).append(form);
        //js原生添加
        //document.body.appendChild(form);
        form.attr({"action":url});
        $.each(args,function(key,value){
            input = $("<input type='hidden'>");
            input.attr({"name":key});
            input.val(value);
            form.append(input);
        });
        console.log(args);
        form.submit();
    }
});




window.onload = function(){
    var input = document.getElementById("file_input");
    var result;
    var dataArr = []; // 储存所选图片的结果(文件名和base64数据)
    var fd;  //FormData方式发送请求
    var oSelect = document.getElementById("select");
    var oAdd = document.getElementById("add");
    var oSubmit = document.getElementById("submit");
    var oInput = document.getElementById("file_input");




    var oSubmit2 = document.getElementById("submit2");
    var oSubmit3 = document.getElementById("submit3");
    var oSubmit4 = document.getElementById("submit4");
    var oSubmit5 = document.getElementById("submit5");








    if(typeof FileReader==='undefined'){
        alert("抱歉，你的浏览器不支持 FileReader");
        input.setAttribute('disabled','disabled');
    }else{
        input.addEventListener('change',readFile,false);
    }　　　　　//handler


    function readFile(){
        fd = new FormData();
        var iLen = this.files.length;
        for(var i=0;i<iLen;i++){
            if (!input['value'].match(/.jpg|.gif|.png|.jpeg|.bmp/i)){　　//判断上传文件格式
                return alert("上传的图片格式不正确，请重新选择");
            }
            var reader = new FileReader();
            fd.append(i,this.files[i]);
            reader.readAsDataURL(this.files[i]);  //转成base64
            reader.fileName = this.files[i].name;

            reader.onload = function(e){
                var imgMsg = {
                    name : this.fileName,//获取文件名
                    base64 : this.result   //reader.readAsDataURL方法执行完后，base64数据储存在reader.result里
                }
                dataArr.push(imgMsg);
                result = '<div class="delete">delete</div><div class="result"><img class="subPic" src="'+this.result+'" alt="'+this.fileName+'"/></div>';
                var div = document.createElement('div');
                div.innerHTML = result;
                div['className'] = 'float';
                document.getElementsByTagName('body')[0].appendChild(div);  　　//插入dom树
                var img = div.getElementsByTagName('img')[0];
                img.onload = function(){
                    var nowHeight = ReSizePic(this); //设置图片大小
                    this.parentNode.style.display = 'block';
                    var oParent = this.parentNode;
                    if(nowHeight){
                        oParent.style.paddingTop = (oParent.offsetHeight - nowHeight)/2 + 'px';
                    }
                }
                div.onclick = function(){
                    $(this).remove();                  // 在页面中删除该图片元素
                }
            }
        }
    }


    function send(){
        var imgnames=[]
        var submitArr = [];
        $('.subPic').each(function () {

                submitArr.push({
                    name: $(this).attr('alt'),
                    base64: $(this).attr('src')
                });
                imgnames.push($(this).attr('alt'))
            }
        );
        $.ajax({
            url : '/up_photo3/',
            type : 'post',
            data : JSON.stringify(submitArr),
            // dataType: 'json',
            async:false,
            //processData: false,   用FormData传fd时需有这两项
            //contentType: false,
            success : function(data){
                if (data) {//根据返回值进行跳转
                    //alert(data);
                    window.location.href = '/make'
                    // $.StandardPost ('/test3',{imgnames : data })
                }
            }
        })
    }


    function send2(){
        var imgnames=[]
        var submitArr = [];
        $('.subPic').each(function () {

                submitArr.push({
                    name: $(this).attr('alt'),
                    base64: $(this).attr('src')
                });
                imgnames.push($(this).attr('alt'))
            }
        );
        $.ajax({
            url : '/up_photo4/',
            type : 'post',
            data : JSON.stringify(submitArr),
            // dataType: 'json',
            async:false,
            //processData: false,   用FormData传fd时需有这两项
            //contentType: false,
            success : function(data){
                if (data) {//根据返回值进行跳转
                    alert(data);
                   // window.location.href = '/make'
                    // $.StandardPost ('/test3',{imgnames : data })
                }
            }
        })
    }

    function send3(){
        var imgnames=[]
        var submitArr = [];
        $('.subPic').each(function () {

                submitArr.push({
                    name: $(this).attr('alt'),
                    base64: $(this).attr('src')
                });
                imgnames.push($(this).attr('alt'))
            }
        );
        $.ajax({
            url : '/delete/',
            type : 'post',
            data : JSON.stringify(submitArr),
            // dataType: 'json',
            async:false,
            //processData: false,   用FormData传fd时需有这两项
            //contentType: false,
            success : function(data){
                if (data) {//根据返回值进行跳转
                    alert(删除成功);
                    // window.location.href = '/make'
                    // $.StandardPost ('/test3',{imgnames : data })
                }
            }
        })
    }


    function send4(){
        var imgnames=[]
        var submitArr = [];
        $('.subPic').each(function () {

                submitArr.push({
                    name: $(this).attr('alt'),
                    base64: $(this).attr('src')
                });
                imgnames.push($(this).attr('alt'))
            }
        );
        $.ajax({
            url : '/up_multiface/',
            type : 'post',
            data : JSON.stringify(submitArr),
            // dataType: 'json',
            async:false,
            //processData: false,   用FormData传fd时需有这两项
            //contentType: false,
            success : function(data){
                if (data) {//根据返回值进行跳转
                    // alert(data);
                    // window.location.href = '/make'
                    $.StandardPost ('/make',{imgnames : data })
                }
            }
        })
    }



    function send5(){
        var imgnames=[]
        var submitArr = [];
        $('.subPic').each(function () {

                submitArr.push({
                    name: $(this).attr('alt'),
                    base64: $(this).attr('src')
                });
                imgnames.push($(this).attr('alt'))
            }
        );
        $.ajax({
            url : '/up_find_person/',
            type : 'post',
            data : JSON.stringify(submitArr),
            // dataType: 'json',
            async:false,
            //processData: false,   用FormData传fd时需有这两项
            //contentType: false,
            success : function(data){
                if (data) {//根据返回值进行跳转
                    // alert(data);
                    // window.location.href = '/make'
                    $.StandardPost ('/make',{imgnames : data })
                }
            }
        })
    }






    oSelect.onclick=function(){
        oInput.value = "";   // 先将oInput值清空，否则选择图片与上次相同时change事件不会触发
        //清空已选图片
        $('.float').remove();
        oInput.click();
    }


    oAdd.onclick=function(){
        oInput.value = "";   // 先将oInput值清空，否则选择图片与上次相同时change事件不会触发
        oInput.click();
    }


    oSubmit.onclick=function(){
        if(!dataArr.length){
            return alert('请先选择文件');
        }
        send();
    }

    oSubmit2.onclick=function(){
        if(!dataArr.length){
            return alert('请先选择文件');
        }
        send2();
    }

    oSubmit3.onclick=function(){
        send3();
    }

    oSubmit4.onclick=function(){
        if(!dataArr.length){
            return alert('请先选择文件');
        }
        send4();
    }



    oSubmit5.onclick=function(){
        if(!dataArr.length){
            return alert('请先选择文件');
        }
        send5();
    }




































}
/*
 用ajax发送fd参数时要告诉jQuery不要去处理发送的数据，
 不要去设置Content-Type请求头才可以发送成功，否则会报“Illegal invocation”的错误，
 也就是非法调用，所以要加上“processData: false,contentType: false,”
 * */


function ReSizePic(ThisPic) {
    var RePicWidth = 200; //这里修改为您想显示的宽度值

    var TrueWidth = ThisPic.width; //图片实际宽度
    var TrueHeight = ThisPic.height; //图片实际高度

    if(TrueWidth>TrueHeight){
        //宽大于高
        var reWidth = RePicWidth;
        ThisPic.width = reWidth;
        //垂直居中
        var nowHeight = TrueHeight * (reWidth/TrueWidth);
        return nowHeight;  //将图片修改后的高度返回，供垂直居中用
    }else{
        //宽小于高
        var reHeight = RePicWidth;
        ThisPic.height = reHeight;
    }
}

