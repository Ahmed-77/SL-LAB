function test()
{
    x=document.getElementById("firstNumber").value
    var array=x.split(" ")
    r=array[0]
    for( var i=1;i<array.length;i++)
    {
        if(r.length<array[i].length)
        {
            r=array[i]
        }
    }
    document.getElementById("result").innerHTML=r
}