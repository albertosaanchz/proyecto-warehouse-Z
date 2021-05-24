class Customers:
    def __init__(self, id: int):
        self.__customer_id: int = id

    def get_customer_id() -> int:
        return self.__customer_id
    
    def get_name() -> str:
        return self.__name

    def get_address() -> str:
        return self.__address

    def get_website() -> str:
        return self.__website
    
    def get_credit_limit() -> float:
        return self.__credit_limit

    def set_name(name: str) -> None:
        self.__name = name

    def set_address(address: str) -> None:
        self.__address = address

    def set_website(website: str) -> None:
        self.__website = website
    
    def set_credit_limit(credit_limit: float) -> None:
        self.__credit_limit = credit_limit