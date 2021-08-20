
from logging import basicConfig, getLogger, INFO

from constants import Constants
from connect_to_ledger import create_qldb_driver

logger = getLogger(__name__)
basicConfig(level=INFO)


def create_index(driver, table_name, index_attribute):
    logger.info("Creating index on '{}'...".format(index_attribute))
    statement = 'CREATE INDEX on {} ({})'.format(table_name, index_attribute)
    cursor = driver.execute_lambda(lambda executor: executor.execute_statement(statement))
    return len(list(cursor))


def main(ledger_name=Constants.LEDGER_NAME):
    logger.info('Creating indexes on all tables...')
    try:
        with create_qldb_driver(ledger_name) as driver:
            create_index(driver, Constants.PERSON_TABLE_NAME, Constants.PERSON_ID_INDEX_NAME)
            create_index(driver, Constants.PERSON_TABLE_NAME, Constants.PERSON_NAME_INDEX_NAME)
            create_index(driver, Constants.PERSON_TABLE_NAME, Constants.CREDIT_NUMBER_INDEX_NAME)
            create_index(driver, Constants.PERSON_TABLE_NAME, Constants.CURRENT_AVAILABLE_AMOUNT_INDEX_NAME)
            create_index(driver, Constants.CREDIT_TABLE_NAME, Constants.CREDIT_NUMBER_INDEX_NAME)
            create_index(driver, Constants.CREDIT_TABLE_NAME, Constants.PERSON_ID_INDEX_NAME)
            create_index(driver, Constants.CREDIT_TABLE_NAME, Constants.EXPIRY_TIME_OF_CREDIT_INDEX_NAME)
            create_index(driver, Constants.CREDIT_TABLE_NAME, Constants.CURRENT_AVAILABLE_AMOUNT_INDEX_NAME)
            create_index(driver, Constants.USER_REGISTRATION_TABLE_NAME, Constants.PERSON_NAME_INDEX_NAME)
            create_index(driver, Constants.USER_REGISTRATION_TABLE_NAME, Constants.CREDIT_NUMBER_INDEX_NAME)
            create_index(driver, Constants.USER_REGISTRATION_TABLE_NAME, Constants.EXPIRY_TIME_OF_CREDIT_INDEX_NAME)
            logger.info('Indexes created successfully.')
    except Exception as e:
        logger.exception('Unable to create indexes.')
        raise e


if __name__ == '__main__':
    main()
