from pyqldb.driver.qldb_driver import QldbDriver

Credit_Number=[]
Person_Name=[]
Current_Available_Amount=[]

qldb_driver = QldbDriver(ledger_name='Wallet-System')

def read_documents(transaction_executor):
    cursor = transaction_executor.execute_statement("SELECT * FROM Person")

    for doc in cursor:
        Person_Name.append(doc["PersonName"])
        Current_Available_Amount.append(doc["CurrentAvailableAmount"])
        Credit_Number.append(doc["CreditNumber"])

qldb_driver.execute_lambda(lambda executor: read_documents(executor))

print(Person_Name)
print(Current_Available_Amount)
print(Credit_Number)
