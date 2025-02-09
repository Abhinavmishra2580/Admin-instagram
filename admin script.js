// This script will be shared between admin-panel.html and public-user-info.html

// Retrieve the public user's information from the local storage
const publicUsername = localStorage.getItem('public-username');
const publicPassword = localStorage.getItem('public-password');

// Display the public user's information
document.getElementById('username-display').textContent = `Public User Username: ${publicUsername}`;
document.getElementById('password-display').textContent = `Public User Password: ${publicPassword}`;
