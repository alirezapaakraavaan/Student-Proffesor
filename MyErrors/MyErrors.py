class MyErrors(Exception):
    def __init__(self, msg=""):
        self.message = msg
        super().__init__(self.message)


    def lecture_not_defined(self):
        self.message = "This class is not defined by proffesor!"
        return self.message
    

    def duplicated_lecture(self):
        self.message = "You can only have a specific lecture once!"
        return self.message
    

    def invalid_point(self):
        self.message = "Your score should be something between 0 to 20!"
        return self.message