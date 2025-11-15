# Power Testers — Defect Log

**Project:** Bookstore Project
**Date:** November 11, 2025
**Team:** Power Testers

---

## ✅ VERIFIED WORKING FEATURES

---

## 🐞 Bug Report

**ID:** BUG-001
**Summary:** Search returns no results when valid title is entered
**Severity/Priority:** Major / High
**Environment:** Chrome v118, Windows 10, Localhost:3000
**Affected FR(s):** FR-O02

**Steps to Reproduce:**

1. Launch the app
2. Enter "Python Basics" in the search bar
3. Press Enter

**Expected Result:** Matching results should appear
**Actual Result:** Matching results appear as expected
**Status:** Closed / Invalid
**Attachments:** `screenshots/BUG-001_search_fail.png`
**Notes:** Verified search functionality. Original bug report may have been caused by case sensitivity or missing sample data during testing.

---

## 🐞 Bug Report

**ID:** BUG-002
**Summary:** Cart icon counter does not update after adding a book
**Severity/Priority:** Minor / Medium
**Environment:** Chrome v118, Ubuntu 22.04, Localhost:3000
**Affected FR(s):** FR-O03

**Steps to Reproduce:**

1. Open any book detail page
2. Click "Add to Cart"
3. Observe the cart icon in header

**Expected Result:** Counter should increment by 1
**Actual Result:** Counter increments correctly without page refresh
**Status:** Closed / Invalid
**Attachments:** `screenshots/BUG-002_cart_counter.png`
**Notes:** Tested multiple scenarios; cart counter updates correctly. Original report may have missed asynchronous state update behavior.

---

## 🐞 Bug Report

**ID:** BUG-003
**Summary:** Checkout button active even when cart is empty
**Severity/Priority:** Minor / Low
**Environment:** Chrome v118, Windows 10, Localhost:3000
**Affected FR(s):** FR-O04

**Steps to Reproduce:**

1. Navigate to cart page
2. Remove all items
3. Observe "Checkout" button

**Expected Result:** Checkout button should be disabled when cart is empty
**Actual Result:** Button is disabled when cart is empty
**Status:** Closed / Invalid
**Attachments:** `screenshots/BUG-003_checkout_empty.png`
**Notes:** Verified checkout validation works. Original report may have used cached state or incorrect test sequence.

---

## 🚨 ACTUAL DEFECTS FOUND

---

## 🐞 Bug Report

**ID:** BUG-004
**Summary:** Missing payment integration - checkout form exists but no payment processing
**Severity/Priority:** Critical / High
**Environment:** Chrome v118, Windows 10, Localhost:3000
**Affected FR(s):** FR-O03

**Steps to Reproduce:**

1. Add items to cart
2. Proceed to checkout
3. Fill in payment details
4. Submit payment

**Expected Result:** Payment processed successfully or proper error handling
**Actual Result:** Form submits but no payment gateway integration exists
**Status:** Open
**Attachments:** `screenshots/BUG-004_payment_missing.png`
**Notes:** Checkout appears to be mock functionality only. No actual payment processing.

---

## 🐞 Bug Report

**ID:** BUG-005
**Summary:** Order history and tracking functionality not implemented
**Severity/Priority:** Major / High
**Environment:** Chrome v118, Windows 10, Localhost:3000
**Affected FR(s):** FR-O04, FR-O05

**Steps to Reproduce:**

1. Look for "My Orders" or order history page
2. Attempt to track an order
3. Look for return functionality

**Expected Result:** Order management features available
**Actual Result:** No order history, tracking, or return features found
**Status:** Open
**Attachments:** `screenshots/BUG-005_orders_missing.png`
**Notes:** Core order management functionality missing from current implementation.

---

## 🐞 Bug Report

**ID:** BUG-006
**Summary:** Review system not implemented
**Severity/Priority:** Major / Medium
**Environment:** Chrome v118, Windows 10, Localhost:3000
**Affected FR(s):** FR-U01, FR-U02, FR-U03

**Steps to Reproduce:**

1. Navigate to any book detail page
2. Look for review section
3. Attempt to add/edit/delete reviews

**Expected Result:** Review functionality available
**Actual Result:** No review system implemented
**Status:** Open
**Attachments:** `screenshots/BUG-006_reviews_missing.png`
**Notes:** Community features (reviews, ratings) completely missing.

---

## 🐞 Bug Report

**ID:** BUG-007
**Summary:** Admin console for book management missing
**Severity/Priority:** Major / High
**Environment:** Chrome v118, Windows 10, Localhost:3000
**Affected FR(s):** FR-M01, FR-M02, FR-M03

**Steps to Reproduce:**

1. Look for admin dashboard or book management interface
2. Attempt to add new book
3. Attempt to edit/delete existing books

**Expected Result:** Admin management interface available
**Actual Result:** No admin functionality found
**Status:** Open
**Attachments:** `screenshots/BUG-007_admin_missing.png`
**Notes:** Book catalog management requires manual database updates.

---

## 🐞 Bug Report

**ID:** BUG-008
**Summary:** Coupon/discount system not implemented
**Severity/Priority:** Minor / Medium
**Environment:** Chrome v118, Windows 10, Localhost:3000
**Affected FR(s):** FR-O02

**Steps to Reproduce:**

1. Go to cart page
2. Look for coupon input field
3. Attempt to apply discount code

**Expected Result:** Coupon application functionality
**Actual Result:** No coupon/discount system found
**Status:** Open
**Attachments:** `screenshots/BUG-008_coupons_missing.png`
**Notes:** Promotional features missing from cart.

---

## 🐞 Bug Report

**ID:** BUG-009
**Summary:** Email notifications not implemented
**Severity/Priority:** Minor / Low
**Environment:** Chrome v118, Windows 10, Localhost:3000
**Affected FR(s):** FR-N01

**Steps to Reproduce:**

1. Complete an order
2. Check for email confirmation

**Expected Result:** Order confirmation email sent
**Actual Result:** No email functionality implemented
**Status:** Open
**Attachments:** `screenshots/BUG-009_notifications_missing.png`
**Notes:** Notification system missing.

---

# 📊 DEFECT SUMMARY

**Total Defects Reported:** 9
**Closed/Invalid:** 3 (33%)
**Open Defects:** 6 (67%)

**Defect Severity Breakdown:**
• Critical: 1
• Major: 4
• Minor: 1

**Recommendations:**
• Focus development on payment integration (BUG-004)
• Implement basic order management system (BUG-005)
• Add admin functionality for book management (BUG-007)
• Consider review system for user engagement (BUG-006)
