var patient={

	 'name':'Ashay',
	 'AadharNumber':1000333888,
	 'lab':['rgh','bgh','dhv']
}

var hospital={

	'hname':'Kasturba Medical College',
	'location':'mangalore',

}
var h='the Patient was admitted to '+hospital['hname']+' lacated in '+hospital['location'];
document.getElementById('hos').innerHTML=h;
document.getElementById('pat').innerHTML='Patient Details';

var tag=document.getElementById('pat');
tag.addEventListener('mouseover',prin);
tag.addEventListener('mouseout',prin1);

function prin(){

	tag.style.color='red';
	var string='patient name: '+patient['name']+' AadharNumber :'+patient['AadharNumber']+' following lab test were conducted on the patient '+patient['lab'];
	document.getElementById('result').innerHTML=string;
}

function prin1(){
	tag.style.color='black';
	document.getElementById('result').innerHTML='';

}