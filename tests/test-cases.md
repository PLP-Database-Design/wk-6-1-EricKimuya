# 📘 Test Cases — Bookstore Project

**Team:** Power Testers  
**Date:** November 2025  
**Environment:** Chrome v118, Windows 10, Localhost  
**Team:** Power Testers 

---

### 🧠 Legend
| ID Prefix | Area | Example |
|------------|-------|----------|
| TC-S | Search | TC-S01 |
| TC-C | Cart & Checkout | TC-C01 |
| TC-P | Payments | TC-P01 |
| TC-O | Orders & Returns | TC-O01 |
| TC-R | Reviews & Community | TC-R01 |
| TC-A | Admin | TC-A01 |
| TC-N | Notifications/Non-Functional | TC-N01 |

---

## 🔍 Search & Catalog (FR-O01, FR-X01)

| ID | Test Case | Steps | Expected Result |
|----|------------|--------|-----------------|
| TC-S01 | Search by book title | Enter “Python 101” in search bar → Click Search | Results show all books titled *Python 101* |
| TC-S02 | Search by author | Enter “John Doe” → Search | All books authored by John Doe appear |
| TC-S03 | Search with no results | Enter “XYZ999” | “No results found” message displays |
| TC-S04 | Filter by category | Choose “Programming” → Apply filter | Only programming books display |
| TC-S05 | Sort by price | Select “Sort by: Low to High” | Books appear sorted by ascending price |

---

## 🛒 Cart & Checkout (FR-O01, FR-O02)

| ID | Test Case | Steps | Expected Result |
|----|------------|--------|-----------------|
| TC-C01 | Add book to cart | Click “Add to Cart” on a book | Cart count increases by 1 |
| TC-C02 | Add multiple books | Add 3 different books | All 3 appear in cart |
| TC-C03 | Remove item from cart | Click remove on an item | Item disappears from cart |
| TC-C04 | Update quantity | Change book quantity from 1 to 3 | Total price updates accordingly |
| TC-C05 | Proceed to checkout | Click “Checkout” → Redirect | Checkout form appears |
| TC-C06 | Apply valid coupon | Enter “SAVE10” → Apply | 10% discount reflects on total |
| TC-C07 | Apply invalid coupon | Enter “INVALID” → Apply | “Coupon not valid” message appears |

---

## 💳 Payment (FR-O03)

| ID | Test Case | Steps | Expected Result |
|----|------------|--------|-----------------|
| TC-P01 | Payment with valid card | Enter valid Visa card → Submit | “Payment Successful” message appears |
| TC-P02 | Payment with invalid card | Enter wrong CVV → Submit | “Payment Failed” message displays |
| TC-P03 | Empty payment form | Leave fields blank → Submit | “All fields required” validation triggers |
| TC-P04 | M-Pesa payment method | Select M-Pesa → Enter number → Confirm | Payment processed successfully |

---

## 📦 Orders & Returns (FR-O04, FR-O05, FR-R01)

| ID | Test Case | Steps | Expected Result |
|----|------------|--------|-----------------|
| TC-O01 | View order history | Go to “My Orders” | List of previous orders shown |
| TC-O02 | Track order | Click “Track” → Enter Order ID | Correct tracking info appears |
| TC-O03 | Cancel pending order | Click “Cancel” before dispatch | Order moves to “Cancelled” status |
| TC-O04 | Return delivered order | Click “Return” → Select reason → Submit | Return request logged successfully |
| TC-O05 | View refund status | Go to “My Returns” | Refund status displayed correctly |

---

## ⭐ Reviews & Community (FR-U01, FR-U02, FR-U03)

| ID | Test Case | Steps | Expected Result |
|----|------------|--------|-----------------|
| TC-R01 | Add review | Enter rating + comment → Submit | Review appears under product |
| TC-R02 | Edit review | Click “Edit” → Change text → Save | Updated review displays |
| TC-R03 | Delete review | Click “Delete” | Review removed |
| TC-R04 | View average rating | View book page with reviews | Average rating auto-calculated |

---

## ⚙️ Admin Console (FR-M01, FR-M02, FR-M03)

| ID | Test Case | Steps | Expected Result |
|----|------------|--------|-----------------|
| TC-A01 | Add new book | Admin → Add new book form → Submit | Book appears in catalog |
| TC-A02 | Edit existing book | Edit price → Save | Catalog updates successfully |
| TC-A03 | Delete book | Click “Delete” | Book removed from system |

---

## 🔔 Notifications & Non-Functional (FR-N01, FR-N02, FR-X02)

| ID | Test Case | Steps | Expected Result |
|----|------------|--------|-----------------|
| TC-N01 | Email confirmation on order | Place order → Check email | Confirmation email received |
| TC-N02 | Load time performance | Open home page | Page loads in < 3 seconds |

---

✅ **Total Test Cases:** 30  
✅ **Coverage:** 100 percent of Functional + 3 Non-Functional Requirements
