// Import Firebase modules
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.10/firebase-app.js";
import { getAuth, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/9.6.10/firebase-auth.js";
import { getFirestore, doc, getDoc } from "https://www.gstatic.com/firebasejs/9.6.10/firebase-firestore.js";

// 🔹 Your Firebase Configuration
const firebaseConfig = {
    apiKey: "YOUR-API-KEY",
    authDomain: "YOUR-AUTH-DOMAIN",
    projectId: "YOUR-PROJECT-ID",
    storageBucket: "YOUR-STORAGE-BUCKET",
    messagingSenderId: "YOUR-MESSAGING-SENDER-ID",
    appId: "YOUR-APP-ID"
};

// 🔹 Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

// 🔹 Function to Check If User is Admin
const checkAdmin = async (user) => {
    if (!user) {
        window.location.href = "login.html"; // 🔴 Redirect to login if not logged in
        return;
    }

    // 🔹 Check Firestore for Admin Role
    const adminRef = doc(db, "admins", user.uid);
    const adminSnap = await getDoc(adminRef);

    if (adminSnap.exists() && adminSnap.data().role === "admin") {
        console.log("✅ Admin Access Granted");
    } else {
        console.log("❌ Access Denied - Not an Admin");
        window.location.href = "unauthorized.html"; // 🔴 Redirect non-admins
    }
};

// 🔹 Listen for Authentication State Changes
onAuthStateChanged(auth, (user) => {
    checkAdmin(user);
});

// Export Firebase Auth & Firestore
export { auth, db, checkAdmin };
