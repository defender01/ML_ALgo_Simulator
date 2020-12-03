var displayName,email,emailVerified,photoURL,isAnonymous,uid,providerData;
var user,choice;

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

    console.log("onAuthStateChanged "+email+" "+name);
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


// for showing animation//////////////////////////////////////

const simulationImage = $('#simulationId');
const costImage = $('#costfunctionID');
// const imagePath = 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/123941';
var imagePath = 'http://127.0.0.1:8000/PolynomialFitting';
var totalFrames;
var animationDuration;
var timePerFrame;
var timeWhenLastUpdate;
var timeFromLastUpdate;
var frameNumber;
var temp1,temp2;

function startSimulation(){
  // create a set of hidden divs
  // and set their background-image attribute to required images
  // that will force browser to download the images
  totalFrames=31;
    temp1=document.getElementById("durationID").value;
    if(temp1==""){
      alert("You should fillup all fields!!");
    }
    else{
      animationDuration = parseInt(temp1)*1000;
      frameNumber = 0;

    }


  console.log("iteration no= "+totalFrames);

  timePerFrame = animationDuration / totalFrames;
  frameNumber=0;

  if(choice==0){
    $(document).ready(() => {
      for (var i = 0; i < totalFrames; i++) {
        $('body').append(`<div id="preload-image-simulationImage-${i}" style="background-image: url('${imagePath}/Default/image${i}.png');"></div>`);
        $('body').append(`<div id="preload-image-costImage-${i}" style="background-image: url('${imagePath}/Default/cost${i}.png');"></div>`);
      }
    });

  }
  else{
    $(document).ready(() => {
      for (var i = 0; i < totalFrames; i++) {
        $('body').append(`<div id="preload-image-customized-simulationImage-${i}" style="background-image: url('${imagePath}/image${i}.png');"></div>`);
        $('body').append(`<div id="preload-image-customized-costImage-${i}" style="background-image: url('${imagePath}/cost${i}.png');"></div>`);
      }
    });

  }



  // call for Simulation
  requestAnimationFrame(step);
}


// 'step' function will be called each time browser rerender the content
// we achieve that by passing 'step' as a parameter to the 'requestAnimationFrame' function
function step(startTime) {
  // 'startTime' is provided by requestAnimationName function, and we can consider it as current time
  // first of all we calculate how much time has passed from the last time when frame was update
  if (!timeWhenLastUpdate) timeWhenLastUpdate = startTime;
  timeFromLastUpdate = startTime - timeWhenLastUpdate;

  // then we check if it is time to update the frame
  if (timeFromLastUpdate > timePerFrame) {
    // and update it accordingly
    if(choice==0){
      simulationImage.attr('src', imagePath + `/Default/image${frameNumber}.png`);
      costImage.attr('src', imagePath + `/Default/cost${frameNumber}.png`);
    }
    else{
      simulationImage.attr('src', imagePath + `/image${frameNumber}.png`);
      costImage.attr('src', imagePath + `/cost${frameNumber}.png`);
    }
    // reset the last update time
    timeWhenLastUpdate = startTime;

    // then increase the frame number or reset it if it is the last frame
    if (frameNumber >= totalFrames-1) {
      return;
    } else {
      frameNumber = frameNumber + 1;
    }
  }



  requestAnimationFrame(step);
}




// choice of simulation

$("input[id='defaultID']").click(function(){
  console.log("default is chossen");
  $("input[id='customizedID']").prop('checked',false);
  choice=0;
});
$("input[id='customizedID']").click(function(){
  console.log("customized is chossen");
      $("input[id='defaultID']").prop('checked',false);
      choice=1;
});

$(window).on('load', () => {
  choice=0;
});

function enterData(){
  window.location.href = "http://localhost:8000/templates/takeInput.html";
}

function loginPageOpen(){
  window.location.href = "http://localhost:8000/templates/loginPage.html";
}
