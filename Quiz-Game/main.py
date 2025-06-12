from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]
for data in question_data:
    ques_text=data["text"]
    ques_answer=data["answer"]
    newobj=Question(ques_text,ques_answer)
    question_bank.append(newobj)

ques1=QuizBrain(question_bank)
while ques1.still_has_question():
    ques1.next_question()

print("You have completed the quiz")
print(f"Your final score is {ques1.correctscore}/{ques1.quesnumber}")