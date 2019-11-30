
var cars=[{'model':'ford','name':'fiesta','price':'$400','year':2019},
           {'model':'mercedes','name':'gle','price':'$600','year':2020},
           {'model':'Audi','name':'A8','price':'$40','year':2021} 
]

document.getElementById('ford').addEventListener('mouseover',ford);
document.getElementById('ford').addEventListener('mouseout',ford1);

function ford(){
	var string='model is'+cars[0]['model']+'name '+cars[0]['name']+'price:'+cars[0]['price'];
	document.getElementById('result').innerHTML=string;
}

function ford1(){
	document.getElementById('result').innerHTML="";

}

document.getElementById('merc').addEventListener('mouseover',merc);
document.getElementById('merc').addEventListener('mouseout',merc1);

function merc(){
	var string='model is '+cars[1]['model']+' name '+cars[1]['name']+' price: '+cars[1]['price'];
	document.getElementById('result').innerHTML=string;
}

function merc1(){
	document.getElementById('result').innerHTML="";

}

document.getElementById('audi').addEventListener('mouseover',audi);
document.getElementById('audi').addEventListener('mouseout',audi1);

function audi(){
	var string='model is '+cars[2]['model']+' name '+cars[2]['name']+' price: '+cars[2]['price'];
	document.getElementById('result').innerHTML=string;
}

function audi1(){
	document.getElementById('result').innerHTML="";

}