var displayName,email,emailVerified,photoURL,isAnonymous,uid,providerData;
var user;

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

const $element = $('.eye-animation');
// const imagePath = 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/123941';
var imagePath = 'http://127.0.0.1:8000/GradientDescent';
var totalFrames;
var animationDuration;
var timePerFrame = animationDuration / totalFrames;
var timeWhenLastUpdate;
var timeFromLastUpdate;
var frameNumber;
var alpha,startX;
var temp1,temp2,temp3;


function upload(){
  temp1=document.getElementById("startPointID").value;
  temp2=document.getElementById("alphaID").value;
  temp3=document.getElementById("durationID").value;
  if(temp1=="" || temp2== "" ||temp3==""){
    alert("You should fillup all fields!!");
  }
  else{
    startX= parseInt(temp1);
    alpha= parseInt(temp2)/100;
    animationDuration = parseInt(temp3)*1000;
    frameNumber = 0;

  }
  // firebase.database().ref().child('gradientDescent').child("guestUser").set({
  //   startPoint: startX,
  //   alpha: alpha,
  //   runState: 0
  // });

  console.log("startX= "+startX+" alpha= "+alpha);
  var data ='gradientDescent'+'*'+ alpha+'*'+startX;
  // $(function(){
    $.ajax({
        url: "http://127.0.0.1:5000/gradientDescent",
        data: {  "firstname":data,
                  "uid": uid,
                "callingState":"gradientDescent",
              "alpha": alpha,
            "startX":startX},

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
  // });


}

function startSimulation(){
  // create a set of hidden divs
  // and set their background-image attribute to required images
  // that will force browser to download the images

  var ref = firebase.database().ref().child("gradientDescent").child(uid).child('iteration');
    ref.on('value', function(snapshot) {
  // updateStarCount(postElement, snapshot.val());
  totalFrames = parseInt(snapshot.val());
  console.log("iteration no= "+totalFrames);

  });
  console.log("iteration no= "+totalFrames);

  timePerFrame = animationDuration / totalFrames;
  frameNumber=0;

  $(document).ready(() => {
    for (var i = 0; i < totalFrames; i++) {
      $('body').append(`<div id="preload-image-${i}" style="background-image: url('${imagePath}/image${i}.png');"></div>`);
    }
  });


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
    $element.attr('src', imagePath + `/image${frameNumber}.png`);
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



// wait for images to be downloaded and start the animation
// $(window).on('load', () => {
//   requestAnimationFrame(step);
// });


function loginPageOpen(){
  window.location.href = "http://localhost:8000/templates/loginPage.html";
}
