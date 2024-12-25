from sqlalchemy import create_engine, text

from logging_config import logger


def get_products_with_increasing_prices() -> None:
    """Execute the main query to find products with strictly increasing prices."""
    database_url: str = "postgresql+psycopg2://dev_user:dev_password@localhost:5432/test_db"

    # Create a database engine
    engine = create_engine(database_url)

    # Define the query
    query = text(
        """
        WITH numbered_prices
             AS (SELECT product,
                        price,
                        Row_number()
                        over (
                            PARTITION BY product
                            ORDER BY DATE) AS row_num
                 FROM   price_updates),
             price_comparison
             AS (SELECT p1.product,
                        p1.price AS cur_price,
                        p2.price AS prev_price
                 FROM   numbered_prices p1
                        left join numbered_prices p2
                            ON p1.product = p2.product
                                AND p1.row_num = p2.row_num + 1),
             valid_products
             AS (SELECT product,
                        Count(*) AS total_records,
                        SUM(CASE
                            WHEN prev_price IS NULL THEN 1
                            WHEN cur_price > prev_price THEN 1
                            ELSE 0
                            END) AS valid_increases
                FROM    price_comparison
                GROUP   BY product)
        SELECT product
        FROM   valid_products
        WHERE  1 = 1
            AND total_records > 1
            AND total_records = valid_increases; 
    """
    )

    # Execute the query
    with engine.connect() as connection:
        result = connection.execute(query).mappings()  # Use .mappings() to get rows as dictionaries
        products = [row["product"] for row in result]

    # Log the results
    logger.info("Products with strictly increasing prices:\n%s", products)


def main() -> None:
    """Entry point for the task1_run_main script."""
    get_products_with_increasing_prices()


if __name__ == "__main__":
    main()
