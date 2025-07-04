
# 📊 Clickstream Dataset Overview

This dataset represents clickstream data captured from users interacting with an e-commerce platform.

Each row in the main **clickstream table** corresponds to a single user action (event) on the website, such as viewing a product, applying a coupon, or placing an order.

## 🧾 Clickstream Table: Columns Explained

| Column Name       | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `click_id`        | Unique identifier for each user action or event.                           |
| `user_id`         | ID representing the user who performed the action.                         |
| `event_timestamp` | Date and time when the event occurred.                                     |
| `source_type`     | The traffic source through which the user arrived (e.g., Google, Facebook).|
| `event_name`      | Type of user action (explained below).                                     |
| `event_details`   | Additional info about the event (e.g., product name, coupon code).         |

## 🔹 `event_name` Types

- `home` – Landed on the homepage  
- `product` – Viewed a product  
- `checkout` – Reached the checkout page  
- `coupon` – Applied a coupon code  
- `order` – Completed a purchase  

> 📌 **Note:** `event_details` may be empty for general actions like homepage visits.

---

## 🧾 Order Details Table: Columns Explained

This new **order_details** table provides **extra information about completed orders** found in the clickstream `order` events.

| Column Name      | Description                                                      |
|------------------|------------------------------------------------------------------|
| `order_id`       | Unique ID of the order (matches `event_details` in `order` events). |
| `state`          | The U.S. state where the order will be delivered.               |
| `amount`         | Total order value in USD.                                       |
| `pincode`        | Zip code (postal code) of the delivery address.                 |
| `delivery_date`  | Scheduled delivery date of the order.                           |

This allows combining behavioral data (clicks) with transactional data (order value and delivery).

---

## 👣 Example of a User Journey (with Enriched Order Details)

Let’s walk through **User `U001`'s** journey on **June 1, 2025**:

### Clickstream Events

| click_id | event_timestamp       | source_type | event_name | event_details   |
|----------|------------------------|-------------|------------|-----------------|
| 1        | 2025-06-01 09:58:00    | google      | home       | (empty)         |
| 2        | 2025-06-01 10:00:05    | google      | product    | Laptop          |
| 3        | 2025-06-01 10:01:10    | google      | product    | Wireless Mouse  |
| 4        | 2025-06-01 10:03:30    | google      | checkout   | (empty)         |
| 5        | 2025-06-01 10:04:10    | google      | coupon     | SUMMER10        |
| 6        | 2025-06-01 10:05:00    | google      | order      | ORD001          |

### Order Details

| order_id | state      | amount | pincode | delivery_date |
|----------|------------|--------|---------|----------------|
| ORD001   | California | 999.99 | 90210   | 2025-06-05     |

✅ So, this user completed a purchase worth **$999.99**, to be delivered to **California (ZIP: 90210)** on **June 5, 2025**.
