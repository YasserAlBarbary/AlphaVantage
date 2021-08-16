from Services.QueryBuilder import Query


def main():
    query = Query()
    query.build_query()
    query.run()


if __name__ == '__main__':
    main()
