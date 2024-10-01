from bson.objectid import ObjectId
from .interfaces.orders_repository import OrdersRepositoryInterface


class OrdersRepository(OrdersRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__collection_name = "orders"
        self.__db_connection = db_connection

    def insert_document(self, document: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)

    def insert_list_of_documents(self, list_of_documents: list) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)

    def select_many(self, doc_filter: dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(doc_filter)
        return data

    def select_one(self, doc_filter: dict) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one(doc_filter)
        return data

    def select_many_with_properties(self, doc_filter: dict) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one(
            doc_filter,  # filtro de busca
            {
                "_id": 0,
                "cupom": 0
            }  # Opções de retorno
        )
        return data

    def select_if_property_exists(self) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            {"address": {"$exists": True}},
            {"_id": 0, "itens": 0}
        )
        return data

    def select_by_object_id(self, object_id: str) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one({"_id": ObjectId(object_id)})
        return data

    def edit_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            {"_id": ObjectId('66946242f2c205dcb32056ce')},  # Filtros
            {"$set": {"cupom": True}}   # Edição
        )

    def edit_many_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_many(
            {"itens.refrigerante": {"$exists": True}},  # Filtros
            {"$set": {"itens.refrigerante": 100}}   # Edição
        )

    def edit_registry_with_increment(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            {"_id": ObjectId('66946242f2c205dcb32056ce')},  # Filtros
            {"$inc": {"itens.pizza.quantidade": 50}}   # Edição
        )

    def delete_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_one({"_id": ObjectId('66946242f2c205dcb32056ce')})

    def delete_many_registries(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_many({"itens.refrigerante": {"$exists": True}})
