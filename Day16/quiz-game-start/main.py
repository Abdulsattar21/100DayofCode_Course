from question_model import Question
from data import question_data

question_bank = []
for ques in question_data:
   questoin = ques["text"]
   answer = ques["answer"]
   new_question = Question(q_text=questoin, q_answer=answer)
   question_bank.append(new_question)

