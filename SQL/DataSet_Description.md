# Clickstream Dataset Overview

This dataset represents **clickstream data** captured from users interacting with an e-commerce platform.  
Each row corresponds to a **single user action (event)** on the website, such as viewing a product, applying a coupon, or placing an order.

---

## 🧾 Columns Explained

| Column Name       | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `click_id`        | Unique identifier for each user action or event.                            |
| `user_id`         | ID representing the user who performed the action.                          |
| `event_timestamp` | Date and time when the event occurred.                                      |
| `source_type`     | The traffic source through which the user arrived (e.g., Google, Facebook). |
| `event_name`      | Type of user action (explained below).                                      |
| `event_details`   | Additional info about the event (e.g., product name, coupon code).          |

### 🔹 `event_name` Types

- **`home`** – Landed on the homepage  
- **`product`** – Viewed a product  
- **`checkout`** – Reached the checkout page  
- **`coupon`** – Applied a coupon code  
- **`order`** – Completed a purchase  

> **Note:** `event_details` may be empty for generic actions like homepage visits.

---

## 👣 Example of a User Journey

Let’s walk through **User `U001`’s journey** on **June 1, 2025**:

| click_id | event_timestamp       | source_type | event_name | event_details    |
|----------|------------------------|-------------|------------|------------------|
| 1        | 2025-06-01 09:58:00    | google      | home       | *(empty)*        |
| 2        | 2025-06-01 10:00:05    | google      | product    | Laptop           |
| 3        | 2025-06-01 10:01:10    | google      | product    | Wireless Mouse   |
| 4        | 2025-06-01 10:03:30    | google      | checkout   | *(empty)*        |
| 5        | 2025-06-01 10:04:10    | google      | coupon     | SUMMER10         |
| 6        | 2025-06-01 10:05:00    | google      | order      | ORD001           |

### 📌 Interpretation

The user:

1. Landed on the homepage via Google.
2. Viewed two products — *Laptop* and *Wireless Mouse*.
3. Went to the checkout page.
4. Applied a coupon code `SUMMER10`.
5. Completed the purchase with order ID `ORD001`.

✅ This represents a **complete conversion flow** from landing to order.

---
