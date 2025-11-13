# Power Testers — Phase 2 Defect Log
**Project:** Bookstore Project  
**Date:** November 11, 2025  
**Team:** Power Testers  

---

🐞 **Bug Report**  
**ID:** BUG-001  
**Summary:** Search returns no results when valid title is entered  
**Severity/Priority:** Major / High  
**Environment:** Chrome v118, Windows 10, Localhost:3000  
**Affected FR(s):** FR-O02  
**Steps to Reproduce:**  
1. Launch the app  
2. Enter “Python Basics” in the search bar  
3. Press Enter  
**Expected Result:** Matching results should appear  
**Actual Result:** Matching results appear as expected  
**Status:** Closed / Invalid  
**Attachments:** `screenshots/BUG-001_search_fail.png`  
**Notes:** Verified search functionality. Original bug report may have been caused by case sensitivity or missing sample data during testing.

---

🐞 **Bug Report**  
**ID:** BUG-002  
**Summary:** Cart icon counter does not update after adding a book  
**Severity/Priority:** Minor / Medium  
**Environment:** Chrome v118, Ubuntu 22.04, Localhost:3000  
**Affected FR(s):** FR-O03  
**Steps to Reproduce:**  
1. Open any book detail page  
2. Click “Add to Cart”  
3. Observe the cart icon in header  
**Expected Result:** Counter should increment by 1  
**Actual Result:** Counter increments correctly without page refresh  
**Status:** Closed / Invalid  
**Attachments:** `screenshots/BUG-002_cart_counter.png`  
**Notes:** Tested multiple scenarios; cart counter updates correctly. Original report may have missed asynchronous state update behavior.

---

🐞 **Bug Report**  
**ID:** BUG-003  
**Summary:** Checkout button active even when cart is empty  
**Severity/Priority:** Minor / Low  
**Environment:** Chrome v118, Windows 10, Localhost:3000  
**Affected FR(s):** FR-O04  
**Steps to Reproduce:**  
1. Navigate to cart page  
2. Remove all items  
3. Observe “Checkout” button  
**Expected Result:** Checkout button should be disabled when cart is empty  
**Actual Result:** Button is disabled when cart is empty  
**Status:** Closed / Invalid  
**Attachments:** `screenshots/BUG-003_checkout_empty.png`  
**Notes:** Verified checkout validation works. Original report may have used cached state or incorrect test sequence.
