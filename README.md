# DIGITAL MART

A Digital Mart built using Python. This project builds a small terminal based UI to let user buy several items from a pre-defined menu .

## Features

- Menu to show availability of different grocery products
- Add or remove products after selecting once
- Makes a bill of all the items purchased
- Avail various discounts based on total billing price
  

## Technologies Used

- Python 3

## How to access the code

1. Clone the repository:

```bash
git clone https://github.com/aman26bce11098/26BCE11098-Digital_Mart.git
```

2. Navigate to the project folder:

```bash
cd 26BCE11098-Digital_Mart
```

3. Run the main program:

```bash
python Digital_Mart.py
```

> **Note:** Keep `Digital_Mart.py` and `MART_MODULE.py` in the same folder, as the main program imports functions from `MART_MODULE.py`.

## Project Structure

```
Digital_Mart/
│
├── Digital_Mart.py     # Main program
├── MART_MODULE.py      # Contains the user-defined functions
├── statement.md
└── README.md
```

## Future Improvements

- Save Mart data to SQL
- Add online payment and ordering system 
- Include better discounts and more limited offers
- Develop a better user interface
- Different list of options for store manager , employees and customers

## Learning Outcomes

Through this project, I practiced:

- Working with Python modules
- Creating reusable functions
- Using lists to manage data
- Implementing conditional statements and loops

## How to run 
- When running the code , the user will get multiple options , such as displaying the available items in the Digital Mart , How many items they want to purchase , etc.
- Its recommended that the user goes through the option one by one .
- Firstly , the user will asked number items he wants to purchase.
- Next , the user will be asked to enter the serial number of the respective items he want to purchase .
>**Note:** The user will be asked to enter y(for yes) before finalising the order also ,if he wants to add or remove items. 
- Accordingly , user can use add and remove feature by entering y(for continue) and n(to exit) and by writing the s.no it will add or remove items respectively .
>**Note:** If user wants to remove any item(s) from cart he must enter the same item(s) which is already present in the cart.
- This whole process is in a looping statement (while) and hence it will ask user to continue( on entering 1 ) and exit( on entering 0 ).
- After the purchase, it has discount feature which will give discount on total expenditure.
- Finally , it will generate a detailed bill of purchase .

## Author

**Aman singh kushwaha**
