
---

# Revised Test Cases — Bookstore Project 

**Team:** Power Testers
**Date:** November 2025
**Environment:** Chrome v118, Windows 10, Localhost
**Project Status:** Complete

---

## 🎯 Testing Scope and Focus

**Current Focus:** Frontend functionality, UI components, basic user interactions
**Limited To:** Features actually implemented in current codebase
**Excluded:** Backend integrations, payment processing, admin features

---

## 🧠 Revised Legend

| ID Prefix | Area               | Status      |
| --------- | ------------------ | ----------- |
| TC S      | Search and Catalog | Implemented |
| TC C      | Cart Management    | Implemented |
| TC UI     | User Interface     | Implemented |
| TC DB     | Data Display       | Implemented |

---

## 🔍 SEARCH and CATALOG (Fully Implemented)

| ID     | Test Case               | Steps                                             | Expected Result                     | Priority |
| ------ | ----------------------- | ------------------------------------------------- | ----------------------------------- | -------- |
| TC S01 | Search by book title    | 1. Enter "Python" in search bar<br>2. Press Enter | Books with "Python" in title appear | High     |
| TC S02 | Search by author        | 1. Enter author name in search<br>2. Press Enter  | Books by that author display        | High     |
| TC S03 | Search with no results  | 1. Enter "XYZ999"<br>2. Search                    | "No results" message shows          | Medium   |
| TC S04 | Case insensitive search | 1. Enter "python" (lowercase)<br>2. Search        | Books with "Python" still appear    | Medium   |
| TC S05 | Partial match search    | 1. Enter "Pyth"<br>2. Search                      | Books with "Python" appear          | Medium   |

---

## 🛒 CART MANAGEMENT (Fully Implemented)

| ID     | Test Case              | Steps                                                    | Expected Result               | Priority |
| ------ | ---------------------- | -------------------------------------------------------- | ----------------------------- | -------- |
| TC C01 | Add book to cart       | 1. Click "Add to Cart" on book<br>2. Observe cart icon   | Cart counter increases by 1   | High     |
| TC C02 | Add multiple books     | 1. Add 3 different books to cart                         | All 3 appear in cart page     | High     |
| TC C03 | Remove item from cart  | 1. Go to cart<br>2. Click remove on item                 | Item disappears from cart     | High     |
| TC C04 | Update quantity        | 1. In cart, change quantity from 1 to 3                  | Total price updates correctly | High     |
| TC C05 | Cart persistence       | 1. Add items to cart<br>2. Refresh page<br>3. Check cart | Items remain in cart          | Medium   |
| TC C06 | Empty cart state       | 1. Remove all items from cart                            | "Cart is empty" message shows | Medium   |
| TC C07 | Cart total calculation | 1. Add multiple items with different quantities          | Total calculates correctly    | High     |

---

## 📖 BOOK DISPLAY and UI (Fully Implemented)

| ID      | Test Case          | Steps                                                    | Expected Result                            | Priority |
| ------- | ------------------ | -------------------------------------------------------- | ------------------------------------------ | -------- |
| TC UI01 | Book list display  | 1. Navigate to home page                                 | All books display with cover, title, price | High     |
| TC UI02 | Book details page  | 1. Click on any book                                     | Detailed book page opens                   | High     |
| TC UI03 | Responsive design  | 1. Resize browser window<br>2. Check mobile view         | Layout adapts correctly                    | Medium   |
| TC UI04 | Navigation working | 1. Click navigation links<br>2. Use browser back forward | Pages load correctly                       | High     |
| TC UI05 | Image loading      | 1. Browse book catalog                                   | All book cover images load                 | Medium   |

---

## ⚡ BASIC CHECKOUT FLOW (UI Only — Mock)

| ID      | Test Case                | Steps                                       | Expected Result          | Priority | Notes         |
| ------- | ------------------------ | ------------------------------------------- | ------------------------ | -------- | ------------- |
| TC CH01 | Checkout button access   | 1. Add items to cart<br>2. Click "Checkout" | Checkout form displays   | Medium   | Mock UI only  |
| TC CH02 | Checkout form validation | 1. Leave required fields empty<br>2. Submit | Validation messages show | Low      | Frontend only |
| TC CH03 | Checkout disabled empty  | 1. Empty cart<br>2. Go to checkout page     | Checkout button disabled | Medium   |               |

---

## 🎭 USER INTERACTION and STATE

| ID      | Test Case        | Steps                                                                  | Expected Result         | Priority |
| ------- | ---------------- | ---------------------------------------------------------------------- | ----------------------- | -------- |
| TC ST01 | State management | 1. Add items to cart<br>2. Navigate between pages<br>3. Return to cart | Cart state preserved    | High     |
| TC ST02 | Error handling   | 1. Trigger various UI errors                                           | Graceful error messages | Medium   |
| TC ST03 | Loading states   | 1. Perform search<br>2. Navigate pages                                 | Loading indicators show | Low      |

---

## 📱 BROWSER COMPATIBILITY

| ID      | Test Case             | Steps                            | Expected Result           | Priority |
| ------- | --------------------- | -------------------------------- | ------------------------- | -------- |
| TC BC01 | Chrome compatibility  | 1. Test all features in Chrome   | All functionality works   | High     |
| TC BC02 | Firefox compatibility | 1. Test core features in Firefox | Basic functionality works | Medium   |
| TC BC03 | Mobile browser test   | 1. Test on mobile Chrome Safari  | Responsive design works   | Medium   |

---

## 🚫 EXCLUDED FROM CURRENT TESTING

**Payment Processing:**
TC P01, TC P02, TC P03, TC P04 (Not implemented)

**Order Management:**
TC O01, TC O02, TC O03, TC O04, TC O05 (Not implemented)

**Reviews and Community:**
TC R01, TC R02, TC R03, TC R04 (Not implemented)

**Admin Features:**
TC A01, TC A02, TC A03 (Not implemented)

**Notifications:**
TC N01, TC N02 (Not implemented)

**Coupons Discounts:**
TC C06, TC C07 (Not implemented)

---

## 📊 TEST EXECUTION SUMMARY

**Test Coverage:**
Total Test Cases: 22 (Revised from original 30)

**High Priority:** 12 tests
**Medium Priority:** 7 tests
**Low Priority:** 3 tests

### Testing Priorities

**Week 1:** Execute all High priority tests (TC S01, TC C01–07, TC UI01–02)
**Week 2:** Execute Medium priority tests and browser compatibility
**Week 3:** Execute Low priority tests and exploratory testing

### Success Criteria

✔ 95 percent pass rate on High priority tests

---


