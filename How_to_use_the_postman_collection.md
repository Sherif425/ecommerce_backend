**Postman collection** that includes **all the backend endpoints** (auth, categories, products, cart, orders, payments), and for each request I’ll specify:

* **HTTP method**
* **URL**
* **Required headers** (Authorization if needed)
* **Request body** example (for POST/PUT)
* **Expected response** (short description)

---

## 🗂 Postman Collection Structure

Your collection will look like this:

```
Ecommerce API (Postman Collection)
├── Auth
│   ├── Register User (POST /api/auth/register/)
│   └── Login User (POST /api/auth/login/)
├── Categories
│   └── List Categories (GET /api/categories/)
├── Products
│   └── List Products (GET /api/products/)
├── Cart
│   ├── Get Cart (GET /api/cart/)
│   ├── Add to Cart (POST /api/cart/add/)
│   └── Remove from Cart (POST /api/cart/remove/)
├── Orders
│   ├── Create Order (POST /api/orders/)
│   └── List Orders (GET /api/orders/)
└── Payments
    └── Process Payment (POST /api/payments/)
```

---

## 📝 Detailed Request Guide

### 🔐 Auth

#### 1. Register User

* **Method**: `POST`
* **URL**: `http://localhost:8000/api/auth/register/`
* **Body (JSON)**:

```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

* **Response**: User object with ID and username.

#### 2. Login User

* **Method**: `POST`
* **URL**: `http://localhost:8000/api/auth/login/`
* **Body (JSON)**:

```json
{
  "username": "john_doe",
  "password": "securepassword123"
}
```

* **Response**:

```json
{
  "access": "JWT_ACCESS_TOKEN",
  "refresh": "JWT_REFRESH_TOKEN"
}
```

* **👉 Note**: Save `access` token and add it to `Authorization` header for all **protected routes**:

```
Authorization: Bearer JWT_ACCESS_TOKEN
```

---

### 📂 Categories

#### 3. List Categories

* **Method**: `GET`
* **URL**: `http://localhost:8000/api/categories/`
* **Headers**: (none required, but token can be used if auth-protected)
* **Response**: List of categories.

---

### 📦 Products

#### 4. List Products

* **Method**: `GET`
* **URL**: `http://localhost:8000/api/products/`
* **Response**:

```json
[
  {
    "id": 1,
    "name": "Laptop",
    "price": "1200.00",
    "category": 1
  }
]
```

---

### 🛒 Cart

#### 5. Get Cart

* **Method**: `GET`
* **URL**: `http://localhost:8000/api/cart/`
* **Headers**:

```
Authorization: Bearer JWT_ACCESS_TOKEN
```

* **Response**: List of cart items.

#### 6. Add to Cart

* **Method**: `POST`
* **URL**: `http://localhost:8000/api/cart/add/`
* **Headers**: Authorization
* **Body (JSON)**:

```json
{
  "product_id": 1,
  "quantity": 2
}
```

* **Response**: Updated cart item.

#### 7. Remove from Cart

* **Method**: `POST`
* **URL**: `http://localhost:8000/api/cart/remove/`
* **Headers**: Authorization
* **Body (JSON)**:

```json
{
  "product_id": 1
}
```

* **Response**: Confirmation of removal.

---

### 📑 Orders

#### 8. Create Order

* **Method**: `POST`
* **URL**: `http://localhost:8000/api/orders/`
* **Headers**: Authorization
* **Body (JSON)**:

```json
{
  "address": "123 Main Street, Cairo",
  "payment_method": "credit_card"
}
```

* **Response**: New order object.

#### 9. List Orders

* **Method**: `GET`
* **URL**: `http://localhost:8000/api/orders/`
* **Headers**: Authorization
* **Response**: List of user’s orders.

---

### 💳 Payments

#### 10. Process Payment

* **Method**: `POST`
* **URL**: `http://localhost:8000/api/payments/`
* **Headers**: Authorization
* **Body (JSON)**:

```json
{
  "amount": 500.00,
  "order_id": 1
}
```

* **Response**:

```json
{
  "status": "success",
  "transaction_id": "txn_12345"
}
```

---

## 🚀 How to Use the Postman Collection

1. Open **Postman**.
2. Go to **Collections > Import**.
3. Upload the JSON file I’ll prepare for you (`ecommerce.postman_collection.json`).
4. Run requests in order:

   * Register
   * Login (save token)
   * Use token for protected routes (Cart, Orders, Payments).
5. You can create an **Environment** in Postman with a variable like:

   * `{{base_url}} = http://localhost:8000/api`
   * `{{auth_token}} = JWT_ACCESS_TOKEN`
     Then replace URLs and headers with variables for easier switching between local and production.

---

