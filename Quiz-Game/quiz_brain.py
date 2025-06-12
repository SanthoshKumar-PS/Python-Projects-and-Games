class QuizBrain:
    def __init__(self,input1):
        self.quesnumber = 0
        self.correctscore=0
        self.ques_list = input1

    def still_has_question(self):
        if self.quesnumber==len(self.ques_list):
            return False
        else:
            return True

    def next_question(self):
        current_ques= self.ques_list[self.quesnumber]
        self.quesnumber+=1
        userinput=input(f"Q.{self.quesnumber}: {current_ques.text}? (True/False): ")
        if userinput== current_ques.answer:
            self.correctscore+=1
        print(f"Correct answer is {current_ques.answer}")
        print(f"Your current score is {self.correctscore}/{self.quesnumber}")
