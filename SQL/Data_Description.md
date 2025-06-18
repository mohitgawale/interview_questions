This dataset represents clickstream data captured from users interacting with an e-commerce platform. Each row corresponds to a single event (or user action) on the website, such as viewing a product, applying a coupon, or placing an order.

Columns Explained:
click_id: Unique identifier for each user action or event.
user_id: ID representing the user who performed the action.
event_timestamp: Date and time when the event occurred.
source_type: The traffic source through which the user arrived on the platform (e.g., Google, Facebook).
event_name: Type of user action, such as:
        
          home – Landed on homepage
          product – Viewed a product
          checkout – Reached the checkout page
          coupon – Applied a coupon code
          order – Completed a purchase

event_details: Additional information about the event (e.g., product name, coupon code, order ID).
                This field can be empty for generic events like homepage visits.

Example of a User Journey:
Let’s walk through User U001’s journey on June 1, 2025:

| click\_id | event\_timestamp    | source\_type | event\_name | event\_details |
| --------- | ------------------- | ------------ | ----------- | -------------- |
| 1         | 2025-06-01 09:58:00 | google       | home        | *(empty)*      |
| 2         | 2025-06-01 10:00:05 | google       | product     | Laptop         |
| 3         | 2025-06-01 10:01:10 | google       | product     | Wireless Mouse |
| 4         | 2025-06-01 10:03:30 | google       | checkout    | *(empty)*      |
| 5         | 2025-06-01 10:04:10 | google       | coupon      | SUMMER10       |
| 6         | 2025-06-01 10:05:00 | google       | order       | ORD001         |

Interpretation:

The user landed on the homepage via Google, browsed two products, proceeded to checkout, applied a coupon (SUMMER10), 
and placed an order (ORD001) — a complete conversion flow.
