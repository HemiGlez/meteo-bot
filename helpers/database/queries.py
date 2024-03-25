
CREATE_TOWNS_TABLE = """
    CREATE TABLE IF NOT EXISTS towns (
        id VARCHAR(24) PRIMARY KEY, 
        name VARCHAR(256) NOT NULL, 
        updated_at DATETIME, 
        forecast VARCHAR(256)
    );
"""

"""
This SQL sentence inserts a new "town" if the id does not exist, 
 it update the name in the case that the id exists and the name is different,
 and it do nothing in the case when the id exists and the name is the same.
"""
INSERT_TOWN = """
    INSERT INTO towns (id, name) 
    VALUES (?, ?)
    ON CONFLICT(id) DO UPDATE SET name = CASE WHEN excluded.name <> towns.name THEN excluded.name ELSE towns.name END;
"""
