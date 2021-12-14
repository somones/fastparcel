importScripts("https://www.gstatic.com/firebasejs/8.2.1/firebase-app.js");
importScripts("https://www.gstatic.com/firebasejs/8.2.1/firebase-messaging.js");

firebase.initializeApp({
  apiKey: "AIzaSyCaETMLHNr-7byzxHxIuMKyNgQIS_Iz3g8",
  authDomain: "fastparcel-75843.firebaseapp.com",
  projectId: "fastparcel-75843",
  storageBucket: "fastparcel-75843.appspot.com",
  messagingSenderId: "623427609842",
  appId: "1:623427609842:web:1bb75dbf6b20809d59dc6b"
});

const messaging = firebase.messaging();