class Vehicle:

    def __init__(self):

        self.__vehicle_cost=None
        self.__vehicle_type=None
        self.__vehicle_id=None
        self.__premium_amount=None

    def set_vehicle_id(self,vehicle_id):

        self.__vehicle_id=vehicle_id

    def set_vehicle_cost(self,vehicle_cost):

        self.__vehicle_cost=vehicle_cost

    def set_vehicle_type(self,vehicle_type):

        if vehicle_type in  ["TwoWheeler","Four Wheeler"]:

            self.__vehicle_type=vehicle_type

        else:

            return "invalid vehicle Details"

            

    def set_premium_amount(self,premium_amount):

        self.__premium_amount=premium_amount

    def get_vehicle_id(self):

        return self.__vehicle_id

    def get_vehicle_cost(self):

         return self.__vehicle_cost

    def get_vehicle_type(self):

         return self.__vehicle_type

    def get_premium_amount(self):

        return self.__premium_amount

    

    def calculate_premium(self):

        pass

    def display_vehicle_details(self):

        print(self.__vehicle_cost)
        print(self.__vehicle_type)
        print(self.__vehicle_id)
        print(self.__premium_amount)

        

