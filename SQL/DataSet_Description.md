
# 📊 Clickstream Dataset Overview

This dataset represents clickstream data collected from an e-commerce platform. It helps track how users interact with the website — from landing on the homepage to completing a purchase. This data is useful for understanding user behavior, measuring conversion rates, and optimizing the user journey.

Each row in the **clickstream** table represents **a single user event** — like viewing a product, using a coupon, or placing an order.

---

## 🧾 Clickstream Table: Columns Explained

| Column Name       | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `click_id`        | A unique ID for each user event. It acts like a row number.                |
| `user_id`         | An identifier for the user who performed the action.                       |
| `event_timestamp` | The exact date and time when the action happened.                          |
| `source_type`     | Where the user came from (like Google or Facebook).                        |
| `event_name`      | The type of event or action the user performed (see list below).           |
| `event_details`   | Extra information about the action (like which product was viewed).        |

### 🔹 Types of `event_name`

The `event_name` column shows what kind of action the user took. These are the possible values:

- `home`: The user landed on the homepage.
- `product`: The user viewed a product page.
- `checkout`: The user reached the checkout page.
- `coupon`: The user applied a coupon code.
- `order`: The user placed an order and completed the purchase.

> ⚠️ **Note:** For general actions like homepage visits, `event_details` may be empty. For example, if someone just visited the homepage, there's no extra detail to capture.

---

## 📦 Order Details Table: Columns Explained

The newly added **order_details** table gives more information about each purchase recorded in the clickstream data.

In the clickstream table, when an `order` event is recorded, the `event_details` field stores the `order_id`. Using this `order_id`, we can link it to the `order_details` table to get details like how much was spent, where the order will be delivered, and when it’s expected to arrive.

| Column Name      | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| `order_id`       | Unique ID for the order. Matches the ID in `event_details` of `order` events.|
| `state`          | The U.S. state where the order is going to be delivered.                    |
| `amount`         | Total order amount in USD.                                                  |
| `pincode`        | The zip code of the delivery location.                                      |
| `delivery_date`  | The expected date when the product will be delivered.                       |

> ✅ This table lets us connect behavioral actions (like clicking and buying) to financial and delivery information.

---

## 👣 Example: A Complete User Journey with Enriched Order Details

Let’s walk through an example of **User `U001`'s** journey on **June 1, 2025** to see how both tables work together:

### 🧭 Clickstream Events

| click_id | event_timestamp       | source_type | event_name | event_details   |
|----------|------------------------|-------------|------------|-----------------|
| 1        | 2025-06-01 09:58:00    | google      | home       | (empty)         |
| 2        | 2025-06-01 10:00:05    | google      | product    | Laptop          |
| 3        | 2025-06-01 10:01:10    | google      | product    | Wireless Mouse  |
| 4        | 2025-06-01 10:03:30    | google      | checkout   | (empty)         |
| 5        | 2025-06-01 10:04:10    | google      | coupon     | SUMMER10        |
| 6        | 2025-06-01 10:05:00    | google      | order      | ORD001          |

### 📦 Matching Order Details (from `order_details` table)

| order_id | state      | amount | pincode | delivery_date |
|----------|------------|--------|---------|----------------|
| ORD001   | California | 999.99 | 90210   | 2025-06-05     |

### ✅ What This Tells Us

- The user **landed on the homepage** via **Google**.
- Then they **viewed two products**: a **Laptop** and a **Wireless Mouse**.
- They proceeded to the **checkout page**.
- Used a **coupon code** `SUMMER10`.
- **Completed the purchase** with order ID **ORD001**.

From the second table, we also know that:
- The order was worth **$999.99**.
- It was to be delivered to **California (ZIP 90210)**.
- Expected delivery date was **June 5, 2025**.

So, we can now track the **full conversion funnel** — from visit to purchase — and enrich it with **transactional data**.

---

Let me know if you want this enriched with visual flowcharts, KPIs, or query examples.
