class TeacherCRUD:
    def __init__(self, database):
        self.db = database

    def create(self, name: str, ano_nasc: int, cpf: str) -> None:
        try:
            query = "CREATE (:Professor {name: '" + name + "', ano_nasc: " + str(ano_nasc) + " , cpf: '" + cpf + "'})"
            self.db.execute_query(query)
            print("Teacher added successfully!")
        except Exception as error:
            print(f"Error while creating teacher {name}", error)

    def read(self, name: str) -> [dict, None]:
        try:
            query = f"MATCH (p:Professor)" \
                    f"WHERE p.name = '{name}' " \
                    f"RETURN p AS professor"
            result = self.db.execute_query(query)

            if result:
                return result[0]["professor"]
            else:
                print(f"No teacher with name {name} found!")
                return None
        except Exception as error:
            print(f"Error while reading teacher {name}", error)

    def update(self, name, newCpf) -> None:
        try:
            query = f"MATCH (p:Professor)" \
                    f"WHERE p.name = '{name}' " \
                    f"SET p.cpf = '{newCpf}'"
            self.db.execute_query(query)
            print(f"Teacher {name}'s cpf updated successfully!")
        except Exception as error:
            print(f"Error while updating teacher {name}", error)

    def delete(self, name) -> None:
        try:
            query = f"MATCH (p:Professor)" \
                    f"WHERE p.name = '{name}' " \
                    f"DETACH DELETE p"
            self.db.execute_query(query)
            print(f"No teacher with name {name} found!")
        except Exception as error:
            print(f"Error while updating teacher {name}", error)
