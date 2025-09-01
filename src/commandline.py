import argparse

def cliGetDatabaseName():
    # Create the parser
    parser = argparse.ArgumentParser(description="Daily Dues - a task tickler with time tracking")

    # Add arguments
    parser.add_argument("--database", type=str, default="dailydues.db", help="Name (with path if needed) of database to use")

    # Parse the arguments
    args = parser.parse_args()

    # Access the arguments
    if args.database:
        return args.database
    else:
        return "dailydues.db"
