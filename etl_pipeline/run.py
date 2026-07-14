from etl_pipeline.data_load import load_data


def main():
    print("Loading data into database...\n")

    load_data("data/user_policy_details.csv", "registered_users")
    load_data("data/registered_users.csv", "policy_details")

    print("\nData loaded successfully!")


if __name__ == "__main__":
    main()