from logging import basicConfig, getLogger, INFO

from constants import Constants
from connect_to_ledger import create_qldb_driver

logger = getLogger(__name__)
basicConfig(level=INFO)


def create_table(driver, table_name):
    logger.info("Creating the '{}' table...".format(table_name))
    statement = 'CREATE TABLE {}'.format(table_name)
    cursor = driver.execute_lambda(lambda executor: executor.execute_statement(statement))
    logger.info('{} table created successfully.'.format(table_name))
    return len(list(cursor))

def main(ledger_name=Constants.LEDGER_NAME):
    try:
        with create_qldb_driver(ledger_name) as driver:
            create_table(driver, Constants.USER_REGISTRATION_TABLE_NAME)
            create_table(driver, Constants.CREDIT_TABLE_NAME)
            create_table(driver, Constants.PERSON_TABLE_NAME)
            logger.info('Tables created successfully.')
    except Exception as e:
        logger.exception('Errors creating tables.')
        raise e


if __name__ == '__main__':
    main()
