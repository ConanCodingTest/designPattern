"""This is a test file for the Person and Teacher classes."""

class Person:
    """表示一個人的類別，包含姓名、年齡與身高等屬性"""
    visited = 0
    def __init__(self,name, age, height):
        """初始化 Person 物件，設定姓名、年齡與身高。"""
        self.__name = name  #private variable
        self._age = age #protected variable
        self.height = height    #public variable

    def get_name(self):
        """取得姓名"""
        return self.__name
        
    def get_age(self):
        """取得年齡"""
        return self._age
    
    def show_info(self):
        """顯示個人資訊"""
        print (f"Name: {self.__name}, Age: {self._age}, Height: {self.height}")
        print (f"Visited: {Person.visited} times")
        Person.visited += 1

class Teacher(Person):
    """表示一個教師的類別，繼承自 Person 類別，並增加標題屬性"""
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
        self.__title = None  # private variable

    def get_title(self):
        """取得教師的標題"""
        return self.__title
    
    def set_title(self, title):
        """設定教師的標題"""
        self.__title = title
    
    def show_info(self):
        """顯示教師資訊，包含標題"""
        super().show_info()
        print(f"Title: {self.__title}")

def test_person():
    """測試 Person 和 Teacher 類別"""
    tony = Person("Tony", 30, 1.77)
    tony.show_info()
    print()
    jenny = Teacher("Jenny", 34, 1.65)
    jenny.set_title("Professor")
    jenny.show_info()

if __name__ == "__main__":
    test_person()
    print("Testing complete.")
