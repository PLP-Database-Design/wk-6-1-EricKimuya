# Power Testers — Phase 2 Test Cases
**Project:** Bookstore Project  
**Date:** November 11, 2025  
**Team:** Power Testers  

---

✅ **Test Case**  
**ID:** TC-001  
**Title:** Verify book search returns relevant results  
**Pre-conditions:** User is on the homepage; sample book data is loaded  
**Steps:**  
1. Launch the Bookstore app (`http://localhost:3000`)  
2. Enter a valid book title, e.g., “Python Basics” in the search bar  
3. Click the search icon or press Enter  
**Expected Result:** Books matching “Python Basics” appear in the catalog  
**Post-conditions:** Search results displayed correctly  
**Evidence:** `screenshots/TC-001_search_results.png`  

---

✅ **Test Case**  
**ID:** TC-002  
**Title:** Add book to shopping cart successfully  
**Pre-conditions:** User is on a book detail page  
**Steps:**  
1. Click on a book from the homepage  
2. Click the “Add to Cart” button  
3. Navigate to the cart page  
**Expected Result:** The selected book appears in the cart with correct title, price, and quantity  
**Post-conditions:** Cart count updates and persists until cleared  
**Evidence:** `screenshots/TC-002_cart_add.png`  

---

✅ **Test Case**  
**ID:** TC-003  
**Title:** Attempt checkout without login (Negative Test)  
**Pre-conditions:** Cart contains at least one item; user not logged in  
**Steps:**  
1. Open the cart page  
2. Click the “Checkout” button  
**Expected Result:** User is redirected to the login page or shown a prompt  
**Post-conditions:** Checkout not processed without authentication  
**Evidence:** `screenshots/TC-003_checkout_redirect.png`  

---

✅ **Test Case**  
**ID:** TC-004  
**Title:** Complete checkout when logged in  
**Pre-conditions:** User logged in with valid credentials; cart has one or more items  
**Steps:**  
1. Navigate to cart page  
2. Click “Checkout”  
3. Fill out shipping details and confirm purchase  
**Expected Result:** Order confirmation message is displayed  
**Post-conditions:** Order saved in order history  
**Evidence:** `screenshots/TC-004_order_success.png`  
