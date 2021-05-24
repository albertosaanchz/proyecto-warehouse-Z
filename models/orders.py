class Orders: 
    def __init__(self,id: int):
        self.__order_id: int = id

        def get_order_id() -> int:
            return self.__order_id

        def get_customer_id() -> int:
            return self.__customer_id

        def get_status() -> str:
            return self.__status

        def get_salesman_id() -> int:
            return self.__salesman_id

        def set_customer_id(id: int) -> None:
            self.__customer_id = id

        def set_status(status: str) -> None:
            self.__status = status

        def set_salesman_id(salesman_id: int) -> None:
            self.salesman_id = salesman_id