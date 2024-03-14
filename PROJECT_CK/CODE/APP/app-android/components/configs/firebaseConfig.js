// Import the functions you need from the SDKs you need
import firebase from 'firebase/compat/app'
import {getDatabase} from 'firebase/database'
const firebaseConfig = {
    apiKey: "AIzaSyCd2D-DPLJHVVGQPWx8jIRYVyng2zOzmPY",
    authDomain: "final-project-tthtn.firebaseapp.com",
    databaseURL: "https://final-project-tthtn-default-rtdb.firebaseio.com",
    projectId: "final-project-tthtn",
    storageBucket: "final-project-tthtn.appspot.com",
    messagingSenderId: "165270503770",
    appId: "1:165270503770:web:3f519fe78472e05ca27363",
    measurementId: "G-BL2N64RRE4"
};
if(firebase.apps.length === 0){
    firebase.initializeApp(firebaseConfig)
}
const db = getDatabase()
export {db}