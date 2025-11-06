---
draft: true
---
; the structure and intent are exposed in [[Storage Information Programs with OOP]] together with other general guidelines.
# Introduction

In this document, I will define several key concepts and classes that are integral to my project. These include both financial and administrative elements. The primary concepts are:

- **Monthly Report**: A financial report summarising the list of banks and their assets.
	- Bank
		- Asset
			- value: float
			- geographic location: string
			- etf or stock: bool
			- asset class: string
			- purchase history
				- transaction
					- money
						- value: float
						- currency: string
					- date
						- day: int
						- month: int
						- year: int
			- price history
				- date
				- money
- **Subletter**: A concept for managing individuals who will sublet a room or property.
	- documents submitted: bool
	- Stay
		- Time stay
			- begin date
				- date
			- end date
				- date
			- amount of nights: int
		- price per night
			- money
		- deposti amount
			- money
		- deposit paid: bool
		- amount of people: int
		- date confirmed: bool
		- exclusivity: bool
		- Overlaps, how critical: int $\in [1, 5]$ 
		- Paid amount
			- money
			- deposit
				- money
- **Cash Flow**: The movement of money into and out of an entity or account.
	- Income
		- Transaction
		- Cause: string
	- Expenses
		- Transaction
		- Cause
- **Futura Student**
	- Subject: string
	- payment per hour
		- money
	- Total payment
		- money
	- Total hours: integer

Each of these concepts will be detailed below, including their attributes and relevant details.

---

# Introduction

In this document, I will define several key concepts and classes relevant to my project. These include:

1. **Monthly Report**: A class that represents a financial report containing a list of banks and their assets.
2. **Subletter**: A concept for managing individuals who will sublet a room or property.
3. **[Additional Concept 1]**: Description of the additional concept and its relevance.
4. **[Additional Concept 2]**: Description of another concept and its details.
5. **[Additional Concept 3]**: Description of the third concept and its attributes.

Each of these items will be detailed below, including their attributes and how they fit into the overall structure of the project.

---

# Monthly Report

The `MonthlyReport` class represents a report containing a list of banks.

### Attributes:
- **`banks`**: A finite list of `Bank` objects. The constructor takes a list of banks.

---

**Bank Class**

The `Bank` class represents a bank, which contains a collection of financial assets.

- **`assets`**: A list of financial assets held by the bank, including instances of the `Asset` class.

**Asset Class**

The `Asset` class represents a financial asset with detailed attributes such as its value, purchase and price history, and other relevant information.

- **`total_value`**: The current total value of the asset.
- **`purchase_history`**: A list of `Transaction` objects, representing past purchases of the asset.
- **`price_history`**: A list of tuples, where each tuple contains a date and a `Money` object.
- **`asset_class`**: The class of the asset (e.g., ETF, stock).
- **`geographic_location`**: The geographic location where the asset is based (e.g., Europe, USA).
- **`is_etf`**: A boolean indicating whether the asset is an ETF or a single stock.

**Transaction Class**

The `Transaction` class represents a transaction for an asset.

- **`date`**: The date when the transaction took place.
- **`provenience`**: The source from which the funds originated (can be an `Asset` or a `Bank`).
- **`destination_asset`**: The `Asset` or `Bank` to which the money is sent.
- **`money_moved`**: A list of tuples representing the amount of money moved and its currency.

**Money Class**

The `Money` class represents the amount of money in a specific currency.

- **`amount`**: A number with two decimal places.
- **`currency`**: A string representing the currency (e.g., EUR, USD).

---

## Subletter

The concept of a `Subletter` pertains to individuals who will sublet a room or property.

### Attributes:
- **`name`**: The name of the subletter.
- **`contact_info`**: Contact details of the subletter.
- **`rental_period`**: Duration for which the room or property is being sublet.

---

## Cash Flow

The `CashFlow` concept tracks the movement of money into and out of an entity or account.

### Attributes:
- **`inflows`**: A list of transactions representing money coming in.
- **`outflows`**: A list of transactions representing money going out.

---

## Expenses

The `Expenses` concept represents costs incurred.

### Attributes:
- **`amount`**: The total amount spent.
- **`category`**: The category of the expense (e.g., rent, utilities).
- **`date`**: The date when the expense occurred.

---

## Income

The `Income` concept represents earnings or revenue received.

### Attributes:
- **`amount`**: The total amount earned.
- **`source`**: The source of the income (e.g., salary, investment).
- **`date`**: The date when the income was received.