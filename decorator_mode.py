from abc import ABCMeta,abstractmethod

#食物抽象类
class Food(metaclass=ABCMeta):
    @abstractmethod
    def get_description(self):
        pass
        """描述"""
    @abstractmethod
    def get_price(self):
        pass
        """价格"""


#实例化食物抽象类，黄焖鸡
class Chicken(Food):
    def __init__(self):
        self.__description = "一份黄焖鸡"
        self.__price = 18.0

    def get_description(self):
        """描述"""
        return self.__description

    def get_price(self):
        """价格"""
        return self.__price

#配菜抽象基类
class Garnish(Food):
    @abstractmethod
    def get_description(self):
        pass
    @abstractmethod
    def get_price(self):
        pass
#辣椒，一份表示微辣，两份中辣，三分特辣
class Chili(Garnish):
    def __init__(self, Food):
        self.baseFood = Food
        self.__description = "+一份辣椒"  # 微辣
        self.__price = 0.0

    def get_description(self):
        return self.baseFood.get_description()+self.__description

    def get_price(self):
        return self.baseFood.get_price()+self.__price

#土豆
class Potato(Garnish):
    def __init__(self, Food):
        self.baseFood = Food
        self.__description = "+一份土豆"  # 微辣
        self.__price = 2.0

    def get_description(self):
        return self.baseFood.get_description()+self.__description
        """描述"""

    def get_price(self):
        return self.baseFood.get_price()+self.__price
        """价格"""



if __name__ == '__main__':
    #现在开始点餐
    chicken = Chicken()

    jack_food = Chili(chicken)
    print('Jack点餐: %s' % jack_food.get_description(), '\n花费: %s' % jack_food.get_price())
    mark_food = Potato(Chili(chicken))
    print('Mark点餐: %s' % mark_food.get_description(), '\n花费: %s' % mark_food.get_price())

    #这时候Tom说要吃特辣
    tom_food = Chili(Chili(Chili(chicken)))
    print('Tom点餐: %s' % tom_food.get_description(), '\n花费: %s' % tom_food.get_price())