var displayName,email,emailVerified,photoURL,isAnonymous,uid,providerData;
var user,from;


firebase.auth().onAuthStateChanged(function(user) {
  if (user) {
    // User is signed in.
    displayName = user.displayName;
    email = user.email;
    emailVerified = user.emailVerified;
    photoURL = user.photoURL;
    isAnonymous = user.isAnonymous;
    uid = user.uid;
    providerData = user.providerData;
    document.getElementById("loginID").style.display = "none";
    document.getElementById("logoutID").style.display = "block";

    console.log("Welcome :"+ email+" user logged in");

    alert("onAuthStateChanged "+email+" "+name);
    // window.location.href = "https://www.google.com";

  } else {
    // User is signed out.
    // ...
    displayName = null;
    email = null;
    emailVerified = null;
    photoURL = null;
    isAnonymous = null;
    uid = null;
    providerData = null;

    document.getElementById("loginID").style.display = "block";
    document.getElementById("logoutID").style.display = "none";

    // document.getElementById("loggedInUser").style.display = "none";
    // document.getElementById("loggedOutUser").style.display = "block";
    console.log(" user logged out");
    alert("onAuthStateChanged else "+email+" "+name);
  }
});

function logout(){
  alert("logout attempted");
  firebase.auth().signOut().then(function() {
// Sign-out successful.
}).catch(function(error) {
  alert("Error: "+error.message);
});
  alert("logout "+email+"  "+password);
}

//for canvas.......................................................................................

//for canvas
var canvasTop,canvasLeft,canvasWidth,canvasHeight;
var pointArray = [];
function draw() {
  pointArray = [];
  $(document).ready(function(){
  // $("button").click(function(){
    var x = $("canvas").offset();
    canvasTop = (parseInt(x.top));
    canvasLeft = (parseInt(x.left));
    console.log("Top: " + canvasTop + " Left: " + canvasLeft + "canvas.getBoundingClientRect().top  ");
  // });
  });

      var dataSetTextArea = document.getElementById
      var canvas = document.getElementById('canvas');
      canvasHeight=canvas.height;
      canvasWidth=canvas.width;

      if (canvas.getContext) {
        var context = canvas.getContext('2d');

        for(var x=0.5;x<500;x+=10) {
          context.moveTo(x,0);
          context.lineTo(x,500);
        }

        for(var y=0.5; y<500; y+=10) {
          context.moveTo(0,y);
          context.lineTo(500,y);

      }

      context.strokeStyle='grey';
      context.stroke();


      context.beginPath();
      context.moveTo(canvas.width/2,0);
      context.lineTo(canvas.width/2,canvas.height);
      context.moveTo(0,canvas.height/2);
      context.lineTo(canvas.width,canvas.height/2);
      context.strokeStyle = "blue";
      context.stroke();

  }

}

function showCoords(canvas,event) {
  var rect = canvas.getBoundingClientRect();
    var posX = (event.clientX-rect.left).toFixed(2);
    var posY = (event.clientY-rect.top).toFixed(2);
    var x = (posX-canvasWidth/2).toFixed(2);
    var y = (canvasHeight/2 - posY).toFixed(2);

    pointArray.push([x,y]);

  $("document").ready(function(){
    $('.userInputTextArea').append(x+","+y+"\n");
  });
    // console.log("x= "+pointArray[pointArray.length-1][0]+"y= "+pointArray[pointArray.length-1][1]);
    console.log("x= "+posX+"y= "+posY);

    var coords = "X coordinates: " + x + ", Y coordinates: " + y;

    // printing dots in canvas start
    var canvas = document.getElementById('canvas');
    var context = canvas.getContext('2d');
    context.beginPath();
    context.arc(posX , posY, 1 , 0, 2 * Math.PI);
    context.strokeStyle = "red";
    context.stroke();
    // printing dots in canvas end


  }
  // .........................................................................................../


function getInput()
{
  var data="";
  var lines = $('.userInputTextArea').val().split('\n');
  for(var i = 0;i < lines.length;i++){
      //code here using lines[i] which will give you each line
      lines[i]=lines[i].trim();
      if(lines[i].length){
        if(data.length == 0){
        data+=lines[i].trim();
        console.log(lines[i]+" lene.length ="+lines[i].length+" data = "+ data);
      }
        else{
        data+=("*"+lines[i].trim());
        console.log(lines[i]+" lene.length ="+lines[i].length+" data = "+ data);
      }
      }
  }

  if(from=="linearRegression"){
    $.ajax({
        url: "http://127.0.0.1:5000/linearRegression",
        data: {  "firstname":data,
                  "uid": uid,
                "callingState":from},
        // contentType: 'application/json;charset=UTF-8',
        // dataType: "json",
        type: "POST",
        success: function(response) {
            console.log("response found" +response);
        },
        error: function(error) {
            console.log(error);
        }
    });

  }
  else{
    $.ajax({
        url: "http://127.0.0.1:5000/polynomialRegression",
        data: {  "firstname":data,
                  "uid": uid,
                "callingState":from},
        // contentType: 'application/json;charset=UTF-8',
        // dataType: "json",
        type: "POST",
        success: function(response) {
            console.log("response found" +response);
        },
        error: function(error) {
            console.log(error);
        }
    });
  }


//   $(document).ready(function () {
//     var val = $.trim($("#userInputTextAreaID").val());
//     if (val != "") {
//         console.log(val);
//     }
// });
}
function getBack()
{
   window.history.back();
}

function loginPageOpen(){
  window.location.href = "http://localhost:8000/templates/loginPage.html";
}

$(window).on('load', () => {
  var str = document.referrer;
  var words= str.split('/');
  var word=words[words.length-1].split('.');
  from = word[0];
  console.log("from = "+from +"previous= "+from);
});
