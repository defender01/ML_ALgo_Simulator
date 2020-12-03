var displayName,email,emailVerified,photoURL,isAnonymous,uid,providerData;
var currentUser;


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

    document.getElementById("loggedInUser").style.display = "block";
    document.getElementById("loggedOutUser").style.display = "none";
    document.getElementById("loggedInUser").innerHTML = "Welcome :"+ email;

    alert("onAuthStateChanged "+email+" "+name+ " uid = "+uid);
    // firebase.database().ref().child('gradientDescent').child(uid).set({
    //   iteration : 50
    // });

    window.location.href = "http://localhost:8000/templates/home.html";

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

    document.getElementById("loggedInUser").style.display = "none";
    document.getElementById("loggedOutUser").style.display = "block";
    alert("onAuthStateChanged else "+email+" "+name);
  }
});



/*
Log in
*/
function login(){
  var userEmail = document.getElementById("emailIDLogin").value;
  var userPassword = document.getElementById("passwordIDLogin").value;
  alert(" this is ppp  login "+userEmail+"  "+userPassword+" ");
  firebase.auth().signInWithEmailAndPassword(userEmail, userPassword).catch(function(error) {
    // Handle Errors here.
    var errorCode = error.code;
    var errorMessage = error.message;
    alert("Error: "+errorMessage);
  });
   alert("login "+userEmail+"  "+userPassword);

}
function signup(){
  var userEmail = document.getElementById("emailIDSignup").value;
  var userPassword = document.getElementById("passwordIDSignup").value;
  var userName = document.getElementById("userNameID").value;
  console.log("signup "+userEmail+"  "+userPassword+" "+userName);
    firebase.auth().createUserWithEmailAndPassword(userEmail, userPassword).catch(function(error) {
    // Handle Errors here.
    var errorCode = error.code;
    var errorMessage = error.message;
    alert(errorMessage);
  });
  alert("signup "+userEmail+"  "+userPassword+" "+userName);
  alert("signup "+userEmail+"  "+userPassword);
  alert("its here");
}
function logout(){
  alert("logout attempted");
  firebase.auth().signOut().then(function() {
// Sign-out successful.
}).catch(function(error) {
  alert("Error: "+error.message);
});
alert("signed out");
}

function loginPageOpen(){
  window.location.href = "http://localhost:8000/templates/loginPage.html";
}
