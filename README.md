# FYP_foodOrder
Food Ordering System<br>
[Live Demo](https://fyp-food-order.vercel.app/)<br>
Overall grade: A-

## Purpose
The purpose of this project is to build a user-friendly and intuitive website for a restaurant point-of-sale (POS) system that seamlessly integrates the chat GPT functionalities. The objective is to create a central platform where customers can place orders, view menus, provide feedback, and interact with the chat GPT plugin, enhancing the overall user experience and facilitating efficient communication between customers and the POS system.

## Tech Stack
Frontend: Vue.js + Bootstrap + Vuetify + ChatGPT API
Backend: Django + Django REST framework + sqlite



## Functions
The project includes the following key functions:

1. Menu Management: The system incorporates a robust menu management module that allows staff to add, edit, and remove menu items, with features for categorization, pricing, availability settings, and menu item descriptions.
2. Order Processing: The system design includes an order management module that enables staff members to efficiently process customer orders, handling order tracking, status updates, and notifications to ensure smooth order fulfillment.
3. Checkout Process: The architecture incorporates a secure and streamlined checkout process, ensuring a seamless transaction flow for staff members, including integration with payment gateways, calculation of order totals, and generation of receipts.
4. Chat GPT Plugin Integration: The system design includes the integration of the chat GPT plugin for enhanced customer interaction. Staff members can set up and configure the chatbot's behavior, train it on restaurant-specific data, and customize its responses to align with the restaurant's brand and requirements.
5. Data Analysis: The system architecture includes components for data analysis, allowing staff members to gain insights into sales trends, popular dishes, and customer preferences, aiding in making informed decisions for menu optimization and business strategies.
6. QR Code Integration: The system architecture incorporates a QR code functionality that customers can scan to access the restaurant POS system website, simplifying the user experience and directing customers to the appropriate web page.
7. Menu Exploration: The website design ensures intuitive and visually appealing menu presentation, enabling customers to easily browse through available items, including detailed descriptions, prices, and promotions, along with any relevant dietary or allergen information.
8. Order Placement: The system design allows customers to conveniently select items, customize their orders, and add them to their cart, with real-time updates to the cart as customers modify their orders, providing a seamless and responsive ordering experience. 
9. Real-Time Order Updates: The system architecture facilitates real-time updates on the staff side, ensuring that staff members are promptly notified of any changes, enabling efficient order fulfillment.
10. Feedback Handling: The system includes a feature that allows the admin to gather and analyze customer feedback, enabling them to view and respond to customer comments and reviews.


# Client Side

## Quick Start

### Installation
```sh
cd Client
```

```sh
npm i
cp .env.example .env.local
```

> modify .env with your information.
- VITE_OPENAI_API_KEY
- VITE_API_URL


### Run the Development Server
```sh
npm run dev
```

# Server Side

## Quick Start

### Installation
```sh
cd Server
```

```sh
pipenv shell
pip install -r requirement.txt
python manage.py runserver
```
