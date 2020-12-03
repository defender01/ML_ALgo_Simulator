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


function loginPageOpen(){
  window.location.href = "http://localhost:8000/templates/loginPage.html";
}
