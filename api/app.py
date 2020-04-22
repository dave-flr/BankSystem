from app import server, db

if __name__ == '__main__':
    db.bind(**server.config['PONY'])
    db.generate_mapping(create_tables=True)
    server.run(debug=True)
