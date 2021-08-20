class Constants:

    LEDGER_NAME = "Wallet-System"

    USER_REGISTRATION_TABLE_NAME = "UserRegistration"
    CREDIT_TABLE_NAME = "Credit"
    PERSON_TABLE_NAME = "Person"

    CURRENT_AVAILABLE_AMOUNT_INDEX_NAME = "CurrentAvailableAmount"
    EXPIRY_TIME_OF_CREDIT_INDEX_NAME = "ExpiryTimeOfCredit"
    CREDIT_NUMBER_INDEX_NAME = "CreditNumber"
    PERSON_NAME_INDEX_NAME = "PersonName"
    PERSON_ID_INDEX_NAME = "PersonId"

    JOURNAL_EXPORT_S3_BUCKET_NAME_PREFIX = "qldb-tutorial-journal-export"
    USER_TABLES = "information_schema.user_tables"
    S3_BUCKET_ARN_TEMPLATE = "arn:aws:s3:::"
    LEDGER_NAME_WITH_TAGS = "tags"

    RETRY_LIMIT = 4
